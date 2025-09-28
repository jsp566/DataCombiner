class DataCollection:
    def __init__(self, datasets):
        self.datasets = datasets


    def groupData(self):
        raise NotImplementedError
    
    def update(self, forceUpdate=False):
        updated = False
        for dataset in self.datasets:
            updated |= dataset.update(forceUpdate=forceUpdate)
        
        if updated:
            self.groupData()

        return updated
    
    def unique(self, parameterType, columnType=None):
        ids = set()

        for dataset in self.datasets:
            ids.update(dataset.unique(parameterType, columnType))

        return ids
    
    def search(self, parameterList, searchType=None, columnType=None, inclusive=False):
        if searchType is None:
            resultdict = {}
            for dataset in self.datasets:
                keys = dataset.search(parameterList, columnType, inclusive)
                resultdict[dataset.name] = keys
            return resultdict
        elif searchType == 'group':
            return self.groupSearch(parameterList)

    def groupSearch(self, parameterList):
        raise NotImplementedError
    
    def keysToResults(self, keys):
        results = []
        for dataset in self.datasets:
            results.append(dataset.keysToResults(keys))
        return results