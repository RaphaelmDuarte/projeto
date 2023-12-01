from fastapi import APIRouter, Request
from models.form.SeriesForm import SeriesForm
from services.SeriesService import getAllSeries, createSeries

import logging 
from logging.config import dictConfig
from ..log_config import log_config

series = APIRouter(
    prefix='/series',
    tags=['series']
)

dictConfig(log_config)
logger = logging.getLogger('foo-logger')

@series.post('/')
async def series_create(seriesForm: SeriesForm, request: Request):
    logger.info("Requisição de criação de série!")
    token: str = await get_token(request)
    return await createSeries(seriesForm, token)

@series.get('/')
async def series_get_all(request: Request):
    token: str = await get_token(request)
    return await getAllSeries(token)

async def get_token(request: Request):
    token: str = request.headers.get('Authorization')
    return token