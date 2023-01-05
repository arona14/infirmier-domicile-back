# import logging

from ..core.config import DATABASE_URL, DATABASE_NAME
from .database import db


async def initialize_app():
    """
    Initialise the db and connects to it.
    Load the airlines as well
    Needs to call this when app starts
    """
    print("Connecting to database...")

    db.init(DATABASE_URL, DATABASE_NAME)

    print("Connected to database")
