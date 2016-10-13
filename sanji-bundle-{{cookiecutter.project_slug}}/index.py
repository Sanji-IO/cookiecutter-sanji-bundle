#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import logging
from sanji.core import Sanji
from sanji.core import Route
from sanji.model_initiator import ModelInitiator
from sanji.connection.mqtt import Mqtt


_logger = logging.getLogger("sanji.{{ cookiecutter.project_name.lower().replace(' ', '_') }}")


class Index(Sanji):

    def init(self, *args, **kwargs):
        self.path_root = os.path.abspath(os.path.dirname(__file__))
        self.model = ModelInitiator("{{ cookiecutter.project_name.lower().replace(' ', '_') }}", self.path_root)

{% if 'get' in cookiecutter.resource_methods %}
    @Route(methods="get", resource="{{ cookiecutter.resource_uri }}")
    def _get(self, message, response):
        return response(data=self.model.db)
{% endif %}
{% if 'put' in cookiecutter.resource_methods %}
    @Route(methods="put", resource="{{ cookiecutter.resource_uri }}")
    def _put(self, message, response):
        try:
            self.model.db = message.data
            self.model.save_db()
        except Exception as e:
            return response(code=400, data={"message": e.message})

        return response(data=message.data)
{% endif %}

if __name__ == '__main__':
    FORMAT = '%(asctime)s - %(levelname)s - %(lineno)s - %(message)s'
    logging.basicConfig(level=0, format=FORMAT)
    logging.getLogger("sh").setLevel(logging.WARN)
    index = Index(connection=Mqtt())
    index.start()
