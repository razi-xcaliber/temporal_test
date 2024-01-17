from temporalio import activity
import requests

@activity.defn
async def say_hello(name: str) -> str:
    print("activity execution started")
    captured_token = activity.info().task_token
    print(captured_token)
    requests.get("http://localhost:5000/", headers={"X-Fission-Params-Token": str(captured_token)})
    print("request call done")
    activity.raise_complete_async()
