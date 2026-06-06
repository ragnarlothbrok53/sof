import os

from fastapi import FastAPI
from temporalio.client import Client

from api.v1.router import api_router

app = FastAPI(
    title="SLM Orchestration Framework",
    description="API gateway for Temporal workflows",
    version="0.1.0",
)

TEMPORAL_ADDRESS = os.getenv("TEMPORAL_ADDRESS", "127.0.0.1:7233")

@app.on_event("startup")
async def startup_event():
    app.state.temporal_client = await Client.connect(TEMPORAL_ADDRESS)

@app.on_event("shutdown")
async def shutdown_event():
    pass

# We mount the v1 router at /api/v1
app.include_router(api_router, prefix="/api/v1")
