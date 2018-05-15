#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import os
import sys
import unittest

from mock import Mock

from sanji.connection.mockup import Mockup
from sanji.message import Message

_logger = logging.getLogger("Index")

try:
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
    from index import Index
except ImportError as e:
    print "Please check the python PATH for import test module. (%s)" \
        % __file__
    exit(1)


class TestIndexClass(unittest.TestCase):

    def setUp(self):
        root_path = os.path.dirname(os.path.realpath(__file__)) + "/../"
        try:
            os.unlink(root_path + "data/{{cookiecutter.project_slug}}.json")
            os.unlink(root_path + "data/{{cookiecutter.project_slug}}.json.backup")
        except Exception:
            pass

        self.index = Index(connection=Mockup())

    def tearDown(self):
        self.index.stop()
        self.index = None

    def test_get_ShouldPass(self):
        # arrange
        resp = Mock()

        # act
        self.index.get(
            message=None,
            response=resp,
            test=True)

        # assert
        _, _, kargs = resp.mock_calls[0]
        data = kargs["data"]
        self.assertFalse(data["enable"])

    def test_put_ShouldPass(self):
        # arrange
        msg = Message({
            "data": {
                "enable": True
            }
        })
        resp = Mock()

        # act
        self.index.put(
            message=msg,
            response=resp,
            test=True)

        # assert
        _, _, kargs = resp.mock_calls[0]
        data = kargs["data"]
        self.assertTrue(data["enable"])


if __name__ == "__main__":
    FORMAT = "%(asctime)s - %(levelname)s - %(lineno)s - %(message)s"
    logging.basicConfig(level=0, format=FORMAT)
    _logger = logging.getLogger("Index")
    unittest.main()
