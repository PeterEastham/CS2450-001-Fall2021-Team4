import csv
from model.user import User
from service.version_handling import class_csv_headers
from service.file_helper import FileHelper as FH


"""
userRepo won't use the BaseCSVRepo just due to its current behavior.
"""
class UserRepo:
    #We'll include a resourceString, but this should never really change.
    #It's mostly to maintain it's format with the other repos.
    def __init__(self, repoPath):
        self.repoPath = repoPath
        self.users = []
        self.__load_repo()

    #Private Method.
    def  __load_repo(self):
        with open(self.repoPath, 'r') as repo:
            csvReader = csv.DictReader(repo)
            for row in csvReader:
                print(row)
                self.users.append(User( row['username'], row['password'],
                                        row['permissions'] ) )

    #LoginController.validate() wraps this.
    def validLogin(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True

        return False

    #Our version of "get_one_by_id"
    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user

    #Only the UserController should call this.
    #Exception: self.update_user()
    def add_one(self, user):
        self.users.append(user)

    #Only the UserController should call this.
    #Exception: self.update_user()
    def remove_one_by_username(self, username):
        for user in self.users:
            if user.username == username:
                self.users.remove(user)

    #Wrapper for remove/add, easiest way to handle it really.
    def update_user(self, updated_user):
        self.remove_one_by_username(updated_user.username)
        self.add_one(updated_user)

    #We'll keep all the users, since in theory we shouldn't
    #Expect the users to be inside the repo.
    def save_repo(self):
        with open(self.repoPath, 'w') as repo:
            repo.write(class_csv_headers(self.users[0]))
            for user in self.users:
                repo.write(user.save_format())

    #More formal version of save_repo(), but we empty self.users to
    #Prevent other functions from functioning.
    def close_repo(self):
        with eopn(self.repoPath, 'w') as repo:
            repo.write(class_csv_headers(self.users[0]))
            for user in self.users:
                repo.write(user.save_format())

        self.users = []
