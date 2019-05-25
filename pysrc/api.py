from fastapi import Cookie, FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import json
import fs
from fs import open_fs
try:
	from fssync.dsync import *
except ImportError:
	from .fssync.dsync import *

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])

matcher = {
    'seriePersona':PSERIE,
    'anime':ANIME,
    'pelicula':MOVIE
}

class Route(BaseModel):
    name: str

class RouteItem(BaseModel):
    item: str
    route: str

class RouteType(BaseModel):
    route: str
    type: str

class MoveType(BaseModel):
    source: str
    destination: str
    type: str


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/get_route/")
async def get_route(route: Route):
    return return_dir_json(open_fs(route.name))

@app.post('/into_folder/')
async def into_folder(item: RouteItem):
    route = fs.path.combine(item.route, item.item)

    return {'items':return_dir_json(open_fs(route)), 'route':route}

@app.post('/organize/')
async def organize_path(info: RouteType):
    try:
        # fs_source = open_fs(info.item)
        # fs_destination = open_fs(info.route)
        # series = SeriesPerson(fs_source, fs_destination)
        # series = series.organize()
        # series.sync()

        print(info)
        await organize(info.route,matcher[info.type])
        return True
    except Exception as e:
        return e

@app.post('/move/')
async def move(info: MoveType):

    print(info)
    sync(info.source, info.destination, matcher[info.type])
    return True

def return_dir_json(route):
    content_list = list(route.scandir('/'))
    return [
        {   'id': element.name,
            'name': element.name,
            'children': []
        } for element in content_list if element.is_dir
        #  else {
        #     'name': element.name
        # }
    ] + [{
        'id':element.name,
        'name': element.name,
    } for element in content_list if not element.is_dir]