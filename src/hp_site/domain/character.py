"""@brief The Character entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Character:
    """@brief A character of the wizarding world.

    @param index Position of the character in the API list, used as its id.
    @param full_name Full name of the character.
    @param nickname Short name or nickname.
    @param house Name of the Hogwarts house.
    @param actor Name of the actor who plays the character.
    @param children Names of the children of the character.
    @param image Address of a picture of the character.
    @param birthdate Date of birth as text.
    """

    index: int
    full_name: str
    nickname: str
    house: str
    actor: str
    children: tuple[str, ...]
    image: str
    birthdate: str
