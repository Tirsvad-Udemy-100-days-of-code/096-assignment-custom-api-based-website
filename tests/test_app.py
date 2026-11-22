"""@brief Tests for the website routes, using a fake character client."""

import pytest
from flask.testing import FlaskClient

from hp_site import constants
from hp_site.application.ports import CharacterClient
from hp_site.domain.character import Character
from hp_site.domain.errors import ApiUnavailableError, CharacterNotFoundError
from hp_site.presentation.app import create_app

HARRY = Character(
    0,
    "Harry James Potter",
    "Harry",
    "Gryffindor",
    "Daniel Radcliffe",
    ("Lily Luna Potter",),
    "https://example.test/h.png",
    "Jul 31, 1980",
)
DRACO = Character(
    1, "Draco Malfoy", "Draco", "Slytherin", "Tom Felton", (), "", "Jun 5, 1980"
)


class FakeClient(CharacterClient):
    """@brief In-memory CharacterClient."""

    def list_characters(self, house: str | None = None) -> list[Character]:
        """@brief List the fake characters."""
        items = [HARRY, DRACO]
        return items if house is None else [c for c in items if c.house == house]

    def get_character(self, index: int) -> Character:
        """@brief Get a fake character."""
        for item in (HARRY, DRACO):
            if item.index == index:
                return item
        raise CharacterNotFoundError(str(index))


class DownClient(CharacterClient):
    """@brief CharacterClient whose service is unavailable."""

    def list_characters(self, house: str | None = None) -> list[Character]:
        """@brief Always fail."""
        raise ApiUnavailableError("down")

    def get_character(self, index: int) -> Character:
        """@brief Always fail."""
        raise ApiUnavailableError("down")


@pytest.fixture
def web() -> FlaskClient:
    """@brief Test client of an app with the fake source."""
    return create_app(FakeClient()).test_client()


def test_home_lists_characters(web: FlaskClient) -> None:
    """@brief The home page lists every character."""
    page = web.get("/")
    assert page.status_code == 200
    assert b"Harry James Potter" in page.data
    assert b"Draco Malfoy" in page.data


def test_house_filters_characters(web: FlaskClient) -> None:
    """@brief A house page lists only that house, in any letter case."""
    page = web.get("/house/slytherin")
    assert b"Draco Malfoy" in page.data
    assert b"Harry James Potter" not in page.data


def test_unknown_house_is_not_found(web: FlaskClient) -> None:
    """@brief An unknown house gives 404."""
    assert web.get("/house/narnia").status_code == constants.STATUS_NOT_FOUND


def test_character_page_shows_details(web: FlaskClient) -> None:
    """@brief A character page shows the actor."""
    page = web.get("/character/0")
    assert page.status_code == 200
    assert b"Daniel Radcliffe" in page.data


def test_unknown_character_is_not_found(web: FlaskClient) -> None:
    """@brief An unknown character id gives 404 with the message."""
    page = web.get("/character/99")
    assert page.status_code == constants.STATUS_NOT_FOUND
    assert constants.MESSAGE_NOT_FOUND.encode() in page.data


@pytest.mark.parametrize("path", ["/", "/house/gryffindor", "/character/0"])
def test_api_down_shows_error_page(path: str) -> None:
    """@brief An unavailable API gives status 503 and the error page."""
    page = create_app(DownClient()).test_client().get(path)
    assert page.status_code == constants.STATUS_SERVICE_UNAVAILABLE
    assert constants.MESSAGE_API_DOWN.encode() in page.data
