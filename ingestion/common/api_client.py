import requests
import logging


logger = logging.getLogger(__name__)


def get(url, params=None):

    try:

        response = requests.get(
            url,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()


    except requests.exceptions.RequestException as e:

        logger.error(
            f"API request failed: {e}"
        )

        raise