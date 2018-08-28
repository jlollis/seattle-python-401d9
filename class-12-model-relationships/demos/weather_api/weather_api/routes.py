from pyramid_restful.routers import ViewSetRouter
from .views.weather_location import WeatherLocationAPIView
from .views.auth import AuthAPIView


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('lookup', '/api/v1/lookup/{zip}')

    router = ViewSetRouter(config)
    # NOTE: Discuss permissions on location route and parameter to auth route (optionally add permissions to auth)
    router.register('api/v1/location', WeatherLocationAPIView, 'location')
    router.register('api/v1/auth/{auth}', AuthAPIView, 'auth')
