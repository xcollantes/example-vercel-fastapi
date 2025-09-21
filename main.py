"""Main module entrypoint for API service."""

import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import catfacts


app = FastAPI()

# Router objects.
# TODO: Add routers here.
app.include_router(catfacts.catfacts_router)  # For testing.

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Update this to ideally only be the frontend URLs.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.environ.get("APP_URL", "0.0.0.0"),
        port=int(os.environ.get("APP_PORT_NUM", 8000)),
        reload=False,
    )
