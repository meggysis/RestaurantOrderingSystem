from pydantic import BaseModel
from typing import Optional

class ResourceResponse(BaseModel):
    id: int
    resource_name: str
    resource_description: Optional[str] = None
    resource_type: str

    class Config:
        orm_mode = True
