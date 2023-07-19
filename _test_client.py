import json
import logging

import grpc

_pb2, _pb2_grpc = grpc.protos_and_services("server/asrserver.proto")

# test_args = {
#     "speaking_id": "d7dc8797-1052-451a-8c2a-5a8b0d9ad796",
#     "object_id": "sample1.flac",
# }

# test_args = {
#     "speaking_id": "f7aeeca9-03c7-403e-9d00-ddcbc14d1580",
#     "object_id": "d0c726ee-fe09-48a5-ba0a-aa2f40aae246.wav-aaa",
# }

test_args = {
    "speaking_id": "b1421b42-6c6a-4ee1-9560-b298b75700fc",
    "object_id": "f2a5283a-05b0-49c6-bf6b-5cdddd695bb8.wav-aaa",
}

def run():
    with grpc.insecure_channel("localhost:9000") as channel:
        stub = _pb2_grpc.AsrStub(channel)
        response = stub.RunAsr(_pb2.NewTaskRequest(**test_args))
        print("message received: " + "success" if response.status else "failed")
        print("text: " + response.text)
        print("duration: " + str(response.duration))


if __name__ == "__main__":
    logging.basicConfig()
    run()
