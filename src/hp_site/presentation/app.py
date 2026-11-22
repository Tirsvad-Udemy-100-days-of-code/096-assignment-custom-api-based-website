"""@brief Flask application factory and controllers."""

from flask import Flask, render_template
from werkzeug.exceptions import NotFound

from hp_site import constants
from hp_site.application.ports import CharacterClient
from hp_site.domain.errors import ApiUnavailableError, CharacterNotFoundError
from hp_site.infrastructure.potter_api_client import PotterApiClient


def create_app(client: CharacterClient | None = None) -> Flask:
    """@brief Build the Flask application.

    @param client Source of characters; the public API client when None.
    @return The configured application.
    """
    app = Flask(__name__)
    source: CharacterClient = client if client is not None else PotterApiClient()

    @app.context_processor
    def inject_globals() -> dict[str, object]:
        """@brief Values every template can use."""
        return {"site_title": constants.SITE_TITLE, "houses": constants.HOUSES}

    @app.get(constants.ROUTE_HOME)
    def home() -> str:
        """@brief Show every character."""
        return render_template(
            "characters.html", characters=source.list_characters(), house=None
        )

    @app.get(constants.ROUTE_HOUSE)
    def house(name: str) -> str:
        """@brief Show the characters of one house.

        @param name Name of the house, in any letter case.
        """
        match = next(
            (h for h in constants.HOUSES if h.casefold() == name.casefold()), None
        )
        if match is None:
            raise NotFound
        return render_template(
            "characters.html", characters=source.list_characters(match), house=match
        )

    @app.get(constants.ROUTE_CHARACTER)
    def character(index: int) -> str:
        """@brief Show one character.

        @param index Id of the character.
        """
        return render_template("character.html", character=source.get_character(index))

    @app.errorhandler(CharacterNotFoundError)
    @app.errorhandler(NotFound)
    def not_found(_error: Exception) -> tuple[str, int]:
        """@brief Show the not-found page."""
        return (
            render_template("error.html", message=constants.MESSAGE_NOT_FOUND),
            constants.STATUS_NOT_FOUND,
        )

    @app.errorhandler(ApiUnavailableError)
    def api_down(_error: Exception) -> tuple[str, int]:
        """@brief Show the page for an unreachable API."""
        return (
            render_template("error.html", message=constants.MESSAGE_API_DOWN),
            constants.STATUS_SERVICE_UNAVAILABLE,
        )

    return app
