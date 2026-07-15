from ingestion.common.api_client import get
from ingestion.common.storage import save_json
from ingestion.common.logger import get_logger
from ingestion.common.config_loader import load_config


logger=get_logger(__name__)


def ingest_crypto():

    config=load_config()

    coins=config["crypto"]["coins"]
    bronze_path = config["storage"]["bronze_path"]


    url="https://api.coingecko.com/api/v3/simple/price"


    params={

         "ids": ",".join(coins),

        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true",
        "include_24hr_change": "true"




    }


    logger.info(
        "Crypto ingestion started"
    )


    data=get(url,params)


    location=save_json(
        data,
        "crypto",
        bronze_path
    )


    logger.info(
        f"Saved {location}"
    )


if __name__=="__main__":

    ingest_crypto()