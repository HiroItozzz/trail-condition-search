from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Trail Condition Search API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}