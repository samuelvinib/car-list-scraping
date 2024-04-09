from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://user:my-secret-pw@localhost/laravel')
Session = sessionmaker(bind=engine)