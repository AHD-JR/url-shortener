from pydantic import BaseModel
from datetime import datetime

class URLRequest(BaseModel):
    url: str

class URLMapping(BaseModel):
    short_id: str
    long_url: str
    created_at: datetime