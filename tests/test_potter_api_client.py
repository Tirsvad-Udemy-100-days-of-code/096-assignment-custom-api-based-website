"""@brief Tests for the Potter API client, without network access."""

import io
import json
import urllib.error
from pathlib import Path
from typing import Any

import pytest

from hp_site.domain.errors import ApiUnavailableError, CharacterNotFoundError
from hp_site.infrastructure import potter_api_client
from hp_site.infrastructure.potter_api_client import PotterApiClient, parse_character

FIXTURE = Path(__file__).parent / "fixtures" / "characters.json"


def _serve(monkeypatch: pytest.MonkeyPatch, payload: Any) -> None:
    """@brief Make the client read `payload` instead of calling the network."""

    def fake_urlopen(request: Any, timeout: float) -> io.BytesIO:
        return io.BytesIO(json.dumps(payload).encode("utf-8"))

    monkeypatch.setattr(potter_api_client.urllib.request, "urlopen", fake_urlopen)


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> PotterApiClient:
    """@brief A client that serves the fixture file."""
    _serve(monkeypatch, json.loads(FIXTURE.read_text(encoding="utf-8")))
    return PotterApiClient()


def test_list_characters_returns_all(client: PotterApiClient) -> None:
    """@brief Without a filter every character is returned."""
    assert [c.full_name for c in client.list_characters()] == [
        "Harry James Potter",
        "Draco Malfoy",
        "Luna Lovegood",
    ]


def test_list_characters_filters_by_house_ignoring_case(
    client: PotterApiClient,
) -> None:
    """@brief The house filter ignores letter case."""
    result = client.list_characters("slytherin")
    assert [c.nickname for c in result] == ["Draco"]


def test_get_character_returns_match(client: PotterApiClient) -> None:
    """@brief A known id returns its character."""
    assert client.get_character(2).actor == "Evanna Lynch"


def test_get_character_unknown_raises(client: PotterApiClient) -> None:
    """@brief An unknown id raises CharacterNotFoundError."""
    with pytest.raises(CharacterNotFoundError):
        client.get_character(99)


def test_network_error_raises_unavailable(monkeypatch: pytest.MonkeyPatch) -> None:
    """@brief A network failure becomes ApiUnavailableError."""

    def failing(request: Any, timeout: float) -> None:
        raise urllib.error.URLError("offline")

    monkeypatch.setattr(potter_api_client.urllib.request, "urlopen", failing)
    with pytest.raises(ApiUnavailableError):
        PotterApiClient().list_characters()


def test_non_list_payload_raises_unavailable(monkeypatch: pytest.MonkeyPatch) -> None:
    """@brief An answer that is not a list is rejected."""
    _serve(monkeypatch, {"error": "nope"})
    with pytest.raises(ApiUnavailableError):
        PotterApiClient().list_characters()


def test_parse_character_missing_field_raises() -> None:
    """@brief A character without a name is rejected."""
    with pytest.raises(ApiUnavailableError):
        parse_character({"index": 1})
