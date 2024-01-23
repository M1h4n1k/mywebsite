from bson import ObjectId
from fastapi import HTTPException, APIRouter, Body
from models.post import PostModel
from database import posts

router = APIRouter(prefix='/posts')


@router.get("/", response_description="List all posts", response_model=list[PostModel])
async def get_posts():
    return await posts.find().to_list(1000)


@router.get("/{post_id}", response_description="Get a single post", response_model=PostModel)
async def get_post(post_id: str):
    post = await posts.find_one({"_id": ObjectId(post_id)})
    if post:
        return post
    raise HTTPException(404, f"Post with id {post_id} not found")


@router.post("/", response_description="Add new post", response_model=PostModel, status_code=201)
async def create_post(post: PostModel = Body(...)):
    new_post = await posts.insert_one(post.model_dump(exclude={'id'}))
    created_post = await posts.find_one({"_id": new_post.inserted_id})
    return created_post
