"""@brief An application whose character service is always unavailable.

@details Used to capture the error page for the screenshots.
"""

from flask import Flask

from hp_site.application.ports import CharacterClient
from hp_site.domain.character import Character
from hp_site.domain.errors import ApiUnavailableError
from hp_site.presentation.app import create_app


class OfflineClient(CharacterClient):
    """@brief CharacterClient that always reports the service as down."""

    def list_characters(self, house: str | None = None) -> list[Character]:
        """@brief Always fail."""
        raise ApiUnavailableError("offline")

    def get_character(self, index: int) -> Character:
        """@brief Always fail."""
        raise ApiUnavailableError("offline")


def create_offline_app() -> Flask:
    """@brief Build the application with the offline client."""
    return create_app(OfflineClient())
