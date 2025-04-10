from pydantic import BaseModel, ConfigDict

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str
    created_at: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "아..강의하기 싫다",
                "image": "path/to",
                "description": "아 진짜하기싫다",
                "tags": ["강의, 귀찮음"],
                "location": "서울",
                "created_at": "2025-04-03T15:40:00Z"
            }
        }
    )