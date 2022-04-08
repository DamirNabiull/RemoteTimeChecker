import _thread
from aiohttp import web
from alarm import alarm_clock


if __name__ == '__main__':
    _thread.start_new_thread(alarm_clock, ("Time-Checker",))

    from routes import routes

    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host='0.0.0.0', port=9090)

