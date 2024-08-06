from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from model import URLRequest
from service import UrlShortnerService
from in_memory_storage import Inmemory_storage

app = FastAPI()

# Dependency Injection
repo = Inmemory_storage()
service = UrlShortnerService(repo)

@app.post('/shorten')
async def shorten_url(req: URLRequest):
    url_dict = req.dict()
    short_id = await service.shorten_url(url_dict['url'])
    return {
        "status_code": 200,
        "short_url": f"http://localhost:8000/{short_id}"
    }


@app.get("/{short_id}")
async def redirect(short_id: str):
    long_url = await service.get_long_url(short_id)
    if long_url is None:
        raise HTTPException(status_code=404, detail="URL not found!")
    
    return RedirectResponse(url=long_url)