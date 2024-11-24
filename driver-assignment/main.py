import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

PORT = int(os.getenv("APP_PORT", 9006))

if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=PORT, reload=True)