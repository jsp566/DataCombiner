class DataCollection:
    

    
    def groupData(self):
        raise NotImplementedError
    
    def update(self):
        updated = False
        for dataset in self.datasets:
            if dataset.update():
                updated = True

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