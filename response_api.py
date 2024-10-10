from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

app = FastAPI()
router = APIRouter()

class Item(BaseModel):
    formResponses: list

@router.get("/tester")
def read_root():
    return{"message": "Hello, FastApi!"}

@router.post("/responses/")
async def read_items(item: Item):
    return {"receivedData": item.formResponses}

app.include_router(router, prefix="/clientResponseApiHandler/api/v1")

