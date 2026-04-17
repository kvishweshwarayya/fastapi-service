from fastapi import FastAPI
import uvicorn
# without routers/__init__.py, we have to import routers as below:
#from routers.user import router as gist_router

# with routers/__ini__.py, we can import routers as package as below:
from routers import gist_router

app = FastAPI()

# Include the router from routers/user.py
app.include_router(gist_router)

def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)

if __name__ == "__main__":
    main()
