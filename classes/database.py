from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgres://sneakersdb_user:2bmkHH8Oh3VRMFzKUuGGhNZwftEbjf5K@dpg-cijtd4tgkuvjvn7i47mg-a.frankfurt-postgres.render.com/sneakersdb'

# equivalent à un "connect"
database_engine = create_engine(DATABASE_URL)
# equivalent à un "cursor"
SessionTemplate = sessionmaker(
    bind=database_engine, autocommit=False, autoflush=False)

# get_cursor is used by almost all endpoint in order to connect to the database
def get_cursor():
    db = SessionTemplate()
    try:
        yield db # yield est une operation python qui permet de récupérer quelques chose qui peut ne pas exister 
    finally:
        db.close()
