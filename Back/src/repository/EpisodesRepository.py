from models.form.EpisodesForm import EpisodesForm
from models.view.EpisodesView import EpisodesView
from settings import CONECTION

connect = CONECTION

async def create_episodes(episodes: EpisodesForm):
    query = "INSERT INTO episodes(episode, name, seasonid, current) VALUES({}, '{}', {}, {})"
    conn = connect
    cur = conn.cursor()
    try:
        sql = query.format(episodes.episode, episodes.name, episodes.seasonId, episodes.current)
        cur.execute(sql)
        conn.commit()
        epis = EpisodesView(id=cur.fetchone[0],
                            episode=episodes.episode,
                            name=episodes.name,
                            seasonId=episodes.seasonId,
                            current=episodes.current)
        return await epis
    except Exception as e:
        print(e)

async def get_all_episodes(seasonId: int):
    episodes = []
    query = "SELECT * FROM episodes WHERE seasonid = {} ORDER BY 1"
    conn = connect
    cur = conn.cursor()
    try:
        sql = query.format(seasonId)
        cur.execute(sql)
        rows = cur.fetchall()
        for data in rows:
            episodes.append(EpisodesView(
                id=data[0],
                episode=data[1],
                name=data[2],
                seasonId=data[3],
                current=data[4]
            ))
        return episodes
    except Exception as e:
        print(e)
    
async def update_current_episode(episodes: EpisodesForm):
    query = "UPDATE episodes SET current = {} WHERE id = {}"
    conn = connect
    cur = conn.cursor()
    try:
        sql = query.format(episodes.current, episodes.id)
        cur.execute(sql)
        conn.commit()
        return EpisodesView(
            id=episodes.id,
            episode=episodes.episode,
            name=episodes.name,
            seasonId=episodes.seasonId,
            current=episodes.current
        )
    except Exception as e:
        print(e)

async def update_episode_name(episodes: EpisodesForm):
    query = "UPDATE episodes SET name = '{}' WHERE id = {}"
    conn = connect
    cur = conn.cursor()
    try:
        sql = query.format(episodes.name, episodes.id)
        cur.execute(sql)
        conn.commit()
        return EpisodesView(
            id=episodes.id,
            episode=episodes.episode,
            name=episodes.name,
            seasonId=episodes.seasonId,
            current=episodes.current
        )
    except Exception as e:
        print(e)