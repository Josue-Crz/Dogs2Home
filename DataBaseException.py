class DatabaseNotAvaiable(Exception):
    # customized msg for database exception
    def __init__(self, message="Google Cloud unable to reach firebase database"):
        self.message = message
        self.status_code = 503