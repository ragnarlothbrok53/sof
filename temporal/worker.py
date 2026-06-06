import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from temporal.workflows import ExampleWorkflow

import os

TASK_QUEUE = "slm-task-queue"
TEMPORAL_ADDRESS = os.getenv("TEMPORAL_ADDRESS", "127.0.0.1:7233")

async def main() -> None:
    client = await Client.connect(TEMPORAL_ADDRESS)
    worker = Worker(
        client,
        task_queue=TASK_QUEUE,
        workflows=[ExampleWorkflow],
    )
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
