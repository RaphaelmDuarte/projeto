from fastapi import APIRouter
from models.form.EpisodesForm import EpisodesForm
from services.EpisodesService import createEpisodes, getAllEpisodes, updateCurrentEpisode, updateEpisodeName

episodes = APIRouter(
    prefix='/episodes',
    tags=['episodes']
)

@episodes.post('/')
async def create(episodes: EpisodesForm):
    return createEpisodes(episodes)

@episodes.get('/{seasonId}')
async def get_all_episodes(seasonId: int):
    return await getAllEpisodes(seasonId)

@episodes.put('/name')
async def update_episode_name(episodes: EpisodesForm):
    return await updateEpisodeName(episodes)

@episodes.put('/current')
async def update_curret_episode(episodes: EpisodesForm):
    return await updateCurrentEpisode(episodes)