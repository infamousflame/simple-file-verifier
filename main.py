"""A simple verifier for files downloaded online.

This currently supports the following hashing algorithms:
* MD5
* SHA1-3
"""

__all__ = []
__author__ = 'Krishna Ranchhod'
__version__ = '0.0.1'

from verifier_app import VerifierApp

if __name__ == '__main__':
    VerifierApp().run()
