"""Performs the hashing of files."""

__all__ = ['SUPPORTED_ALGORITHMS', 'DEFAULT_HASH_ALGORITHM', 'hasher']

from hashlib import new as new_hash

SUPPORTED_ALGORITHMS: dict[str, str] = {
    'md5': 'MD5',
    'sha1': 'SHA-1',
    'sha224': 'SHA-224',
    'sha256': 'SHA-256',
    'sha384': 'SHA-384',
    'sha512': 'SHA-512',
    'sha3_224': 'SHA3-224',
    'sha3_256': 'SHA3-256',
    'sha3_384': 'SHA3-384',
    'sha3_512': 'SHA3-512',
    'blake2b': 'BLAKE2b',
    'blake2s': 'BLAKE2s'
}

DEFAULT_HASH_ALGORITHM: str = 'sha256'


class Hasher:
    """Class that does all the hashing."""
    def __init__(self) -> None:
        self._hash_algorithm: str = DEFAULT_HASH_ALGORITHM
        self._file_path: str = ''

    @property
    def hash_algorithm(self) -> str:
        """The hash algorithm to be used.

        Returns:
            str: The current value of `_hash_algorithm`.
        """
        return self._hash_algorithm


    @hash_algorithm.setter
    def hash_algorithm(self, value: str) -> None:
        """The hash algorithm to be used.

        Args:
            value (str): The value to set `_hash_algorithm` to.
        """
        self._hash_algorithm = value


    @property
    def file_path(self) -> str:
        """The path of the file to hash.

        Returns:
            str: The current value of `_file_path`.
        """
        return self._file_path


    @file_path.setter
    def file_path(self, value: str) -> None:
        """The path of the file to hash.

        Args:
            value (str): The value to set `_file_path` to.
        """
        self._file_path = value


    def compute_digest(self) -> tuple[str, int]:
        """Computes the file's hash digest (if possible).

        Returns:
            tuple[str, int]: The hexadecimal digest (if successful)
            or error message (if there was one), and a status code:

        Status codes:
            0 - successful
            1 - file not found
            2 - permission denied
            3 - no file selected
        """
        if not self._file_path:
            return '', 3

        hash_object = new_hash(self._hash_algorithm)
        try:
            with open(self._file_path, 'rb') as f:
                while True:
                    chunk: bytes = f.read(1024)
                    if not chunk:
                        break
                    hash_object.update(chunk)
        except FileNotFoundError as e:
            return str(e), 1
        except PermissionError as e:
            return str(e), 2
        else:
            return hash_object.hexdigest(), 0

hasher = Hasher()
