from fastapi import APIRouter, Request
from src.models.form.SeriesForm import SeriesForm
from src.services.SeriesService import getAllSeries, createSeries

series = APIRouter(
    prefix='/series',
    tags=['series']
)

@series.post('/')
async def series_create(seriesForm: SeriesForm, request: Request):
    token: str = await get_token(request)
    print(seriesForm)
    return await createSeries(seriesForm, token)

@series.get('/')
async def series_get_all(request: Request):
    token: str = await get_token(request)
    return await getAllSeries(token)

async def get_token(request: Request):
    token: str = request.headers.get('Authorization')
    return token