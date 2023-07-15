import json
import logging

import grpc

_pb2, _pb2_grpc = grpc.protos_and_services("asrserver.proto")

test_args = {
    "speaking_id": "d7dc8797-1052-451a-8c2a-5a8b0d9ad796",
    "object_id": "sample1.flac",
}


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = _pb2_grpc.AsrStub(channel)
        response = stub.RunAsr(_pb2.NewTaskRequest(**test_args))
        print("message received: " + "success" if response.status else "failed")
        print("text: " + response.text)
        print("duration: " + str(response.duration))


if __name__ == "__main__":
    logging.basicConfig()
    run()
