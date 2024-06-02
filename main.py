import uvicorn
from api.app import app

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8081, reload=False, access_log=True)
