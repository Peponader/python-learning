from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

#shkl al data al bnst2blha
class promtrequest(BaseModel):
    user_name: str
    prompt: str
    temperature: float = 0.7 
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"msa msa ya, {name} hacker!"} 


# 2. Create a POST route to receive the prompt
@app.post("/ask-agent")
def ask_agent(request: promtrequest):
    return {        "status": "success",
        "received_from": request.user_name,
        "prompt": request.prompt,
        "agent_response": f"AI Agent is processing: '{request.prompt}' with temperature {request.temperature}..."
    }   