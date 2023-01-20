from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from fastapi import APIRouter, File

from .nurse_controllers import NurseController
from .nurse_schema import NurseBase, NurseUpdate
from ..helper import database


router = APIRouter()
controller = NurseController()


@router.get("/")
async def get_nurses(name: str = None, query: str = ''):
    """
    This route gets  the nurse with the provide name
    :param name: the name column on the table nurses
    :return a json representing the nurse
    """
    if name:
        return [controller.get_by_name(name)]

    if query:
        return controller.search(query)

    return controller.get_all()


@router.get("/{nurse_id}")
async def get_nurse(nurse_id: str):
    """
    This route gets one booking by its id

    :param nurse_id: the nurse id
    :return: json representing a nurse
    """
    return controller.get_by_id(nurse_id)


@router.post("/", status_code=HTTP_201_CREATED)
async def add_nurse(nurse: NurseBase):
    """
    This route  is used to create a new nurse
    in the database
    :param nurse: the nurse schema
    :return: dict of nurse
    """
    return controller.create(nurse)


@router.put("/{nurse_id}")
async def update_nurse(nurse_id: str, nurse: NurseUpdate):
    """
    This updates an nurse

    :param nurse_id: the id of the nurse to update
    :param nurse: the new data
    :return: a json representing the new nurse after update
    """
    print('nurse....', nurse)
    return controller.udpate_nurse(nurse_id, nurse)


@router.delete("/{nurse_id}", status_code=HTTP_204_NO_CONTENT)
async def remove_nurse(nurse_id: str):
    """
    This route help you to delete an nurse

    :param nurse_id: the id of the nurse to delete
    :return: status 204 or raise un exception (if not found)
    """
    return controller.delete_nurse(nurse_id)


@router.post("/{nurse_id}/photo/")
async def create_nurse_with_photo(nurse_id: str, photo: bytes = File(...)):
    """
    This router upload nurse photo
    :param nurse_id: the given nurse
    :photo: the photo file
    :return a dict has this format
    {
        "id": "nurse.id",
        "name": "nurse.name",
        "photo": "nurse photo"
    }
    """
    _id = database.to_object_id(nurse_id)
    url = controller.upload_photo(photo=photo, id=_id)
    # logging.info("Customer Logo " + str(url['logo_url']) + "successfully updated")
    return url
