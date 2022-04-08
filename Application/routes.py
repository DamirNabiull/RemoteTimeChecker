from aiohttp import web
import logging
import readers
import requests
import os

logging.basicConfig(filename='Logs/app_routes.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

routes = web.RouteTableDef()


@routes.get('/ping')
async def get_ping(request):
    data = {'status': 200}
    return web.json_response(status=200, data=data)


@routes.post('/set')
async def post_timer(request):
    status = 500
    try:
        data = await request.json()

        for i in data:
            if i != 'start' and i != 'end':
                readers.players_d[i] = data[i]
            else:
                readers.time_d[i] = data[i]

        readers.write_time()
        readers.write_players()

        status = 200
    except Exception as e:
        logging.error(f'/set : status - {e}')
    data = {'status': status}
    return web.json_response(status=status, data=data)


@routes.get('/suspendAll')
async def get_ping(request):
    readers.read_players()
    for i in readers.players_d:
        link = f'http://{readers.players_d[i]}:8080/suspend'
        requests.get(link)


@routes.get('/startAll')
async def get_ping(request):
    readers.read_players()
    for i in readers.players_d:
        cmd = f'wakeonlan {i}'
        os.system(cmd)
