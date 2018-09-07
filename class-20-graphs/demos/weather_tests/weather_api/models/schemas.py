from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from . import WeatherLocation, Account, AccountRole


class AccountRoleSchema(ModelSchema):
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')

    class Meta:
        model = Account


class WeatherLocationSchema(ModelSchema):
    #  This is really just an example of multiple fields
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')
    account = fields.Nested(AccountSchema, exclude=(
        'password', 'locations', 'roles', 'date_created', 'date_updated',
    ))

    class Meta:
        model = WeatherLocation