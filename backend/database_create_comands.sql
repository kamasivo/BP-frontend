-- Database: db

-- DROP DATABASE db;

CREATE DATABASE db
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Table: public.devices

-- DROP TABLE public.devices;

CREATE TABLE public.devices
(
    ip_address text COLLATE pg_catalog."default",
    os text COLLATE pg_catalog."default",
    name text COLLATE pg_catalog."default",
    vendor text COLLATE pg_catalog."default",
    num_of_vulns bigint,
    od_family text COLLATE pg_catalog."default",
    os_gen text COLLATE pg_catalog."default",
    open_ports bigint
)

TABLESPACE pg_default;

ALTER TABLE public.devices
    OWNER to postgres;

ALTER TABLE public.devices
    ADD COLUMN ip_address text COLLATE pg_catalog."default";

ALTER TABLE public.devices
    ADD COLUMN os text COLLATE pg_catalog."default";


ALTER TABLE public.devices
    ADD COLUMN name text COLLATE pg_catalog."default";

ALTER TABLE public.devices
    ADD COLUMN vendor text COLLATE pg_catalog."default";

ALTER TABLE public.devices
    ADD COLUMN num_of_vulns bigint;


ALTER TABLE public.devices
    ADD COLUMN od_family text COLLATE pg_catalog."default";


ALTER TABLE public.devices
    ADD COLUMN os_gen text COLLATE pg_catalog."default";

ALTER TABLE public.devices
    ADD COLUMN open_ports bigint;



CREATE TABLE public.ports
(
    ip_address "char"[],
    port_number bigint
)