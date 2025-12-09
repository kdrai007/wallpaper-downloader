from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# We use APIRouter instead of FastAPI() here
router = APIRouter()

# Point to the templates folder
# Note: We use "app/templates" because the code is run from the root folder
templates = Jinja2Templates(directory="my_app/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
