
class File:

    # type: int
    id = None
    # type: str
    guid = None
    # type: str
    relpath = None
    # type: int
    total_chunks = None
    # type: str
    file_sha256 = None

    def to_dictionary(self):
        return {
            'id': self.id,
            'guid': str(self.guid),
            'relpath': self.relpath,
            'total_chunks': self.total_chunks,
            'file_sha256': str(self.file_sha256)
        }