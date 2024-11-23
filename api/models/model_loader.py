# api/model_loader.py
from api.models import customers, orders, ratings, payments, menu_items, resources, promotions  # import models
from ..dependencies.database import engine

def index():
    """
    Create all tables in the database for all models dynamically.
    """
    customers.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    ratings.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
