import json

from ..core.controller import Controller
from .nurse_schema import NurseBase, NurseUpdate
from  ..helper import database

class NurseController(Controller):
    """
    This class contains all the methods needed to work with nurses.
    It inherits from controller where is defined default methods used for creating, fetching, updating
    and deleting elements in the db.
    """

    def __init__(self):
        super().__init__('nurse')

    def get_all(self):
        """
        Get_all is a basic find method with an empty query
        It is just an alias

        :return: a list of dict representing a nurse
        """
        return self.find({})

    def search(self, query: str, min_char_length=2):
        """
        """

        if (len(query) >= min_char_length):
            fields = {}
            val = {'$regex': f".*{query}.*", '$options': 'i'}

            fields['Name'] = val
            fields['Phone'] = val

            params = {"$or": [{k: v} for k, v in fields.items()]}

            return self.find(params)
        else:
            raise HTTPException(
                status_code=HTTP_409_CONFLICT, detail=f"Query must be at least {min_char_length} characters"
            )

    def get_by_id(self, item_id):
        """
        An alias to get a booking by its id

        :param item_id: the id of the booking (pnr)
        :return: a dict representing a booking
        """
        nurse = json.loads(self.find_by_id(item_id))
        return nurse

    def create(self, nurse: NurseBase):
        """
        this creates an nurse
        :param nurse: the nurse to create
        :return: a dict representing the airport
        """
        # if self.find({"AirportCode": airport.AirportCode}):
        #     raise HTTPException(
        #         status_code=HTTP_409_CONFLICT, detail="Provided airport code already exists!"
        #     )

        self.add_one(nurse.dict())

        return json.loads(self.find_one({"Phone": nurse.Phone}))

    def get_by_name(self, name: str):
        """
        Get a nurse by its name.

        :param name: the name of the nurse.
        :return: a dict that represent an nurse.
        """
        return json.loads(self.find_one({"Name": name}))

    def udpate_nurse(self, id, nurse: NurseUpdate):
        """
        Update an element in the collection (nurse)

        :param id: the id of the nurse.
        :param nurse: the new data
        :return: a json representing the new airport after update
        """

        _id = database.to_object_id(id)
        print(_id)
        print(nurse)
        if self.find({"_id": _id}):
            print('yesssss')
            self.edit_one({"_id": _id}, nurse.dict())
            return json.loads(self.find_one({"_id": _id}))

        else:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND, detail="Nurse not found"
            )

    def delete_nurse(self, id):
        """
        Deletes an element in the collection (nurse)
        :param id: the given query
        :return: no content after deleting.
        """

        _id = database.to_object_id(id)
        if self.find({"_id": _id}):

            self.remove_one({"_id": _id})
        else:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND, detail="Nurse not found"
            )
