from models.form.SeriesForm import SeriesForm
from models.view.SeriesView import SeriesView
from settings import CONECTION

connect = CONECTION

async def get_all_series(userId: int):
    series = []
    query = 'SELECT * FROM series WHERE userid = {} ORDER BY name'
    conn = connect
    cur = conn.cursor()
    try:
        sql = query.format(userId)
        cur.execute(sql)
        rows = cur.fetchall()
        for data in rows:
            series.append(SeriesView(
                id=data[0],
                name=data[1]
            ))
        return series
    except Exception as e:
        print(e)
    
async def create_series(series: SeriesForm, userId: int):
    query = "INSERT INTO series (name, userId) VALUES('{}', {}) RETURNING id;"
    conn = connect
    cur = conn.cursor()
    try:
        sql = query.format(series.name, userId)
        cur.execute(sql)
        serieId = cur.fetchone()[0]
        serie = SeriesView(
            id=serieId,
            name=series.name
        )
        conn.commit()
        return serie
    except Exception as e:
        print(e)