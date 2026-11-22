"""@brief HTTP client for the public Potter API, built on the standard library."""

import json
import urllib.error
import urllib.request
from typing import Any

from hp_site import constants
from hp_site.application.ports import CharacterClient
from hp_site.domain.character import Character
from hp_site.domain.errors import ApiUnavailableError, CharacterNotFoundError


def parse_character(raw: dict[str, Any]) -> Character:
    """@brief Turn one JSON object of the API into a Character.

    @param raw The decoded JSON object.
    @return The character.
    @throws ApiUnavailableError When a required field is missing or has a wrong type.
    """
    try:
        return Character(
            index=int(raw["index"]),
            full_name=str(raw["fullName"]),
            nickname=str(raw.get("nickname", "")),
            house=str(raw.get("hogwartsHouse", "")),
            actor=str(raw.get("interpretedBy", "")),
            children=tuple(str(name) for name in raw.get("children", [])),
            image=str(raw.get("image", "")),
            birthdate=str(raw.get("birthdate", "")),
        )
    except (KeyError, TypeError, ValueError) as err:
        raise ApiUnavailableError("The API returned an unexpected character") from err


class PotterApiClient(CharacterClient):
    """@brief CharacterClient that reads the public Potter API."""

    def __init__(
        self,
        base_url: str = constants.API_BASE_URL,
        timeout: float = constants.API_TIMEOUT_SECONDS,
    ) -> None:
        """@brief Create the client.

        @param base_url Address of the API, without a trailing slash.
        @param timeout Seconds to wait for an answer.
        """
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout

    def _fetch_characters(self) -> list[Character]:
        """@brief Download and parse every character.

        @return All characters.
        @throws ApiUnavailableError On network errors or malformed data.
        """
        request = urllib.request.Request(
            self._base_url + constants.API_CHARACTERS_PATH,
            headers={"User-Agent": constants.API_USER_AGENT},
        )
        try:
            with urllib.request.urlopen(request, timeout=self._timeout) as response:
                payload = json.load(response)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as err:
            raise ApiUnavailableError("The character service is not available") from err
        if not isinstance(payload, list):
            raise ApiUnavailableError("The API returned an unexpected answer")
        return [parse_character(item) for item in payload]

    def list_characters(self, house: str | None = None) -> list[Character]:
        """@copydoc CharacterClient::list_characters"""
        characters = self._fetch_characters()
        if house is None:
            return characters
        wanted = house.casefold()
        return [item for item in characters if item.house.casefold() == wanted]

    def get_character(self, index: int) -> Character:
        """@copydoc CharacterClient::get_character"""
        for item in self._fetch_characters():
            if item.index == index:
                return item
        raise CharacterNotFoundError(f"No character with id {index}")
