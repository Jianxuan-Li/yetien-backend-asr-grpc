import os

"""
These models are only for development purposes.
https://asr.yetien.com/docs#/
"""

# APIs for development models:
# https://asr.yetien.com/model/0/asr
# https://asr.yetien.com/model/1/asr

# APIs for production models:
# http://yetien-asr-model-1/asr
# http://yetien-asr-model-2/asr

ASR_DEV_MODEL_HOST = "https://asr.yetien.com"

MODELS = []
MODELS_NUM = 2

for i in range(MODELS_NUM):
    MODELS.append(
        [
            f"{ASR_DEV_MODEL_HOST}/model/{i}/asr",
            os.getenv(f"YETIEN_DEV_MODEL_{i}_USER", ""),
            os.getenv(f"YETIEN_DEV_MODEL_{i}_PWD", ""),
        ]
    )

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_DB = os.getenv("REDIS_DB")
