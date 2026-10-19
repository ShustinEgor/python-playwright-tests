from pydantic import BaseModel, ConfigDict

class ErrorBodyResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    message: str




