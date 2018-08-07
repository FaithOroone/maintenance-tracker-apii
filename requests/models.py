class Requests:
    def __init__(self,name, category, request_type, description, department, status):
        self.name = name
        self.category = category
        self.request_type = request_type
        self.description = description
        self.department = department
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

    def get_status(self):
        return self.status

    def __repr__(self):
       return repr(self._dict_)
requests = []
