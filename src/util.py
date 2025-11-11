import os
from pathlib import Path
import requests
from enum import Enum
import sqlite3


folder = os.path.dirname(__file__)
SourceFileFolderName = 'SourceFiles'
SQLcons = {"SQLite": sqlite3.connect('Database.db')}


TableNames = {
    "SourceFiles": "Data.SourceFiles",
    "DataRows": "Data.DataRows"
}

class ColumnDescription:
    def __init__(self):
        self.name = None
        self.description = None
        self.datatype = None # e.g. "string", "int", "float", "date"
        self.idtype = None # e.g. BIC, NAME, 
        self.relationtype = None # e.g. self, sponsor, group, result


class DatasetId(Enum):
    BSBDirectory = 1
    BSBKeys = 2
    BundesSCLFromURL = 3
    OctInstAdherence = 4
    SDDB2BAdherence = 5
    SDDCoreAdherence = 6
    SepaAdherence = 7
    SepaInstAdherence = 8
    SIC = 9
    SPAAAdherence = 10
    SRTPAdherence = 11
    VOPAdherence = 12

class FileStatus(Enum):
    New = 1
    Processed = 2
    Error = 3


class FileType(Enum):
    SourceFile = 1
    CSVFile = 2
    EnhancedFormatFile = 3
    IdToKeysFile = 4

class idtype(Enum):
    BIC = 1
    NAME = 2


class relationtype(Enum):
    SELF = 1
    SPONSOR = 2
    GROUP = 3
    RESULT = 4



def urlToFile(url, filePath):
    """Downloads a file from a URL and saves it to the specified file path."""
    response = requests.get(url, stream=True)

    with open(filePath, mode="wb") as file:
        for chunk in response.iter_content(chunk_size=10 * 1024):
            file.write(chunk)
    

def createFolderIfNotExists(folderPath, folderName):
    """Creates a folder if it does not already exist."""
    fullPath = os.path.join(folderPath, folderName)
    Path(fullPath).mkdir(parents=True, exist_ok=True)
    return fullPath