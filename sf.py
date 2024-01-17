import time
from flask import Flask, request
from temporalio.client import Client
    
app = Flask(__name__)

@app.route("/")
async def hello_world():
    print("sleeping...")
    time.sleep(10)
    token = request.headers["X-Fission-Params-Token"]
    print(token)
    client = await Client.connect("localhost:7233", namespace="default")
    handle = client.get_async_activity_handle(task_token=bytes(token, "utf-8"))
    
    await handle.complete(result="Hello from Fission!")