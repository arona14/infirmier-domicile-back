import bson
from starlette.exceptions import HTTPException


def to_object_id(given_id):
    """
    Transforms a str id to an bson ObjectId

    :param given_id: the id in str
    :return: an bson ObjectId
    """
    if given_id is not None:
        if not isinstance(given_id, bson.ObjectId):
            try:
                return bson.ObjectId(given_id)
            except bson.errors.InvalidId:
                raise HTTPException(
                    status_code=422, detail="Invalid ObjectId"
                )
        else:
            return given_id
    else:
        return None
