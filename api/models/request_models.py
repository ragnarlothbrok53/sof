from typing import Any, Optional

from pydantic import BaseModel


class RunWorkflowRequest(BaseModel):
    workflow_id: str
    task_queue: str = "slm-task-queue"
    input_data: Optional[dict[str, Any]] = None
