from fastapi import FastAPI

app=FastAPI(title="OptiPrompt AI",
            description="LLM Token Optimization Platform",
            version="0.1.0")

@app.get("/")
def root():
    return{
        "message":"Welcome to OptiPrompt AI",
        "status": "running"
    }