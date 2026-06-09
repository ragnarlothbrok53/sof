# SLM Orchestration Framework (SOF)

## Project Overview

SOF is a robust and scalable framework designed for orchestrating Small Language Model (SLM) workflows. It leverages FastAPI for building high-performance APIs and Temporal for reliable, fault-tolerant workflow execution. This framework is ideal for managing complex, long-running AI tasks, ensuring their completion even in the face of failures.

## Key Features

*   **Scalable API:** Built with FastAPI, providing a fast and efficient interface for interacting with SLM workflows.
*   **Fault-Tolerant Workflows:** Utilizes Temporal to define and execute durable workflows, ensuring that tasks are completed reliably and can recover from interruptions.
*   **Modular Architecture:** Designed with a clear separation of concerns, making it easy to extend and maintain.
*   **Containerized Deployment:** Includes Dockerfile and docker-compose for easy setup and deployment in various environments.

## Technical Stack

*   **Backend Framework:** FastAPI
*   **Workflow Orchestration:** Temporal
*   **Containerization:** Docker, Docker Compose
*   **Language:** Python 3.13+

## Getting Started

To get started with SOF, clone the repository and follow the instructions below.

### Prerequisites

*   Docker and Docker Compose
*   Python 3.13+

### Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ragnarlothbrok53/sof.git
    cd sof
    ```
2.  **Set up environment variables:**
    (Add instructions for any necessary environment variables here)
3.  **Run with Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    This will start the FastAPI application and the Temporal worker.

## API Endpoints

The API documentation will be available at `/docs` or `/redoc` once the application is running.

## Workflow Definitions

Temporal workflows are defined in `temporal/workflows.py` and activities in `temporal/activities.py`.

## Contributing

Contributions are welcome! Please refer to the `CONTRIBUTING.md` (if available) for guidelines.

## License

This project is licensed under the MIT license - see the `LICENSE` file for details.
