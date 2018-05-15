#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import os

from sanji.model_initiator import ModelInitiator

from voluptuous import Required
from voluptuous import REMOVE_EXTRA
from voluptuous import Schema


_logger = logging.getLogger("sanji.{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}")


class {{cookiecutter.project_slug[0].upper()+cookiecutter.project_slug[1:]}}(object):

    PUT_SCHEMA = Schema({
        Required("enable"): bool
    }, extra=REMOVE_EXTRA)

    def __init__(self, *args, **kwargs):
        root_path = os.path.abspath(os.path.dirname(__file__) + "/../")
        self.model = ModelInitiator("{{cookiecutter.project_slug}}", root_path)

    def get(self):
        return self.model.db

    def put(self, data):
        _data = self.PUT_SCHEMA(data)
        self.model.db = _data
        self.model.save_db()
        return _data
