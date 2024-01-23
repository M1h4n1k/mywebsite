from fastapi import Request, APIRouter, Depends
from models.project import ProjectModel
from database import projects
from .utils import get_username

router = APIRouter(prefix='/projects')


@router.get('/', response_description='List all projects', response_model=list[ProjectModel])
async def get_projects():
    return await projects.find().to_list(1000)


@router.post('/', response_description='Add new project', response_model=ProjectModel, status_code=201)
async def create_project(project: ProjectModel, username: str = Depends(get_username)):
    new_project = await projects.insert_one(project.model_dump(exclude={'id'}))
    created_project = await projects.find_one({'_id': new_project.inserted_id})
    return created_project
