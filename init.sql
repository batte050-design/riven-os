-- Title: Init riven Database

-- Fetch the docker secrets, if they are available.
-- Otherwise fall back to environment variables, or hardwired 'riven'
\set db_user `([ -r /var/run/secrets/riven-user ] && cat /var/run/secrets/riven-user) || echo "${POSTGRES_USER:-riven}"`
\set db_password `([ -r /var/run/secrets/riven-password ] && cat /var/run/secrets/riven-password) || echo "${POSTGRES_PASSWORD:-riven}"`
\set db_name `([ -r /var/run/secrets/riven-db ] && cat /var/run/secrets/riven-db) || echo "${POSTGRES_DB:-riven}"`

-- CREATE USER :"db_user"
--     WITH PASSWORD :'db_password'
--     NOCREATEDB
--     NOCREATEROLE
--     ;
--
-- CREATE DATABASE :"db_name"
--     WITH
--     OWNER = :"db_user"
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'en_US.utf8'
--     LC_CTYPE = 'en_US.utf8'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;

-- Set up our schema and extensions in our new database.
\c :"db_name"

CREATE SCHEMA :"db_name"
    AUTHORIZATION :"db_user";

ALTER DATABASE :"db_name"
    SET search_path TO :"db_name";

CREATE EXTENSION IF NOT EXISTS vector WITH SCHEMA :"db_name";

DROP SCHEMA IF EXISTS public CASCADE;
