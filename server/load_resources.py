import importlib.util
import os, sys
from flask_restful import Api


def load_resource(app, name, path, model_name, uri):
    api = Api(app)
    spec = importlib.util.spec_from_file_location(name, path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    mcall = getattr(foo, model_name)
    api.add_resource(mcall, uri)
    return app


def find_resources(app):
    for name in os.listdir("resources"):
        path = os.path.join('resources', name)
        if not os.path.isdir(path):
            continue
        controller_name = "%s_controller.py" % name.lower()
        model_name = name
        uri = "/%s" % name.lower()
        controller_path = os.path.join(path, controller_name)
        resource_name = 'resource.%s' % name
        if not os.path.isfile(controller_path):
            continue
        try:
            load_resource(app, resource_name, controller_path, model_name, uri)
        except Exception as e:
            print(e)
            sys.exit()
