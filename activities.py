import time
from temporalio import activity

@activity.defn
async def say_hello(name: str) -> str:
    # activity.heartbeat("lubb dubb")
    # for i in range(0, 100): 
    #     brrr()
    #     time.sleep(1)
    return f"Hello, {name}!"


def brrr(): 
    print("brrr")