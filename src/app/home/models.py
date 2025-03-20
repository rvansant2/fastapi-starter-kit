from pydantic import BaseModel

class HomeData(BaseModel):
    name: str
    description: str
    version: str


class HomeResponse(BaseModel):
    data: HomeData