import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "server"))

import asyncio
import logging
from server.server import serve

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
