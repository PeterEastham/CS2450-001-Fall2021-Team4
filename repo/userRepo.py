import csv
from model.user import User
from service.version_handling import class_csv_headers

class UserRepo:

    def __init__(self, resourceString=".//resources//users.csv"):
        self.users = []
        self.repoPath = resourceString
        self.__load_repo()

    def  __load_repo(self):
        with open(self.repoPath, 'r') as repo:
            csvReader = csv.DictReader(repo, delimiter=":")
            for row in csvReader:
                print(row)
                self.users.append(User( row['username'], row['password'],
                                        row['permissions'] ) )

    def validLogin(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True

        return False

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def add_one(self, user):
        self.users.append(user)

    def remove_one_by_username(self, username):
        for user in self.users:
            if user.username == username:
                self.users.remove(user)

    def update_user(self, updated_user):
        self.remove_one_by_username(updated_user.username)
        self.add_one(updated_user)

    def save_repo(self):
        with open(self.repoPath, 'w') as repo:
            repo.write(class_csv_headers(self.users[0]).replace(",",":"))
            for user in self.users:
                repo.write(user.save_format())
