from fastapi import APIRouter, Depends, UploadFile
from .utils import get_username
from uuid import uuid4

router = APIRouter(prefix='')


# should be done with nginx
@router.post('/upload', response_description='Upload image', response_model=str, status_code=201)
async def upload_file(file: UploadFile, username: str = Depends(get_username)):
    place = uuid4().hex + '.' + file.filename.split('.')[-1]
    with open(f'./uploads/{place}', 'wb') as f:
        f.write(file.file.read())
    return '/uploads/' + place
