import uuid

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log_error(self, message):
        guid = uuid.uuid4()
        with open("error_log.txt", "a") as file:
            file.write(f"[{guid}] {message}\n")