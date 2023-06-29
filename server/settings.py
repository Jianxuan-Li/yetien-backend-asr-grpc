import os

"""
These models are only for development purposes.
https://asr.yetien.com/docs#/
"""

ASR_DEV_MODEL_HOST = "https://asr.yetien.com"

MODELS = []
MODELS_NUM = 2

for i in range(MODELS_NUM):
    MODELS.append([
        f"{ASR_DEV_MODEL_HOST}/model/{i}",
        os.getenv(f"YETIEN_DEV_MODEL_{i}_USER", ""),
        os.getenv(f"YETIEN_DEV_MODEL_{i}_PWD", ""),
    ])


REDIS_HOST=os.getenv("REDIS_HOST")
REDIS_PORT=os.getenv("REDIS_PORT")
REDIS_DB=os.getenv("REDIS_DB")