"""@brief Tests for the shared constants."""

from hp_site import constants


def test_api_base_url_is_https() -> None:
    """@brief The API address uses a secure scheme."""
    assert constants.API_BASE_URL.startswith("https://")


def test_timeout_is_positive() -> None:
    """@brief The timeout is a positive number of seconds."""
    assert constants.API_TIMEOUT_SECONDS > 0
