import unittest
import configparser
import os
import inspect
import logging

from synco.lib.sql.sqlitemanager import SQLiteManager
from synco.lib.sql.models.file import File
from synco.lib.sql.models.filechunk import FileChunk

class SqliteManagerTests(unittest.TestCase):

    _sqlite_manager = None


    @classmethod
    def setUpClass(cls):
        cls._sqlite_manager = SQLiteManager()

    @classmethod
    def tearDownClass(cls):
        cls._sqlite_manager.close_everything()

    def test_instantiate(self):

        self._sqlite_manager.get_file(0)