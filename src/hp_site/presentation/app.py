"""@brief Flask application factory and the website controller."""

from flask import Flask, render_template
from werkzeug.exceptions import NotFound

from hp_site import constants
from hp_site.application.ports import CharacterClient
from hp_site.domain.errors import ApiUnavailableError, CharacterNotFoundError
from hp_site.infrastructure.potter_api_client import PotterApiClient


class SiteController:
    """@brief Controller of the website: one method per page."""

    def __init__(self, source: CharacterClient) -> None:
        """@brief Create the controller.

        @param source Source of characters.
        """
        self._source = source

    def home(self) -> str:
        """@brief Show every character."""
        return render_template(
            "characters.html", characters=self._source.list_characters(), house=None
        )

    def house(self, name: str) -> str:
        """@brief Show the characters of one house.

        @param name Name of the house, in any letter case.
        @throws NotFound When the house does not exist.
        """
        wanted = name.casefold()
        match = next((h for h in constants.HOUSES if h.casefold() == wanted), None)
        if match is None:
            raise NotFound
        return render_template(
            "characters.html",
            characters=self._source.list_characters(match),
            house=match,
        )

    def character(self, index: int) -> str:
        """@brief Show one character.

        @param index Id of the character.
        """
        return render_template(
            "character.html", character=self._source.get_character(index)
        )

    def not_found(self, _error: Exception) -> tuple[str, int]:
        """@brief Show the not-found page."""
        return (
            render_template("error.html", message=constants.MESSAGE_NOT_FOUND),
            constants.STATUS_NOT_FOUND,
        )

    def api_down(self, _error: Exception) -> tuple[str, int]:
        """@brief Show the page for an unreachable API."""
        return (
            render_template("error.html", message=constants.MESSAGE_API_DOWN),
            constants.STATUS_SERVICE_UNAVAILABLE,
        )


def _inject_globals() -> dict[str, object]:
    """@brief Values every template can use."""
    return {"site_title": constants.SITE_TITLE, "houses": constants.HOUSES}


def create_app(client: CharacterClient | None = None) -> Flask:
    """@brief Build the Flask application.

    @param client Source of characters; the public API client when None.
    @return The configured application.
    """
    app = Flask(__name__)
    controller = SiteController(client if client is not None else PotterApiClient())
    app.context_processor(_inject_globals)
    app.add_url_rule(constants.ROUTE_HOME, "home", controller.home)
    app.add_url_rule(constants.ROUTE_HOUSE, "house", controller.house)
    app.add_url_rule(constants.ROUTE_CHARACTER, "character", controller.character)
    app.register_error_handler(CharacterNotFoundError, controller.not_found)
    app.register_error_handler(NotFound, controller.not_found)
    app.register_error_handler(ApiUnavailableError, controller.api_down)
    return app
