import asyncio
import logging
import random
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
        print("status: ", "success" if status else "failed")
        print("text: ", result["text"])
        print("duration: ", duration)
        return _pb2.TaskRecieved(status=status, text=result["text"], duration=duration, error="")


async def serve() -> None:
    server = grpc.aio.server()
    _pb2_grpc.add_AsrServicer_to_server(AsrModelRunner(), server)
    listen_addr = "[::]:9000"
    server.add_insecure_port(listen_addr)
    logging.info("Starting ASR model server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()
