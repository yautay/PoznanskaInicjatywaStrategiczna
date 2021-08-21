
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
```$ pytest``` vanilla pytest\
```$ pytest  --cov="." ``` with pytest-cov coverage analysis\
```$ pytest  --cov="." --cov-report=html``` with pytest-cov coverage analysis and detailed report
## FastAPI docs
Swagger docs -> [http://127.0.0.1:8000/docs#](http://127.0.0.1:8000/docs#)
## Changelog
### completed
0.1.0 - initial release, architecture\
0.2.0 - JWT implementation, TTD implementation\
### in development 
0.3.0 - DB migrations - TODO