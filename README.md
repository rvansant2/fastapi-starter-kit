# fastapi-starter-kit

A FastAPI starter kit including:
- [SQLAlchemy](https://www.sqlalchemy.org/) (Object Relational Mapper)
- [Pydantic](https://docs.pydantic.dev/latest/) (Validations)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) (Data migrations)
- [psycopg2-binary](https://www.psycopg.org/docs/install.html) (Postgres connection)

## Requirements
- Python version ^3.12
- Docker

## Get started
- Clone [repo](https://github.com/rvansant2/fastapi-starter-kit/tree/master).
- Change into directory `fastapi-starter-kit`.
- Copy `.env.example` as `.env` and replace the definitions for `FILL_ME_IN`.
- Run command `docker compose up --build`
- Visit [home](http://localhost:8000/) to verify you see the default data.
- Visit (Swagger documentation](http://localhost:8000/docs) to view current defined endpoints

## Useful development tools
- [Postman](https://www.postman.com/downloads/)
- [DBeaver](https://dbeaver.io/download/)


