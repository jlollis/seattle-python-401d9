from ..models.schemas import WeatherLocationSchema
from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.response import Response
from pyramid.view import view_config
from ..models import WeatherLocation
import requests
import json


@view_config(route_name='lookup', renderer='json', request_method='GET')
def lookup(request):
    """
    """
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={}&APPID={}'.format(
        request.matchdict['zip_code'],
        '8e0c26a44bf6712344c15767b017840e',
    )
    response = requests.get(url)

    return Response(json=response.json(), status=200)


class WeatherLocationAPIView(APIViewSet):
    def create(self, request):
        """
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'zip_code' not in kwargs:
            return Response(json='Expected value; zip_code', status=400)

        try:
            weather = WeatherLocation.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Zip code already exists', status=409)

        schema = WeatherLocationSchema()
        data = schema.dump(weather).data

        return Response(json=data, status=201)

    def list(self, request):
        return Response(json={'message': 'listing all the records'}, status=200)

    def retrieve(self, request, id=None):
        return Response(json={'message': 'listing one of the records'}, status=200)

    def destroy(self, request, id=None):
        """
        """
        if not id:
            return Response(json='Not Found', status=404)

        try:
            WeatherLocation.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204)