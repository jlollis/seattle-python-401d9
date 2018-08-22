from pyramid_restful.routers import ViewSetRouter
from .views.weather import WeatherAPIView
# from .views.auth import AuthAPIView


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    router.register('api/v1/weather', WeatherAPIView, 'weather')
    # router.register('api/v1/auth', AuthAPIView, 'auth')