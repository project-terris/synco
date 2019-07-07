import sqlite3
import uuid
import datetime
import time as t

import os
import inspect

from synco.lib.sql.models.file import File
from synco.lib.sql.models.filechunk import FileChunk


class SQLiteManager:

    _db_dir = None
    _db_path = None
    _cursor = None
    _logger = None

    def __init__(self):

        self._conn = sqlite3.connect(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
                                     + os.sep + 'synco.db')
        self._cursor = self._conn.cursor()

        self._cursor.execute('''CREATE TABLE IF NOT EXISTS files
                            (id INTEGER PRIMARY KEY, guid TEXT, relpath TEXT, total_chunks INTEGER, file_sha256 BLOB)''')

        self._cursor.execute('''CREATE TABLE IF NOT EXISTS file_chunks
                            (id INTEGER PRIMARY KEY, guid TEXT, file_id INTEGER, chunk_id INTEGER, chunk_sha256 BLOB)''')
        self._conn.commit()

    def close_everything(self):
        try:
            self._cursor.close()
            self._conn.close()
        except:
            print("SQLiteManager - Exception was thrown while shutting down the SQLite connection. Do we care ?")

    def insert_file(self, file:File)->File:
        guid = file.guid
        if file.guid is None:
            guid = uuid.uuid4()

        relpath = file.relpath
        total_chunks = file.total_chunks
        file_sha256 = file.file_sha256

        query = "INSERT INTO files (guid, relpath, total_chunks, file_sha256) VALUES ('{guid}', '{relpath}', '{total_chunks}', ?)"
        query = query.format(guid=guid, relpath=relpath, total_chunks=total_chunks)

        self._cursor.execute(query, [memoryview(bytes(file_sha256))])
        file_id = self._cursor.lastrowid
        self._conn.commit()

        return self.get_file(file_id)

    def get_file(self, file_id:int):
        query = "SELECT id, guid, relpath, total_chunks, file_sha256 FROM files WHERE id = " + str(file_id)
        self._cursor.execute(query)
        file = self._cursor.fetchone()


        if file is None:
            return None

        file_model = File()
        file_model.id = file[0]
        file_model.guid = file[1]
        file_model.relpath = file[2]
        file_model.total_chunks = file[3]
        file_model.file_sha256 = str(file[4])

        return file_model

    def update_file(self, file_id:int, file:File)->File:
        self.delete_file(file_id)
        return self.insert_file(file)

    def delete_file(self, file_id:int)->File:
        file = self.get_file(file_id)
        query = "DELETE FROM files WHERE id = '" + str(file_id) + "'"
        self._cursor.execute(query)
        self._conn.commit()
        return file

    def insert_file_chunk(self, file_chunk:FileChunk)->FileChunk:
        guid = file_chunk.guid
        if file_chunk.guid is None:
            guid = uuid.uuid4()

        file_id = file_chunk.file_id
        chunk_id = file_chunk.chunk_id
        chunk_sha256 = file_chunk.chunk_sha256

        query = "INSERT INTO file_chunks (guid, file_id, chunk_id, chunk_sha256) VALUES ('{guid}', '{file_id}', '{chunk_id}', ?)"
        query = query.format(guid=guid, file_id=file_id, chunk_id=chunk_id)

        self._cursor.execute(query, [memoryview(bytes(chunk_sha256))])
        file_chunk_id = self._cursor.lastrowid
        self._conn.commit()

        return self.get_file_chunk(file_chunk_id)

    def get_file_chunk(self, file_chunk_id:int):
        query = "SELECT id, guid, file_id, chunk_id, chunk_sha256 FROM file_chunks WHERE id = " + str(file_chunk_id)
        self._cursor.execute(query)
        file_chunk = self._cursor.fetchone()

        if file_chunk is None:
            return None

        file_model = FileChunk()
        file_model.id = file_chunk[0]
        file_model.guid = file_chunk[1]
        file_model.file_id = file_chunk[2]
        file_model.chunk_id = file_chunk[3]
        file_model.chunk_sha256 = str(file_chunk[4])

        return file_model

    def update_file_chunk(self, file_chunk_id:int, file_chunk:FileChunk)->FileChunk:
        self.delete_file_chunk(file_chunk_id)
        return self.insert_file_chunk(file_chunk)

    def delete_file_chunk(self, file_chunk_id:int)->FileChunk:
        file_chunk = self.get_file_chunk(file_chunk_id)
        query = "DELETE FROM file_chunks WHERE id = '" + str(file_chunk_id) + "'"
        self._cursor.execute(query)
        self._conn.commit()
        return file_chunk

