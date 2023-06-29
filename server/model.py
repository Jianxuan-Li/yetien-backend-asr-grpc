from heapq import heappush, heappop, heapify
from time import monotonic
import threading
from .lib import Singleton

MODEL_NUM = 2

class Model(metaclass=Singleton):
    def __init__(self) -> None:
        self.in_use = set()
        self.not_use = heapify(range(MODEL_NUM))
        self.lock = threading.Lock()

    def _get_available_model(self) -> int | None:
        self.lock.acquire()

        if len(self.not_use) == 0:
            return None

        model_id = heappop(self.not_use)
        self.in_use.add(model_id)

        self.lock.release()
        return model_id
    
    def _release_model(self, model_id) -> None:
        self.lock.acquire()
        if model_id in self.in_use:
            self.in_use.remove(model_id)
            heappush(self.not_use, model_id)
        self.lock.release()

    def use(self):
        model_id = self._get_available_model()
        if model_id is None:
            return None
        start_time = monotonic()

        # TODO: schedule the task to the model
        # TODO: if the model is not available, save the task to the queue, and wait for the model to be available

        # once the task is done, release the model
        self._release_model(model_id)
        duration = monotonic() - start_time
        return model_id, duration
