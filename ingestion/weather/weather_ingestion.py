from ingestion.common.api_client import get
from ingestion.common.storage import save_json
from ingestion.common.logger import get_logger
from ingestion.common.config_loader import load_config


logger=get_logger(__name__)


def ingest_weather():

    config=load_config()

    latitude=config["weather"]["city"]["latitude"]

    longitude=config["weather"]["city"]["longitude"]

    bronze_path = config["storage"]["bronze_path"]


    url="https://api.open-meteo.com/v1/forecast"


    params={

        "latitude":latitude,

        "longitude":longitude,

        "hourly":
        "temperature_2m,relativehumidity_2m"

    }


    logger.info(
        "Weather ingestion started"
    )


    data=get(url,params)


    location=save_json(
        data,
        "weather",
        bronze_path
    )


    logger.info(
        f"Saved {location}"
    )


if __name__=="__main__":

    ingest_weather()