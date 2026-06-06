from fastapi import APIRouter, HTTPException, Request

from temporal.workflows import ExampleWorkflow

from api.models.request_models import RunWorkflowRequest


router = APIRouter()


@router.post("/workflow/run")
async def run_workflow(request_data: RunWorkflowRequest, request: Request):
    try:
        handle = await request.app.state.temporal_client.start_workflow(
            ExampleWorkflow.run,
            request_data.input_data or {},
            id=request_data.workflow_id,
            task_queue=request_data.task_queue,
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    return {"workflow_id": handle.id, "run_id": handle.run_id}
