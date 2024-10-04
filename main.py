from typing import Union
import prop_file
from fastapi import FastAPI



app = FastAPI(title=prop_file.TITLE, summary=prop_file.SUMMARY, version=prop_file.VERSION)

# app.include_router(public_router)
# app.include_router(user_router)
# app.include_router(order_router)
# app.include_router(service_router)
# app.include_router(auth_router)



@app.get("/")
def read_root():
    return {"Hello": "World"}