import os
from pathlib import Path
import requests

SourceFileFolderName = 'SourceFiles'
CSVFileFolderName = 'CSVFiles' # CSV files in common format
EnhancedFormatFileFolderName = 'EnhancedFormatFiles' # Pickle files with enhanced format
IdToKeysFileFolderName = 'IdToKeys'

folder = os.path.dirname(__file__)

class ColumnDescription:
    def __init__(self):
        self.name = None
        self.description = None
        self.datatype = None # e.g. "string", "int", "float", "date"
        self.idtype = None # e.g. BIC, NAME, 
        self.relationtype = None # e.g. self, sponsor, group, result



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

def createFolderIfNotExists(folderPath, folderName):
    """Creates a folder if it does not already exist."""
    fullPath = os.path.join(folderPath, folderName)
    Path(fullPath).mkdir(parents=True, exist_ok=True)
    return fullPath