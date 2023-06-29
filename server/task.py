from .settings import MODELS

class Task:
    def __init__(self, obj_id: str, model_id: int) -> None:
        self.obj_id = obj_id
        self.model_id = model_id

    def run(self) -> str:
        model = self.get_model()
        audio = self.get_audio()

        # TODO: run model with audio
        pass

    def get_model(self) -> str:
        return MODELS[self.model_id - 1]
    
    def get_audio(self) -> str:
        # TODO: fetch audio from S3 with obj_id
        pass

    def __str__(self) -> str:
        return f"Task {self.obj_id} on model {self.model_id}"