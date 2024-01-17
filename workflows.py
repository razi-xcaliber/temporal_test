from datetime import timedelta
from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import say_hello

@workflow.defn
class SayHello:
    signal = ''

    @workflow.signal
    async def hello_signal(self, name: str) -> str:
        self.signal = name

    @workflow.run
    async def run(self, name: str) -> str:
        # op =  await workflow.execute_activity(
        #     say_hello, name, start_to_close_timeout=timedelta(seconds=100)
        # )
        # await workflow.wait_condition(lambda: self.signal == 'GO')
        # return op
        return await workflow.execute_activity(
            say_hello, name, start_to_close_timeout=timedelta(seconds=100)
        )