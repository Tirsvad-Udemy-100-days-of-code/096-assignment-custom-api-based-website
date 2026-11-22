"""@brief Errors raised by the domain and its ports."""


class ApiUnavailableError(Exception):
    """@brief The character service cannot be reached or answered badly."""


class CharacterNotFoundError(Exception):
    """@brief No character exists with the requested id."""
