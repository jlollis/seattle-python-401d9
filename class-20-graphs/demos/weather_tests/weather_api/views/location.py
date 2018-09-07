from sqlalchemy.exc import IntegrityError, DataError
from ..models.schemas import WeatherLocationSchema
from pyramid_restful.viewsets import APIViewSet
from ..models import WeatherLocation, Account
from pyramid.response import Response
import requests
import json


class LocationLookupAPIView(APIViewSet):
    def list(self, request, zip_code=None):
        """
        """
        # import pdb; pdb.set_trace()
        url = 'https://api.openweathermap.org/data/2.5/weather?zip={}&APPID={}'.format(
            zip_code,
            '75a7450d79ddcdbf8ceef630bf21766b',
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

        # This is new, and required for managing model relationships
        if request.authenticated_userid:
            account = Account.one(request, request.authenticated_userid)
            kwargs['account_id'] = account.id

        try:
            weather = WeatherLocation.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Zip code already exists', status=409)

        schema = WeatherLocationSchema()
        data = schema.dump(weather).data

        return Response(json=data, status=201)

    def list(self, request):
        """
        """
        if not request.authenticated_userid:
            return Response(json='Forbidden', status=403)

        all_records = WeatherLocation.all(request)
        user_records = [record for record in all_records if record.accounts.email == request.authenticated_userid]

        schema = WeatherLocationSchema()
        data = [schema.dump(record).data for record in user_records]

        return Response(json=data, status=200)

    def retrieve(self, request, id=None):
        """
        """
        record = WeatherLocation.one(request, id)
        if not record:
            return Response(json='Not Found', status=404)

        schema = WeatherLocationSchema()
        data = schema.dump(record).data

        return Response(json=data, status=200)


    def destroy(self, request, id=None):
        """
        """
        if not request.authenticated_userid:
            return Response(json='Forbidden', status=403)

        if not id:
            return Response(json='Not Found', status=404)

        try:
            WeatherLocation.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204)