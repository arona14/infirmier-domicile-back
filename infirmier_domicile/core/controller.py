# This file contains the basic controller class


import json

import bson
from fastapi import HTTPException
from .utils import MJSONEncoder
from ..data.database import DB
from ..helper.database import to_object_id


class Controller:
    """
    Basic controller class. It provides methods that helps to deal with CRUD in the db.
    Uses pymongo default methods
    """

    def __init__(self, collection: str):
        """
        Needs a collection (table) name to work with

        :param collection: name of the collection
        """
        self.collection = collection

    def aggregate(self, query):
        """
        Aggregate method which help make more advanced queries

        :param query: the given query
        :return: usually a list of elements in the db.
        """
        return DB.aggregate(self.collection, query)

    def find_one(self, query):

        result = DB.find_one(self.collection, query)
        # bson objectId can't directly parsed to json. Need to encode it.
        return MJSONEncoder().encode(result)

    def find(self, query):
        """
        A simple find method.
        :param query: the given query
        :return: a list of objects
        """

        # Needs to encode the object cause the bson property ObjectId can't be directly transform to json.
        return [json.loads(MJSONEncoder().encode(element)) for element in DB.find(self.collection, query)]

    def find_by_id(self, _id):
        """
        Uses find_one method with the query that contains the id of the element.

        :param _id: the str id of the element to fetch
        :return: a dict representing the element to fetch
        """
        try:
            # transforms the str id to bson ObjectId
            item_id = to_object_id(_id)
        except bson.errors.InvalidId:
            raise HTTPException(status_code=422, detail="Id invalid")

        result = DB.find_one(self.collection, {"_id": item_id})
        # bson objectId can't directly parsed to json. Need to encode it.
        return MJSONEncoder().encode(result)

    def edit_one(self, query, data):
        """
        edit an element in the collection.

        :param query: the new data
        """
        return DB.update_one(self.collection, query, data)

    def edit_many(self, query, data):
        """
        edit many elements which match the query in the collection.

        :param query: the new data
        :param data:
        """
        return DB.update_many(self.collection, query, data)

    def edit_one_by_id(self, item_id, data):
        try:
            # transforms the str id to bson ObjectId
            item_id = to_object_id(item_id)
        except bson.errors.InvalidId:
            raise HTTPException(status_code=422, detail="Id invalid")

        return self.edit_one({"_id": item_id}, data)

    def remove_one(self, query):
        """
        Deletes an element in the collection.

        :param query: the given query
        """
        return DB.delete_one(self.collection, query)

    def remove_many(self, query):
        """
        Deletes many elements that meets the condition specified in the query

        :param query: the given query
        :return: a dict that contains the number of deleted elements.
        """
        return DB.delete_many(self.collection, query)

    def add_one(self, item):
        return DB.insert(self.collection, item)

    def upsert_one(self, query, data):
        return DB.update_one_or_insert(self.collection, query, data)

    def created_index(self, condition, name, isUnique=False):
        DB.created_index(self.collection, condition=condition, isUnique=isUnique, name=name)
