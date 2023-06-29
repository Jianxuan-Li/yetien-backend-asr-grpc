import os

"""
These models are only for development purposes.
https://asr.yetien.com/docs#/
"""

ASR_DEV_MODEL_HOST = "https://asr.yetien.com"

MODELS = []
MODELS_NUM = 2

for i in range(1, MODELS_NUM + 1):
    MODELS.append([
        f"{ASR_DEV_MODEL_HOST}/model/{i}",
        os.getenv(f"YETIEN_DEV_MODEL_{i}_USER", ""),
        os.getenv(f"YETIEN_DEV_MODEL_{i}_PWD", ""),
    ])
