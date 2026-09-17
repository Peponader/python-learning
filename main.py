from fastapi import FastAPI
app = FastAPI()

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"msa msa ya {name}, ready l-bna2 el-AI Agent?"}