import pymongo


class DB(object):
    """
    This class is a singleton. It uses a single instance of mongoclient.
    All methods are static but need to init the class in beginning of the app.
    """

    DATABASE = None

    @staticmethod
    def init(uri: str, name: str):
        """
        Initialize the db with the given parameters.

        :param uri: URI of the db
        :param name: The name of the database
        """
        client = pymongo.MongoClient(uri)
        DB.DATABASE = client[name]

db = DB()
