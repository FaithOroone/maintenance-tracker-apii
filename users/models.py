class Users:
    def __init__(self, first_name, last_name, user_id, email, password, confirm_password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_user_id(self):
        return self.user_id

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_confirm_password(self):
        return self.confirm_password

def __repr__(self):
       return repr(self._dict_)
users = []

class Requests:
    def __init__(self,name, category, request_type, description, department,request_id, status):
        self.name = name
        self.category = category
        self.request_type = request_type
        self.description = description
        self.department = department
        self.request_id = request_id
        self.status = status

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_request_type(self):
        return self.request_type

    def get_description(self):
        return self.description

    def get_department(self):
        return self.department
    def get_request_id(self):
        return self.request_id

    def get_status(self):
        return self.status

    def __repr__(self):
       return repr(self._dict_)
requests = []
