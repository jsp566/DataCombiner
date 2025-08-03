import os
from pathlib import Path
import requests

SourceFileFolderName = 'SourceFiles'
CommonFormatFileFolderName = 'CommonFormatFiles'
IdToKeysFileFolderName = 'IdToKeys'

folder = os.path.dirname(__file__)

def urlToFile(url, filePath):
    """Downloads a file from a URL and saves it to the specified file path."""
    response = requests.get(url, stream=True)

    with open(filePath, mode="wb") as file:
        for chunk in response.iter_content(chunk_size=10 * 1024):
            file.write(chunk)
    
def getFileHash(filePath):
    """Calculates the hash of a file."""
    import hashlib
    hash_md5 = hashlib.md5()
    with open(filePath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()