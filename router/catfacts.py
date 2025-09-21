"""Test endpoint."""

import logging
import random

from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse

catfacts_router = APIRouter()


# http://localhost:8000/api/upload/v1/ping?some_param=This is the message from xavier
@catfacts_router.get("/ping", include_in_schema=False)
async def ping(some_param: str = None):
    """Test endpoint."""
    return JSONResponse(
        content={
            "message": "Test endpoint!!!1",
            "some_param": f"Your param: {some_param}",
        }
    )


@catfacts_router.get("/catfact", include_in_schema=False)
async def catfact() -> JSONResponse:
    """Return a random cat fact.

    Endpoint: http://localhost:8002/api/facts/v1/catfact
    """
    logging.info("Calling catfacts API endpoint.")

    facts: list[str] = [
        "A cat uses its whiskers for measuring distances.  The whiskers of a cat are capable of registering very small changes in air pressure.",
        "Cats dislike citrus scent.",
        "When a family cat died in ancient Egypt, family members would mourn by shaving off their eyebrows. They also held elaborate funerals during which they drank wine and beat their breasts. The cat was embalmed with a sculpted wooden mask and the tiny mummy was placed in the family tomb or in a pet cemetery with tiny mummies of mice.",
        "A cat's nose is as unique as a human's fingerprint.",
        "Researchers are unsure exactly how a cat purrs. Most veterinarians believe that a cat purrs by vibrating vocal folds deep in the throat. To do this, a muscle in the larynx opens and closes the air passage about 25 times per second.",
        "See cat video: https://youtu.be/VZrDxD0Za9I",
        "Cats have been domesticated for half as long as dogs have been.",
        "Cats have supersonic hearing",
        "House Cats Share 95.6% of Their Genetic Makeup With Tigers.",
        "A House Cat Can Reach Speeds of Up to 30mph.",
        "A group of cats is called a clowder.",
    ]

    chosen_fact: str = random.choice(facts)
    logging.info("Found fact: %s", chosen_fact)

    return JSONResponse(content={"message": "Success", "fact": chosen_fact})


@catfacts_router.get("/blog", include_in_schema=False)
async def blog() -> JSONResponse:
    """Cat blog.

    This returns an HTML page.

    Endpoint: http://localhost:8002/api/facts/v1/blog
    """
    logging.info("Calling blog API endpoint.")

    return HTMLResponse(
        content="""
        <html>
            <body>
                <h1>Blog</h1>
                <p>This is a blog about cats.</p>

                <iframe width="640" height="360" style="border:1px solid
                #e6e6e6"
                src="https://www.krem.com/embeds/video/responsive/293-2555007/iframe"
                allowfullscreen="true" webkitallowfullscreen="true"
                mozallowfullscreen="true"></iframe>

                <br />

                <iframe width="560" height="315"
                src="https://www.youtube-nocookie.com/embed/VZrDxD0Za9I"
                title="YouTube video player" frameborder="0"
                allow="accelerometer; autoplay; clipboard-write;
                encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen></iframe>

            </body>
        </html>
        """
    )
