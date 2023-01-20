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

    @staticmethod
    def aggregate(collection: str, query):
        """
        Uses pymongo aggregate method.

        :param collection: collection (table) to work with
        :param query: the query to aggregate
        :return: a list of elements from the db that meet the conditions specified in the query
        """
        return DB.DATABASE[collection].aggregate(query)

    @staticmethod
    def insert(collection: str, data):
        """
        Inserts one document in the collection.

        :param collection: the collection (table) to work with
        :param data: the element to insert
        :return a pymongo status of the insertion.
        """
        return DB.DATABASE[collection].insert_one(data)

    @staticmethod
    def insert_many(collection: str, data):
        """
        Inserts many documents in the collection.

        :param collection:
        :param data: the collection (table) to work with
        :return: a pymongo status of the insertion. It contains the number of inserted elements
        """
        return DB.DATABASE[collection].insert_many(data)

    @staticmethod
    def find_one(collection: str, query):
        """
        Gets one document in the collection that meets the condition specified in the query.

        :param collection: the name of the collection (table) to work with
        :param query: the query to run.
        :return: the founded item
        """
        item = DB.DATABASE[collection].find_one(query)
        return item

    @staticmethod
    def find(collection: str, query):
        """
        Finds documents in the collection with the given query.

        :param collection:  the name of the collection (table) to work with
        :param query: the query to run.
        :return: a list of founded elements.
        """
        return DB.DATABASE[collection].find(query)

    @staticmethod
    def update_one(collection: str, query, data):
        """
        Edits one document in the collection that meets the condition specified in the query.

        :param collection: the name of the collection (table) to work with
        :param query: the query to run.
        :param data: the data to update
        """
        return DB.DATABASE[collection].update_one(query, {
            "$set": data
        })

    @staticmethod
    def update_one_or_insert(collection: str, query, data):
        """
        Edits one document in the collection that meets the condition specified in the query.

        :param collection: the name of the collection (table) to work with
        :param query: the query to run.
        :param data: the data to update
        """
        return DB.DATABASE[collection].update_one(query, {
            "$set": data
        }, upsert=True)

    @staticmethod
    def update_many(collection: str, query, data):
        """
        Edits many documents in the collection with the given query.

        :param collection: the name of the collection (table) to work with
        :param query: the query to run
        :param data: the data to update
        :return: a pymongo status with the number of updated elements.
        """
        return DB.DATABASE[collection].update_many(query, {
            "$set": data
        })

    @staticmethod
    def delete_many(collection: str, query):
        """
        Removes many documents in the collection with the given query.

        :param collection: the name of the collection (table) to work with
        :param query: the query to run
        :return: a pymongo status with the number of removed documents
        """
        return DB.DATABASE[collection].delete_many(query)

    @staticmethod
    def delete_one(collection: str, query):
        """
        Removes one document in the collection that meets the condition specified in the query.

        :param collection: the name of the collection (table) to work with
        :param query: the query to run
        :return: a pymongo status
        """
        return DB.DATABASE[collection].delete_one(query)


db = DB()
