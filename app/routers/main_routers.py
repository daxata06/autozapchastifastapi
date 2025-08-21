import os
from fastapi.responses import HTMLResponse
from fastapi import Request
from app.utils.get_items import get_items, get_manufacturer_data
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from typing import Optional

router = APIRouter(prefix="/items")
templates = Jinja2Templates(
    directory=os.path.join(os.path.dirname(__file__), "..", "templates")
)


@router.get("/", response_class=HTMLResponse)
async def search_tems(
    request: Request, query: Optional[str] = None, typed: Optional[str] = None
):
    items = await get_items(query=query, typed=typed)
    context = {
        "request": request,
        "items": items,
        "query": query,
        "typed": typed,
    }
    return templates.TemplateResponse("index.html", context)


@router.get("/getmanufacturer", response_class=HTMLResponse)
async def get_manufacturer(
    request: Request,
    manufacturerid: int,
):
    data = await get_manufacturer_data(manufacturerId=manufacturerid)
    context = {
        "request": request,
        "data": data,
    }
    return templates.TemplateResponse("manufacturerdata.html", context)
