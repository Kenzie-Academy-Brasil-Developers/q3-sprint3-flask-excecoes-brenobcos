class EmailAlreadyExistsError(Exception):
    def __init__(self, message=None, status_code=409):

        if not message:
            self.message = "Email already exists"
        else:
            self.message = message

        self.status_code = status_code