from typing import Annotated, Optional
from pydantic import BaseModel, Field, BeforeValidator, ConfigDict

PyObjectId = Annotated[str, BeforeValidator(str)]


class ProjectModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    img: str = Field(...)
    title: str = Field(...)
    subtitle: str = Field(...)
    description: str = Field(...)
    button: dict[str, str] = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                'img': "https://picsum.photos/seed/1/300/300",
                'title': "Some name",
                'subtitle': "Some subtitle",
                'description':
                    "In tempor pulvinar sollicitudin. In hac habitasse platea dictumst. " +
                    "In non aliquam nulla. Cras arcu tellus, lobortis condimentum justo id," +
                    " posuere finibus nibh. Mauris quis justo ligula. Praesent sit amet urna" +
                    " sed lacus gravida pretium. Fusce ac mi non nulla faucibus tempus a ac ex." +
                    " Vestibulum lacinia, risus vitae interdum commodo, metus neque posuere nisl," +
                    " maximus condimentum metus risus id felis. ",
                'button': {
                    'text': "Read more",
                    'link': "https://goo.gle",
                },
            }
        },
    )
