from fastapi import APIRouter
from services.SeasonsService import getAllSeasons

season = APIRouter(
    prefix='/season',
    tags=['season']
)

@season.get('/{serieId}')
async def season_all_get(serieId: int):
    return await getAllSeasons(serieId)