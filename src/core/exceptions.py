class AppException(Exception):
    status_code = 500

    def __init__(self, message: str, *, details: dict | None = None):
        self.message = message
        self.details = details or {}
        super().__init__(message)


class NotFoundError(AppException):
    status_code = 404


class ValidationError(AppException):
    status_code = 400


class DatabaseError(AppException):
    status_code = 500
