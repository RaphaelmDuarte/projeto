from models.form.SeasonForm import SeasonForm
from models.view.SeasonView import SeasonView
from settings import CONECTION

connect = CONECTION

async def create_season(season: SeasonForm):
    query = "INSERT INTO season(season, seriesid, current) VALUES({}, {}, {}) RETURNING id;"
    conn = connect
    cur = conn.cursor()
    try:
        sql = query.format(season.season, season.seriesId, season.current)
        cur.execute(sql)
        seasonId = cur.fetchone()[0]
        conn.commit()
        return SeasonView(
            id=seasonId,
            season=season.season,
            seriesId=season.seriesId,
            current=season.current
        )
    except Exception as e:
        print(e)

async def get_all_seasons(serieId: int):
    seasons = []
    query = "SELECT * FROM season WHERE seriesId = {} ORDER BY 1"
    conn = connect
    cur = conn.cursor()
    try:
        sql = query.format(serieId)
        cur.execute(sql)
        rows = cur.fetchall()
        for data in rows:
            seasons.append(SeasonView(
                id=data[0],
                season=data[1],
                seriesId=data[2],
                current=data[3]
            ))
        return seasons
    except Exception as e:
        print(e)