from models.form.EpisodesForm import EpisodesForm
from repository.EpisodesRepository import create_episodes, get_all_episodes, update_current_episode, update_episode_name

async def createEpisodes(episodes: EpisodesForm):
    return await create_episodes(episodes)

async def getAllEpisodes(seasonId: int):
    return await get_all_episodes(seasonId)

async def updateCurrentEpisode(episodes: EpisodesForm):
    return await update_current_episode(episodes)

async def updateEpisodeName(episodes: EpisodesForm):
    return await update_episode_name(episodes)