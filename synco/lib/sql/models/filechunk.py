

class FileChunk:

    # type: int
    id = None
    # type: str
    guid = None
    # type: int
    file_id = None
    # type: int
    chunk_id = None
    # type: str
    chunk_sha256 = None

    def to_dictionary(self):
        return {
            'id': self.id,
            'guid': str(self.guid),
            'file_id': self.file_id,
            'chunk_id': self.chunk_id,
            'chunk_sha256': str(self.chunk_sha256)
        }