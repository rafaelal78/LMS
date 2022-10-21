class user:
    def __init__(self, user_ID, user_type, fullname, username, password):
        self.user_ID = user_ID
        self.user_type = user_type
        self.fullname = fullname
        self.username = username
        self.password = password

class Class:
    def __init__(self, class_ID, user_ID):
        self.class_ID = class_ID
        self.user_ID = user_ID

class module:
    def __init__(self, module_ID, module_name, class_ID, file_path):
        self.module_ID = module_ID
        self.module_name = module_name
        self.class_ID = class_ID
        self.file_path = file_path

class content:
    def __init__(self, content_ID, content_name, class_ID, abs_file_path, module_ID):
        self.content_ID = content_ID
        self.content_name = content_name
        self.class_ID = class_ID
        self.absolute_path = abs_file_path
        self.module_ID = module_ID