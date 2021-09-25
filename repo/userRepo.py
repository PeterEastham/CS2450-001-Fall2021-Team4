import csv
from model.user import User
from service.version_handling import class_csv_headers
from service.file_helper import FileHelper as FH


"""
Of all the modules, the Repo module could use a Parent Class.
I need to study up on inheritance, could be useful to use a
factory construction pattern? Pass it the object, and then
it uses the provided information to handle that?
"""
class UserRepo:
    #We'll include a resourceString, but this should never really change.
    #It's mostly to maintain it's format with the other repos.
    def __init__(self, repoPath=".//resources//users.csv"):
        file_aid = FH.get_helper()
        self.repoPath = file_aid.get_cwd_path(repoPath)
        self.users = []
        self.__load_repo()

    #Private Method.
    def  __load_repo(self):
        with open(self.repoPath, 'r') as repo:
            csvReader = csv.DictReader(repo, delimiter=":")
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
    #Expect the users to inside the repo.
    def save_repo(self):
        with open(self.repoPath, 'w') as repo:
            repo.write(class_csv_headers(self.users[0]).replace(",",":"))
            for user in self.users:
                repo.write(user.save_format())

    #More formal version of save_repo(), but we empty self.users to
    #Prevent other functions from functioning.
    def close_repo(self):
        with eopn(self.repoPath, 'w') as repo:
            repo.write(class_csv_headers(self.users[0]).replace(",",":"))
            for user in self.users:
                repo.write(user.save_format())

        self.users = []
