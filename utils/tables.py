from loguru import logger

from db import db

async def create_tables():
    users = """create table if not exists users(
        id serial primary key,
        full_name varchar(255) not null,
        tlg_user_id bigint not null unique,
        phone varchar(50) not null unique
    );"""
    cars = """create table if not exists cars(
        id serial primary key,
        name varchar(255) not null
    );"""
    drivers = """create table if not exists driver(
        id serial primary key,
        user_id int references users(id),
        car_id int references cars(id),
        car_number varchar(15),
        status varchar(50)
    );"""

    await db.execute_multiple(users, cars, drivers)
    logger.info('ℹ tables successfully created')

async def create_user(data):
    query = """insert into users(full_name, tlg_user_id, phone) values ($1,$2,$3)"""
    await db.pool.execute(query, data)