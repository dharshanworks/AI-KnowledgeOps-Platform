from database.connection import engine
from database.base import Base

# Import all models
from models.user import User

Base.metadata.create_all(bind=engine)

print("\nDatabase Tables Created Successfully\n")