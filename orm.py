from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# ------------------------------------
# Conexión mysql
# ------------------------------------
#sqlite "sqlite:///personas.db"
DATABASE_URL = (
    "mysql+mysqldb://new:new@localhost/housing_api"
)
engine = create_engine(
    DATABASE_URL,
    echo=True
)

# ------------------------------------
# Clase base para modelos
# ------------------------------------

Base = declarative_base()

