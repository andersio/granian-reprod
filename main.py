import io
import os
from random import randbytes
from fastapi import APIRouter, FastAPI
from fastapi.middleware import Middleware
from fastapi.responses import StreamingResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse

from distutils.util import strtobool

router = APIRouter(prefix="/stream")

class ReprodMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        return await call_next(request)

BYTES_TO_RETURN = randbytes(1_000_000)

@router.post("/pdf", response_class=StreamingResponse)
async def streaming_bytes() -> StreamingResponse:
    return StreamingResponse(
        io.BytesIO(BYTES_TO_RETURN),
        media_type="application/octet-stream",
    )

app = FastAPI(
    middleware=[
        Middleware(ReprodMiddleware),
    ] if strtobool(os.environ.get("USE_HTTP_MIDDLEWARE", "no")) else []
)
app.include_router(router)
