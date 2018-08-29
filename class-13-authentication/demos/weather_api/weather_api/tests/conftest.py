# from pyramid.testing import DummyRequest
# from pyramid.config import Configurator
# from webtest import TestApp
# import pytest


# @pytest.fixture
# def dummy_request():
#     return DummyRequest()


# @pytest.fixture
# def testapp():
#     def main():
#         config = Configurator()
#         config.include('pyramid_jinja2')
#         config.include('.routes')
#         config.scan()
#         return config.make_wsgi_app()

#     app = main()
#     return TestApp(app)


