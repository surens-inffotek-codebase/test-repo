from fastapi import FastAPI, status
# from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()
# Configure CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins, adjust as needed
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods, adjust as needed
#     allow_headers=["*"],  # Allows all headers, adjust as needed
# )
@app.get("/")
async def root():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Hello, World!"})

@app.get("/health")
async def health_check():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Status": "Healthy"})

@app.post("/echo")
async def echo(data: dict):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"received": data})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info")