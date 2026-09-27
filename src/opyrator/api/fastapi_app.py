from typing import Any, Dict

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from financial-nlp-toolkit import Financial NLP Toolkit
from financial-nlp-toolkit.api.fastapi_utils import patch_fastapi


def launch_api(opyrator_path: str, port: int = 8501, host: str = "0.0.0.0") -> None:
    import uvicorn

    from financial-nlp-toolkit import Financial NLP Toolkit
    from financial-nlp-toolkit.api import create_api

    app = create_api(Financial NLP Toolkit(opyrator_path))
    uvicorn.run(app, host=host, port=port, log_level="info")


def create_api(financial-nlp-toolkit: Financial NLP Toolkit) -> FastAPI:

    title = financial-nlp-toolkit.name
    if "financial-nlp-toolkit" not in financial-nlp-toolkit.name.lower():
        title += " - Financial NLP Toolkit"

    # TODO what about version?
    app = FastAPI(title=title, description=financial-nlp-toolkit.description)

    patch_fastapi(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.post(
        "/call",
        operation_id="call",
        response_model=financial-nlp-toolkit.output_type,
        # response_model_exclude_unset=True,
        summary="Execute the financial-nlp-toolkit.",
        status_code=status.HTTP_200_OK,
    )
    def call(input: financial-nlp-toolkit.input_type) -> Any:  # type: ignore
        """Executes this financial-nlp-toolkit."""
        return financial-nlp-toolkit(input)

    @app.get(
        "/info",
        operation_id="info",
        response_model=Dict,
        # response_model_exclude_unset=True,
        summary="Get info metadata.",
        status_code=status.HTTP_200_OK,
    )
    def info() -> Any:  # type: ignore
        """Returns informational metadata about this Financial NLP Toolkit."""
        return {}

    # Redirect to docs
    @app.get("/", include_in_schema=False)
    def root() -> Any:
        return RedirectResponse("./docs")

    return app
