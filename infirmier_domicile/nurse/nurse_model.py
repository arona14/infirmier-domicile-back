from pydantic import BaseModel


class Nurse(BaseModel):
    name: str = None
    address: str = None
    phone: str = None
    domain: str = None
    photo: str = None
    city: str = None
    email: str = None
    office: str = None
    availablity: str = None
