import os
from pathlib import Path
import requests

import sqlite3


folder = os.path.dirname(__file__)
SourceFileFolderName = 'DataStorage/SourceFiles'
SQLcons = {"SQLite": sqlite3.connect('DataStorage/Database.db')}


TableNames = {
    "SourceFiles": "SourceFiles",
    "DataRows": "DataRows",
    "BankCodes": "BankCodes",
    "BankCodeRelations": "BankCodeRelations",
}

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
    

def createFolderIfNotExists(folderPath, folderName):
    """Creates a folder if it does not already exist."""
    fullPath = os.path.join(folderPath, folderName)
    Path(fullPath).mkdir(parents=True, exist_ok=True)
    return fullPath