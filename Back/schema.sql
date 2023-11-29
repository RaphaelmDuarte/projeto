CREATE TABLE IF NOT EXISTS appuser(
id bigserial PRIMARY KEY,
name varchar(250) NOT NULL,
email varchar(300) NOT NULL,
password varchar(400) NOT NULL,
    Constraint uk_email UNIQUE (email)
);

CREATE TABLE IF NOT EXISTS series(
id bigserial PRIMARY KEY,
name varchar(250) NOT NULL,
userId bigint,
    Constraint fk_userid FOREIGN KEY (userId) references appuser(id)
);

CREATE TABLE IF NOT EXISTS season(
id bigserial PRIMARY KEY,
season bigint NOT NULL,
seriesId bigint,
current Boolean NOT NULL,
    Constraint fk_seriesId FOREIGN KEY (seriesId) references series(id)
);

CREATE TABLE IF NOT EXISTS episodes(
id bigserial PRIMARY KEY,
episode bigint NOT NULL,
name varchar(250),
seasonId bigint,
current Boolean NOT NULL,
    COnstraint fk_seasonId FOREIGN KEY (seasonId) references season(id)
);