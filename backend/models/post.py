from typing import Annotated, Optional
from pydantic import BaseModel, Field, BeforeValidator, ConfigDict

PyObjectId = Annotated[str, BeforeValidator(str)]


class PostModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    img: str = Field(...)
    title: str = Field(...)
    caption: str = Field(...)
    blocks: list[dict[str, str | list]] = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "img": "https://picsum.photos/seed/1/300/300",
                "title": "Lorem Ipsum",
                "caption": "Some short description of the post",
                "blocks": [
                    {
                        "title": "Introduction",
                        "text": [
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                            "Sed non risus. Suspendisse lectus tortor, dignissim sit amet, "
                            "adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. "
                        ]
                    },
                ]
            }
        },
    )
