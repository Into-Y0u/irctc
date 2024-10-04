from fastapi import Depends, APIRouter


train_router = APIRouter(
    prefix='/train',
    tags=['train']
)


@train_router.get("/get")
async def get_train():
    return {"inside train router":"success"}