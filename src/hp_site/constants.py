"""@brief Constants shared across the project.

@details Every literal that is used in more than one place, or that a reader
may want to change, lives here.
"""

## Name shown in page titles.
SITE_TITLE: str = "Wizarding World Characters"

## Base address of the public Harry Potter API.
API_BASE_URL: str = "https://hp-api.onrender.com/api"

## Seconds to wait for the API before giving up.
API_TIMEOUT_SECONDS: float = 10.0

## Host and port of the local development server.
DEFAULT_HOST: str = "127.0.0.1"
DEFAULT_PORT: int = 5000
