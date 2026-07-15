import json
from datetime import datetime
import os


#def save_json(data, folder):
def save_json(data, folder, bronze_path):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    path = (
        #f"bronze/{folder}/"
        f"{bronze_path}/{folder}/"
        f"{timestamp}.json"
    )


    os.makedirs(
        os.path.dirname(path),
        exist_ok=True
    )


    with open(path,"w") as file:

        json.dump(
            data,
            file,
            indent=4
        )


    return path