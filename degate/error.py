class Error(Exception):
    pass


class ClientError(Error):
    def __init__(self, status_code, error_code, error_message, header):
        # https status code
        self.status_code = status_code
        # error code returned from server
        self.error_code = error_code
        # error message returned from server
        self.error_message = error_message
        # the whole response header returned from server
        self.header = header

    def __str__(self):
        return "Found ClientError. status: {}, error code: {}, error message: {}".format(self.status_code, self.error_code, self.error_message)


class DeGateError(Error):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return "Found DeGateError {}".format(self.error_message)

class ServerError(Error):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return "Found ServerError. status: {}, error message: {}".format(self.status_code, self.message)


class ParameterRequiredError(Error):
    def __init__(self, params):
        self.params = params

    def __str__(self):
        return "%s is mandatory, but received empty." % (", ".join(self.params))


class ParameterValueError(Error):
    def __init__(self, params):
        self.params = params

    def __str__(self):
        return "the enum value %s is invalid." % (", ".join(self.params))


class ParameterTypeError(Error):
    def __init__(self, params):
        self.params = params

    def __str__(self):
        return f"{self.params[0]} data type has to be {self.params[1]}"


class ParameterArgumentError(Error):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message
