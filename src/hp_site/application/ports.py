"""@brief Ports the website depends on."""

from abc import ABC, abstractmethod

from hp_site.domain.character import Character


class CharacterClient(ABC):
    """@brief Source of characters; the website only knows this interface."""

    @abstractmethod
    def list_characters(self, house: str | None = None) -> list[Character]:
        """@brief List characters.

        @param house Name of a house to filter on, or None for every character.
        @return The matching characters, in API order.
        @throws ApiUnavailableError When the service cannot be used.
        """

    @abstractmethod
    def get_character(self, index: int) -> Character:
        """@brief Get one character.

        @param index Id of the character.
        @return The character.
        @throws CharacterNotFoundError When no character has this id.
        @throws ApiUnavailableError When the service cannot be used.
        """
