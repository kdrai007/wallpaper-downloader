from typing import Union

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    in_offer: Union[bool, None] = None


# We use APIRouter instead of FastAPI() here
router = APIRouter()

# Point to the templates folder
# Note: We use "app/templates" because the code is run from the root folder
templates = Jinja2Templates(directory="my_app/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"name": item.name, "item_id": item_id}
