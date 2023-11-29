from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.EpisodesRoutes import episodes
from routes.SeasonRoutes import season
from routes.SeriesRoutes import series
from routes.UserRoutes import user

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

@app.get('/')
def app_get():
    return f'Main'