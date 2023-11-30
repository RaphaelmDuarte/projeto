from src.models.form.EpisodesForm import EpisodesForm
from src.repository.EpisodesRepository import create_episodes, get_all_episodes, update_current_episode, update_episode_name

import logging 
from logging.config import dictConfig
from log_config import log_config

dictConfig(log_config)
logger = logging.getLogger('foo-logger')

async def createEpisodes(episodes: EpisodesForm):
    return await create_episodes(episodes)

async def getAllEpisodes(seasonId: int):
    return await get_all_episodes(seasonId)

async def updateCurrentEpisode(episodes: EpisodesForm):
    return await update_current_episode(episodes)

async def updateEpisodeName(episodes: EpisodesForm):
    try:
        return await update_episode_name(episodes)
    except Exception as e:
        print(e)