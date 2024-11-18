from uuid import UUID
from pydantic import BaseModel

    
class CreateHistoryScrapeRequestDto(BaseModel):
    keyword : str
    num_groups: int
    num_posts : int
    num_comments: int

class UpdateHistoryScrapeRequestDto(BaseModel):
    keyword: str
    num_groups: int
    num_posts: int
    num_comments: int
