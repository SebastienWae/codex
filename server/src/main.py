import importlib.metadata

from fastapi import FastAPI

__version__ = importlib.metadata.version("codex")

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": f"Hello World: {__version__}"}
