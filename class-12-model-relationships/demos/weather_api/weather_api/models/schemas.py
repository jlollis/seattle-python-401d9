from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from . import WeatherLocation, Account, AccountRole


class AccountRoleScheme(ModelSchema):
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    roles = fields.Nested(AccountRoleScheme, many=True, only='name')

    class Meta:
        model = Account


class WeatherLocationSchema(ModelSchema):
    roles = fields.Nested(AccountRoleScheme, many=True, only='name')
    account = fields.Nested(AccountSchema, exclude=(
        'password', 'locations', 'roles', 'date_created', 'date_updated'))

    class Meta:
        model = WeatherLocation
