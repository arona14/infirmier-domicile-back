from pydantic import BaseModel


class NurseBase(BaseModel):
    """
    This class will help you to know the column of
    the table Nurse
    """
    Name: str
    Address: str = None
    Phone: str
    Domain: str = None
    Photo: str = None
    City: str = None
    Email: str = None
    Office: str = None
    availablity: str = None


class NurseUpdate(BaseModel):
    """
    This class will help you to know the column of
    the table Nurse
    """
    Name: str = None
    Address: str = None
    Phone: str = None
    Domain: str = None
    Photo: str = None
    City: str = None
    Email: str = None
    Office: str = None
    availablity: str = None
