from fastapi import FastAPI, Request, status
from starlette.staticfiles import StaticFiles
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()
Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="TestTodoApp/templates")

app.mount("/static", StaticFiles(directory="TestTodoApp/static"), name="static")

@app.get("/healthy")
def healthy_check():
    return {"status": "healthy"}

@app.get('/')
def test(request: Request):
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)

@app.get("/")
def test(request: Request):
    return templates.TemplateResponse("home.html", context={"request": request})


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
