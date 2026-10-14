from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

app = FastAPI()

security = HTTPBasic()


@app.get("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):

    username = secrets.compare_digest(
        credentials.username,
        "admin"
    )

    password = secrets.compare_digest(
        credentials.password,
        "admin123"
    )

    if not (username and password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

    return {
        "message": "Login Successful",
        "username": credentials.username
    }