from temporalio import workflow

@workflow.defn
class ExampleWorkflow:
    @workflow.run
    async def run(self, input_data: dict) -> dict:
        return {"received": input_data}
