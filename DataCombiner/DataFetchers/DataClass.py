import os
import DataFetchers.util as util
import pandas as pd

class Dataset:
    def __init__(self):
        self.updatedDate = None
        self.sourceDataDate = None
        self.data = None
        self.idToKeys = None

        # These attributes are set by the subclass
        self.name = None
        self.sourceDataExtension = None
        self.columnTypes = None

    def downloadSourceFile(self):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    def updateSourceFile(self):
        try:
            oldHash = util.getFileHash(self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension))
        except FileNotFoundError:
            self.downloadSourceFile()
            return True

        self.downloadSourceFile()

        newHash = util.getFileHash(self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension))

        if oldHash != newHash:
            return True

        return False


    def sourceFileToCommonFormat(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def createIdToKeys(self):
        raise NotImplementedError
    
    def update(self):
        updated = self.updateSourceFile()

        if updated:
            self.sourceFileToCommonFormat()
            
            # Implement this
            #self.createIdToKeys()

        return updated
    
    def getFilePath(self, folderName, fileExtension="csv"):
        return os.path.join(util.folder, folderName, f"{self.name}.{fileExtension}")
    
    def getSavedFiles(self, firstTime=True):
        try:
            self.updatedDate = os.path.getmtime(self.getFilePath(util.SourceFileFolderName, self.sourceDataExtension))
            self.data = pd.read_csv(self.getFilePath(util.CSVFileFolderName))
            self.idToKeys = pd.read_csv(self.getFilePath(util.IdToKeysFileFolderName))

            # Missing implementation for sourceDataDate
            self.sourceDataDate = None

        except FileNotFoundError:
            if firstTime:
                self.update()
                self.getSavedFiles(firstTime=False)
            else:
                raise FileNotFoundError

    def unique(self, parameterType, columnType=None):
        raise NotImplementedError
    
    def search(self, parameterList, columnType=None, inclusive=False):
        if inclusive:
            keys = set()
            def adder(keysum, keys):
                keysum.update(keys)
        else:
            keys = set(self.unique('Key'))
            def adder(keysum, keys):
                keysum.intersection_update(keys)

        for parameter in parameterList:
            adder(keys, self.idToKeys[columnType][parameter.type][parameter.value])
        return keys
    
    def keysToResults(self, keys):
        raise NotImplementedError
