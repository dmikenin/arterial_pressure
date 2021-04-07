# Arterial pressure

## Description
Backend for opensource app Arterial Pressure. App help people 
to observe them pressure.

### Technical stack
- Language: Python
- Framework: FastApi
- DB: PostgreSQL
- ORM: SQLAlchemy
- Manage migration: Alembic
- Tests: PyTest
- Documentation: Swagger/Redoc


### Local develop
- git pull repo
- activate venv
- ```pip3 install -r requirements.txt```
- create alembic.ini 
- ```docker-compose -f docker-compose.dev.yml```
- ```alembic upgrade```
- ```python main.py```

### Next step
1. Method for show statistics user
2. Method for send push-notification, that user not forgotten add today data 


## Author
**Denis Mikenin** - *Backend developer* -
    [my web-site](http://mikenin.com)

