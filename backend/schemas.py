from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ExperienceCreate(BaseModel):
    title: str
    company: str
    location: str = ""
    start_date: str
    end_date: str = "Present"
    description: str = ""
    highlights: str = ""


class ExperienceUpdate(BaseModel):
    title: str | None = None
    company: str | None = None
    location: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    description: str | None = None
    highlights: str | None = None


class ExperienceOut(BaseModel):
    id: int
    title: str
    company: str
    location: str
    start_date: str
    end_date: str
    description: str
    highlights: str
    order_index: int

    model_config = {"from_attributes": True}
