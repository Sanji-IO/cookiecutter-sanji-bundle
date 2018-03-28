#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging

from sanji.core import Route
from sanji.core import Sanji

from {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}} import {{cookiecutter.project_slug[0].upper()+cookiecutter.project_slug[1:]}}


_logger = logging.getLogger("sanji.{{cookiecutter.project_slug}}")


class Index(Sanji):

    def init(self, *args, **kwargs):
        self.{{cookiecutter.project_slug}} = {{cookiecutter.project_slug[0].upper()+cookiecutter.project_slug[1:]}}()
{% if 'get' in cookiecutter.resource_methods %}
    @Route(methods="get", resource="{{cookiecutter.resource_endpoint}}")
    def get(self, message, response):
        return response(data=self.{{cookiecutter.project_slug}}.get())
{%- endif %}
{% if 'put' in cookiecutter.resource_methods %}
    @Route(
        methods="put",
        resource="{{cookiecutter.resource_endpoint}}",
        schema={{cookiecutter.project_slug[0].upper()+cookiecutter.project_slug[1:]}}.PUT_SCHEMA)
    def put(self, message, response):
        try:
            self.{{cookiecutter.project_slug}}.put(message.data)
        except Exception as e:
            return response(code=400, data={"message": e.message})

        return response(data=message.data)
{%- endif %}


if __name__ == "__main__":
    from sanji.connection.mqtt import Mqtt

    FORMAT = "%(asctime)s - %(levelname)s - %(lineno)s - %(message)s"
    logging.basicConfig(level=0, format=FORMAT)
    _logger = logging.getLogger("sanji.{{cookiecutter.project_slug}}")

    index = Index(connection=Mqtt())
    index.start()
