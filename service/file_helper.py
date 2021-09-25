
class FileHelper:
    _FileInstance = None

    @staticmethod
    def start_helper(basePath):
        if FileHelper._FileInstance == None:
            FileHelper(basePath)
        else:
            return FileHelper._FileInstance

    @staticmethod
    def get_helper():
        if FileHelper._FileInstance != None:
            return FileHelper._FileInstance
        else:
            return None

    def __init__(self, basePath):
        if FileHelper._FileInstance != None:
            raise Exception("This class is a singleton!")
        else:
            FileHelper._FileInstance = self
            self._basePath = basePath

    def get_cwd_path(self, from_root):
        return (self._basePath + from_root)
