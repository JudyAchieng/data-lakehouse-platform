from datetime import datetime

from ingestion.common.api_client import get
from ingestion.common.storage import save_json
from ingestion.common.logger import get_logger
from ingestion.common.config_loader import load_config

logger = get_logger(__name__)


def ingest_jobs():

    config = load_config()

    jobs_config = config["jobs"]

    keywords = jobs_config["keywords"]

    bronze_path = config["storage"]["bronze_path"]

    url = "https://remotive.com/api/remote-jobs"

    logger.info("Jobs ingestion started")

    for keyword in keywords:

        try:

            logger.info(f"Searching jobs for: {keyword}")

            params = {
                "search": keyword
            }

            data = get(url, params)

            if not data:
                logger.warning(f"No response for '{keyword}'")
                continue

            if "jobs" not in data:
                logger.warning(f"Invalid response for '{keyword}'")
                continue

            output = {
                "ingestion_timestamp": datetime.utcnow().isoformat(),
                "source": "remotive",
                "search_term": keyword,
                "record_count": len(data["jobs"]),
                "data": data
            }

            folder = f"jobs/{keyword.replace(' ', '_')}"

            location = save_json(
                output,
                folder,
                bronze_path
            )

            logger.info(
                f"{keyword}: {len(data['jobs'])} jobs saved to {location}"
            )

        except Exception as e:

            logger.error(
                f"Failed to ingest '{keyword}': {e}"
            )

    logger.info("Jobs ingestion completed")


if __name__ == "__main__":

    ingest_jobs()