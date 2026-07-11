CREATE SCHEMA IF NOT EXISTS rdl;
CREATE SCHEMA IF NOT EXISTS ppl;

CREATE TABLE IF NOT EXISTS rdl.webm_excel (
    id serial4 NOT NULL,
    dt date NOT NULL,
    page_path text,
    query text,
    demand int4,
    impressions int4,
    position float8,
    clicks int4
);

CREATE TABLE IF NOT EXISTS ppl.webmaster_aggregated (
    id serial4 not null,
    dt date not null,
    query text,
    page_path text,
    demand int4,
    impressions int4,
    position float8,
    clicks int4
);

ALTER TABLE ppl.webmaster_aggregated
ADD CONSTRAINT uq_webmaster
UNIQUE (dt, page_path, query, impressions, clicks);

ALTER TABLE rdl.webm_excel
ADD CONSTRAINT uq_webm
UNIQUE (dt, page_path, query, impressions, clicks);