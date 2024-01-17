from temporalio.client import Client
import asyncio


async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    handle = client.get_workflow_handle("hello-workflow")
    await handle.signal("hello_signal", "GO")


if __name__ == "__main__":
    asyncio.run(main())