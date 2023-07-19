import asyncio
import time
import requests
from settings import MODELS
from s3 import generate_presigned_url


class Task:
    def __init__(self) -> None:
        pass

    def run(self, speaking_id: str, obj_id: str) -> str:
        req_file = {"audio_file": self.get_audio(obj_id)}
        req_param = {"task": "transcribe", "output": "json"}
        model_url = MODELS[0][0]
        model_username = MODELS[0][1]
        model_password = MODELS[0][2]
        print("start to send request to model server: ", model_url)
        r = requests.post(
            model_url,
            files=req_file,
            params=req_param,
            auth=(model_username, model_password),
        )

        if r.status_code != 200:
            print("response from model server: ", r.status_code)
            print(r)
            return {"error": "bad model response"}

        return r.json()

    def get_audio(self, obj_id: str) -> str:
        self.obj_id = obj_id
        url = generate_presigned_url(obj_id)
        print("download file from:", url)
        file_obj = requests.get(url)
        return file_obj.content

    def __str__(self) -> str:
        return f"Task: {self.obj_id}"
