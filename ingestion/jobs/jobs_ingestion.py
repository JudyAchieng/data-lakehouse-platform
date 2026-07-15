from ingestion.common.api_client import get
from ingestion.common.storage import save_json
from ingestion.common.logger import get_logger
from ingestion.common.config_loader import load_config


logger=get_logger(__name__)


def ingest_jobs():

    config=load_config()

    keywords=config["jobs"]["keywords"]
    bronze_path = config["storage"]["bronze_path"]


    url="https://remotive.com/api/remote-jobs"

#for keyword in keywords:
    params={

         "search": keywords



    }


    logger.info(
        "Jobs ingestion started"
    )


    data=get(url,params)


    location=save_json(
        data,
        "jobs",
        bronze_path
    )


    logger.info(
        f"Saved {location}"
    )


if __name__=="__main__":

    ingest_jobs()