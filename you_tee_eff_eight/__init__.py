from pyramid.config import Configurator

from pyramid.view import view_config


@view_config(route_name='home', renderer='you_tee_eff_eight:templates/home.mako')
def home_view(request):
    languages = request.registry.settings['available_languages']

    return {'available_languages': languages}


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
