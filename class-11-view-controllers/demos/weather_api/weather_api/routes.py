from pyramid_restful.routers import ViewSetRouter
from .views.location import WeatherLocationAPIView


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('lookup', '/api/v1/lookup/{zip_code}')

    router = ViewSetRouter(config)
    router.register('api/v1/location', WeatherLocationAPIView, 'location')