from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 1. Serve the main page


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 2. Serve JUST the update (the fragment)


@app.post("/clicked", response_class=HTMLResponse)
async def clicked_button(request: Request):
    # We simulate some logic here
    new_message = "You clicked the button! 🚀"

    # We return a raw HTML string, or a small template fragment
    return f"""
        <p style="color: green; font-weight: bold;">
            {new_message}
        </p>
    """
