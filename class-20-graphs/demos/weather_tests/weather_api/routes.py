from .views.location import WeatherLocationAPIView, LocationLookupAPIView
from pyramid_restful.routers import ViewSetRouter
from .views.auth import AuthAPIViewset


def includeme(config):
    config.add_route('home', '/')

    router = ViewSetRouter(config, trailing_slash=False)
    router.register('api/v1/auth/{auth}', AuthAPIViewset, 'auth')
    router.register('api/v1/location', WeatherLocationAPIView, 'location', permission='admin')
    router.register('api/v1/lookup/{zip_code}', LocationLookupAPIView, 'lookup')