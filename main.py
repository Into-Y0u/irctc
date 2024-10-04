from typing import Union
import prop_file
from fastapi import FastAPI
from app_pack.train.train_routes import train_router
from app_pack.train.train_db.database import TrainBase, train_db_engine


app = FastAPI(title=prop_file.TITLE, summary=prop_file.SUMMARY, version=prop_file.VERSION)

app.include_router(train_router)


TrainBase.metadata.create_all(bind=train_db_engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}