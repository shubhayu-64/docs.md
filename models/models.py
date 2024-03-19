from datetime import datetime
from typing import List, Optional
from uuid import uuid4
from pydantic import BaseModel, Field

# 00000000-0000-0000-0000-000000000000

class DocsModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    createdBy: str = Field(default="00000000-0000-0000-0000-000000000000", alias="createdBy")
    createdAt: datetime = Field(default_factory=datetime.now, alias="createdAt")
    name: str = Field(..., alias="title", min_length=1)
    type: str = Field(default="docs", alias="type")
    html: Optional[str] = Field(None, alias="html")
    css: Optional[str] = Field(None, alias="css")
    body: Optional[str] = Field(None, alias="description")
    slug: str = Field(..., alias="slug", min_length=1)
    tags: Optional[List[str]] = Field(None, alias="tags")