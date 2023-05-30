from db import db

async def create_tables():
    clients = """create table if not exists client(
        id serial primary key,
        full_name varchar(255) not null,
        user_id bigint not null unique,
        phone varchar(50) not null unique
    );"""
    cars = """create table if not exists cars(
        id serial primary key,
        name varchar(255) not null
    );"""
    drivers = """create table if not exists driver(
        LIKE client including constraints,
        car_id int references cars(id),
        car_number varchar(15),
        status varchar(50)
    );"""

    await db.execute_multiple(clients, cars, drivers)