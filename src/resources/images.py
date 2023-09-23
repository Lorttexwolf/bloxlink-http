import datetime
from io import BytesIO
from typing import Optional

from resources.secrets import IMAGE_SERVER_HOST, IMAGE_SERVER_AUTH  # type: ignore
from resources.utils import fetch, ReturnType


# A resource to access the image server. 
async def fetch_card(avatar_img: str, joined_at: Optional[datetime.datetime] = None, background: Optional[str] = None):
    data, res = await fetch("GET", f"{IMAGE_SERVER_HOST}/card", return_data=ReturnType.BYTES, 
        headers={
            "Authorization": IMAGE_SERVER_AUTH # TODO: Move to fetch util
        }, 
        body={
            "avatar_url": avatar_img,
            "joined_at": joined_at,
            "background": background
    })  # type: ignore

    if res.status != 200:
        raise NotImplementedError()
    
    return  BytesIO(data) # type: ignore
