import pydantic


class CatDto(pydantic.BaseModel):
    name: str
    age: int
