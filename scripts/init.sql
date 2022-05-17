CREATE USER ipa WITH ENCRYPTED PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE iya_service_docker TO ipa;


create table if not exists Users(
    user_id serial NOT NULL PRIMARY KEY,
    nickname text UNIQUE not null,
    email text UNIQUE not null,
    password text
);

create table if not exists Sessions(
    session_hash text NOT NULL PRIMARY KEY,
    user_id integer UNIQUE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

create table if not exist Text(
    text_id serial NOT NULL PRIMARY KEY,
    written_text text,
    user_id integer,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE cascade
)