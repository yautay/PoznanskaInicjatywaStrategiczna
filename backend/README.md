
# PiS-API

## Rollout

1) Create virtual Python environment: 
   ```$ virtualenv venv```
2) Activate virtual environment: 
   ```$ source venv/bin/activate```
3) Install dependencies:
   ```$ pip3 install -r requirements.txt```
4) Choose DB: 
   1) SQLite -> ready to go! Nothing to do.
   2) PostgreSQL -> in [session.py](db/session.py):
      1) uncomment 
         ```
         # SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
         # engine = create_engine(SQLALCHEMY_DATABASE_URL)
      2) comment
         ```
         SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
         engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
5) declare environmental variables in [.env](.env) file

## Start development server

```$ uvicorn main:app --reload```

## Unit Tests

```$ pytest``` vanilla pytest  
```$ pytest  --cov="." ``` with pytest-cov coverage analysis  
```$ pytest  --cov="." --cov-report=html``` with pytest-cov coverage analysis and detailed report

## FastAPI docs

Swagger docs -> [http://127.0.0.1:8000/docs#](http://127.0.0.1:8000/docs#)

## Migrations via Alembic

### SQLite - ready to go!

### PostgreSQL

uncomment following lines from [env.py](alembic/env.py)  
```
# from core.config import settings
# config = context.config
# config.set_main_option('sqlalchemy.url', settings.DATABASE_URL)
```

### Build and run migrations

First you must import model Class into [env.py](alembic/env.py), then autogenerate migrations  
``` alembic revision --autogenerate -m "migration_description"```  
to upgrade migration:  
```alembic upgrade head``` or refer to revision id. ```alembic upgrade ae12er34```  
to downgrade migration:  
```alembic upgrade base``` downgrades to <span style="color:red">*nothing*</span> or refer to revision id. ```alembic upgrade ae12er34``` 

## Changelog

### completed

0.1.0 - initial release, architecture  
0.2.0 - JWT implementation, TTD implementation  
0.3.0 - Alembic implementation, Unit Tests, refactor

### in development 

0.4.0 - BGG integration
