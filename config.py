
import os
from typing import Final


# k_service: Final = os.environ.get("K_SERVICE")

config = {
    "MONGO_DATABASE": "dev",
    "MONGO_HOST": os.environ.get("MONGO_HOST"),
    "MONGO_PASSWORD": os.environ.get("MONGO_PASSWORD"),
    "MONGO_USERNAME": os.environ.get("MONGO_USERNAME") or "snapapp",
}