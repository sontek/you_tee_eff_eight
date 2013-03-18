from pyramid.config         import Configurator

from pyramid.view           import view_config
from pyramid.i18n           import TranslationStringFactory
from pyramid.i18n           import get_localizer
from pyramid.threadlocal    import get_current_request

from deform                 import Form
from pkg_resources          import resource_filename


import colander
import deform

_ = TranslationStringFactory('you_tee_eff_eight')

class BaseForm(deform.Form):
    def __init__(self, request, *args, **kwargs):
        self.request = request

        deform_templates = resource_filename('deform', 'templates')
        search_path = resource_filename('you_tee_eff_eight', 'templates/deform')

        self.set_zpt_renderer([
            search_path
            , deform_templates
        ], translator=translator)

        super(BaseForm, self).__init__(*args, **kwargs)


def translator(term):
    request = get_current_request()
    if request is not None:
        return get_localizer(request).translate(term)
    else:
        return term.interpolate() if hasattr(term, 'interpolate') else term

@view_config(route_name='home', renderer='you_tee_eff_eight:templates/home.mako')
def home_view(request):
    languages = request.registry.settings['available_languages']

    return {'available_languages': languages}

class TestSchema(colander.TupleSchema):
    name = colander.SchemaNode(
        colander.String(),
        title = _("FOO")
    )

@view_config(route_name='colander', renderer='you_tee_eff_eight:templates/colander.mako')
def colander_view(request):
    schema = TestSchema()
    form = BaseForm(request, schema=schema)

    return {'form': form.render()}

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('colander', '/colander')
    config.add_translation_dirs('you_tee_eff_eight:locale/')
    config.scan()
    return config.make_wsgi_app()
