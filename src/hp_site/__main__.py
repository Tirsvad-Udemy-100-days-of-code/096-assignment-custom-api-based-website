"""@brief Start the website: `python -m hp_site`."""

from hp_site import constants
from hp_site.presentation.app import create_app


def main() -> None:
    """@brief Run the local development server."""
    create_app().run(host=constants.DEFAULT_HOST, port=constants.DEFAULT_PORT)


if __name__ == "__main__":
    main()
