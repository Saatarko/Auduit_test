import os

import PySide6
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



basedir = os.path.abspath(os.path.dirname(PySide6.__file__))
plugin_path =  os.path.join(basedir, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

DATABASE_URL = "sqlite+pysqlite:///base.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


