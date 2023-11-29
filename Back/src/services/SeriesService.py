from models.form.EpisodesForm import EpisodesForm
from models.form.SeasonForm import SeasonForm
from models.form.SeriesForm import SeriesForm
from models.view.SeasonView import SeasonView
from models.view.SeriesView import SeriesView
from repository.EpisodesRepository import create_episodes
from repository.SeriesRepository import get_all_series, create_series
from repository.SeasonRepository import create_season
from services.TokenService import get_userId

async def getAllSeries(token: str):
    userId: int = await get_userId(token)
    return await get_all_series(userId)

async def createSeries(seriesForm: SeriesForm, token: str):
    userid: int = await get_userId(token)
    savedSeries: SeriesView = await create_series(seriesForm, userid)
    for season in seriesForm.seasons:
        seasonForm = SeasonForm(
            season=season.season,
            seriesId=savedSeries.id,
            current=False
        )
        savedSeason: SeasonView = await create_season(seasonForm)
        for i in range(season.episodes):
            episodesForm = EpisodesForm(
                episode=i+1,
                name='S'+str(season.season)+'E'+str(i+1),
                seasonId= savedSeason.id,
                current=False
            )
            print(episodesForm)
            await create_episodes(episodesForm)
    return SeriesView(
        id=savedSeries.id,
        name=savedSeries.name
    )
    