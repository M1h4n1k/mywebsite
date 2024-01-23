from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os
import secrets
from typing import Annotated

security = HTTPBasic()


def get_username(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)]
) -> str:
    current_username_bytes = credentials.username.encode('utf8')
    correct_username_bytes = os.getenv('ADMIN_USERNAME', 'admin').encode('utf8')
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode('utf8')
    correct_password_bytes = os.getenv('ADMIN_PASSWORD', 'admin').encode('utf8')
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=401,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Basic'},
        )
    return current_username_bytes.decode('utf8')
