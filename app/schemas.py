from pydantic import BaseModel,ConfigDict,Field


class PostBase(BaseModel):
    meal: str = Field(min_length=1,max_length=100)
    area: str = Field(min_length=1)
    instructions: str = Field(min_length=1,max_length=50)
    ingrenients: str = Field(min_length=1,max_length=100)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted:str

