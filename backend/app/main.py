from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Time Complexity Analyzer API",
    description="A backend API that predicts time complexity of Python and Java code.",
    version="1.0.0"
)

app.include_router(router, prefix="/api")


@app.get("/")
def root():
    return {
        "message": "Time Complexity Analyzer API is running.",
        "docs": "/docs",
        "health": "/api/health",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
