from datetime import datetime

from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    original_url: HttpUrl


class URLOut(BaseModel):
    short_code: str
    original_url: HttpUrl
    click_count: int
    created_at: datetime

    class Config:
        from_attributes = True