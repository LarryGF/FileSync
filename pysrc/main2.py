import eel
from eel import btl
import random
import json
import fs
from fs import open_fs

eel.init('dist')

@eel.expose
def get_route(route: str):
    return return_dir_json(open_fs(route))

@eel.expose
def into_folder(item, route):
    route = fs.path.combine(route, item)
    
    return {'items':return_dir_json(open_fs(route)), 'route':route}


@btl.get('/route')
def getroute():
    btl.request
    print(btl.request.json())

    return return_dir_json(from_route)



def return_dir_json(route):
    content_list = list(route.scandir('/'))
    # directory_list = []
    # files_list  = []
    # for element in content_list:
    #     if element.is_dir:
    #         directory_list.append(element)
    #     else:
    #         files_list.append(element)

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


if __name__ == "__main__":
    eel.start('index.html', options={'port': 8686})
