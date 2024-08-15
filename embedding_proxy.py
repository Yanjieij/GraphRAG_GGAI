import json
from fastapi import FastAPI, HTTPException
import uvicorn
import httpx
from pydantic import BaseModel
from typing import List, Union

import os

app = FastAPI()

OLLAMA_URL = "http://localhost:11434"  # Default Ollama URL

class EmbeddingRequest(BaseModel):
    input: Union[str, List[str]]
    model: str

class EmbeddingResponse(BaseModel):
    object: str
    data: List[dict]
    model: str
    usage: dict

@app.post("/embeddings")
@app.post("/api/embeddings")
@app.post("/v1/embeddings")
@app.post("/v1/api/embeddings")
async def create_embedding(request: EmbeddingRequest):
    async with httpx.AsyncClient() as client:
        if isinstance(request.input, str):
            request.input = [request.input]

        ollama_requests = [{"model": request.model, "input": text} for text in request.input]

        embeddings = []


        for i, ollama_request in enumerate(ollama_requests):
            # print(ollama_request)

            request_file_path = f"ollama_request_{i}.json"
            with open(request_file_path, "w") as f:
                json.dump(ollama_request, f)

            response = await client.post(f"{OLLAMA_URL}/api/embed", json=ollama_request)

            result = response.json()

            result_file_path = f"result_{i}.json"
            with open(result_file_path, "w") as f:
                json.dump(result, f)

            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail="Ollama API error")
        

            embeddings.append({
                "object": "embedding",
                "embedding": result["embeddings"],
                "index": i
            })
            

        return EmbeddingResponse(
            object="list",
            data=embeddings,
            model=request.model,
            usage={},
        )

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run the embedding proxy server")
    parser.add_argument("--port", type=int, default=11435, help="Port to run the server on")
    parser.add_argument("--host", type=str, default="http://localhost:11434", help="URL of the Ollama server")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload for development")
    args = parser.parse_args()

    OLLAMA_URL = args.host
    uvicorn.run("embedding_proxy:app", host="0.0.0.0", port=args.port, reload=args.reload)
