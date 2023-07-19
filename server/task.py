import asyncio
import time
import requests
import logging
from time import monotonic
from settings import MODELS
from s3 import generate_presigned_url


class Task:
    def __init__(self) -> None:
        self.model_in_use = False

    async def run(self, speaking_id: str, obj_id: str) -> str:
        if self.model_in_use:
            return {"error": "model is in use"}

        self.model_in_use = True

        try:
            req_file = {"audio_file": self.get_audio(obj_id)}
            req_param = {"task": "transcribe", "output": "json"}
            model_url = MODELS[0][0]
            model_username = MODELS[0][1]
            model_password = MODELS[0][2]
            logging.info("start to send request to model server: %s", model_url)
            r = requests.post(
                model_url,
                files=req_file,
                params=req_param,
                auth=(model_username, model_password),
            )

            if r.status_code != 200:
                logging.error("bad model response: ", r.status_code)
                return {"error": "bad model response"}
            
            self.model_in_use = False
        except Exception as e:
            logging.exception("error when sending request to model server")
            self.model_in_use = False
            return {"error": "error when sending request to model server"}

        return r.json()

    def get_audio(self, obj_id: str) -> str:
        self.obj_id = obj_id
        logging.info("start to download file: %s, %s", obj_id, str(type(obj_id)))
        url = generate_presigned_url(obj_id)
        start_time = monotonic()
        file_obj = requests.get(url)
        duration = monotonic() - start_time
        logging.info("download file: %s, duration: %.2f", obj_id, duration)
        return file_obj.content

    def __str__(self) -> str:
        return f"Task: {self.obj_id}"
