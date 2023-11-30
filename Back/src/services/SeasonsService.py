from src.repository.SeasonRepository import get_all_seasons

async def getAllSeasons(serieId: int):
    return await get_all_seasons(serieId)