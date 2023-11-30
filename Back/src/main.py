from fastapi import BackgroundTasks, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.EpisodesRoutes import episodes
from src.routes.SeasonRoutes import season
from src.routes.SeriesRoutes import series
from src.routes.UserRoutes import user
from src.mensageria.reciever import receiver
import time

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(episodes)
app.include_router(season)
app.include_router(series)
app.include_router(user)

def backgroun_task():
    while True:
        receiver()
        time.sleep(1)


@app.get('/')
def app_get(background_tasks: BackgroundTasks):
    background_tasks.add_task(background_task)
    return f'Main'