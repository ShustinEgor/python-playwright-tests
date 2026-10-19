from pydantic import BaseModel, ConfigDict

class Auth(BaseModel):
    model_config = ConfigDict(extra="forbid")

    accessToken: str
    refreshToken: str
    id: int
    username: str
    email: str
    firstName: str
    lastName: str
    gender: str
    image: str