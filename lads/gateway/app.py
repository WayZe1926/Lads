from fastapi import FastAPI, Request
from gateway.ztna import verify_identity
from edge.analyzer import analyze_request
from stream.event_bus import publish_event

app = FastAPI()

@app.post("/event")
async def event(req: Request):

    data = await req.json()

    identity = verify_identity(data)

    if identity == "DENY":
        return {"status": "DENIED"}

    result = analyze_request(data)

    publish_event({
        "ip": data["ip"],
        "score": result["score"],
        "action": result["action"]
    })

    return result