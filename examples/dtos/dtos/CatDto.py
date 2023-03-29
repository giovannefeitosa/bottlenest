import pydantic


class CatDto(pydantic.BaseModel):
    name: str
    age: int

    def __init__(self, body):
        super().__init__(**body)
