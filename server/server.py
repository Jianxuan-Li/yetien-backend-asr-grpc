import asyncio
import logging
import grpc
from time import monotonic
from task import Task

_pb2, _pb2_grpc = grpc.protos_and_services("asrserver.proto")
t = Task()


class AsrModelRunner(_pb2_grpc.AsrServicer):
    def __init__(self):
        pass

    async def RunAsr(
        self, request: _pb2.NewTaskRequest, context: grpc.aio.ServicerContext
    ) -> _pb2.TaskRecieved:
        if t.model_in_use:
            return _pb2.TaskRecieved(status=False, text="", duration=0, error="model is in use")

        logging.info("Task: %s, %s", request.speaking_id, request.object_id)
        start_time = monotonic()
        result = t.run(request.speaking_id, request.object_id)
        duration = monotonic() - start_time
        status = True
        if not result or "text" not in result or len(result["text"]) == 0:
            status = False
        if "error" in result:
            status = False
            message = result["error"]
            return _pb2.TaskRecieved(status=status, text="", duration=duration, error=message)
        logging.info("Task: %s, status: %s, text: %s \nduration %.2f", request.speaking_id, "success" if status else "failed", result["text"], duration)
        return _pb2.TaskRecieved(status=status, text=result["text"], duration=duration, error="")


async def serve() -> None:
    server = grpc.aio.server()
    _pb2_grpc.add_AsrServicer_to_server(AsrModelRunner(), server)
    listen_addr = "[::]:9000"
    server.add_insecure_port(listen_addr)
    logging.info("Starting ASR model server on %s", listen_addr)
    logging.basicConfig(level=logging.INFO)
    await server.start()
    await server.wait_for_termination()
