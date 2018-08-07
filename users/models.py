class Users:
    def __init__(self, first_name, last_name, email, password, confirm_password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_confirm_password(self):
        return self.confirm_password

def __repr__(self):
       return repr(self._dict_)
users = []