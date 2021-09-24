
class User:

    def __init__(self, username, password, permissions):
        self.username = username
        self.password = password
        self.permissions = self.parsePermissions(permissions)


    def has_permission(self, permission):
        return permission in self.permissions


    def parsePermissions(self, permissions):
        permissions = permissions.split(",")
        temp = list()
        for permission in permissions:
            temp.append(int(permission))
        return temp

    def save_format(self):
        save = ""
        save += self.username
        save += ":"
        save += self.password
        save += ":"

        for permission in self.permissions:
            save += f"{permission},"

        save = save[:-1]
        return save
