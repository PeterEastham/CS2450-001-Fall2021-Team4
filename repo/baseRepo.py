from abc import ABC, abstractmethod
from service.version_handling import class_csv_headers
import csv

class BaseCSVRepo(ABC):

    def __init__(self, repoPath):
        self.repoPath = repoPath
        self.objects = []
        self._load_repo()

    def _load_repo(self):
        with open(self.repoPath, 'r') as repo:
            reader = csv.DictReader(repo)
            for row in reader:
                self.objects.append(self.make_object(row))

    @abstractmethod
    def make_object(self, dict_object):
        pass

    def add_one(self, object):
        self.objects.append(object)

    #We assume all the objects have IDs
    #Potentially we override the __compare__ for each?
    def get_one_by_id(self, id):
        for object in self.objects:
            if object.id == id:
                return object
        return None

    def get_all(self):
        return self.objects

    def remove_one_by_id(self, id):
        for object in self.objects:
            if object.id == id:
                self.objects.remove(object)

    def update_object(self, object):
        self.remove_one_by_id(object.id)
        self.add_one(object)

    def save_repo(self):
        save_objects = self.save_objects_list()
        with open(self.repoPath, 'w') as save_loc:
            for object in save_objects:
                save_loc.write(object)

    def export_repo(self, export_loc_path):
        save_objects = self.save_objects_list()
        with open(export_loc_path, 'w') as export_loc:
            for object in save_objects:
                export_loc.write(object)

    """
    This function should return a list with each index being a new line to write to
    the ouput file. If you odn't want CSV headers for example.
    """
    @abstractmethod
    def save_objects_list(self):
        pass
