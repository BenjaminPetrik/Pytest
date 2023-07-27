class ResponseModel:
    def __init__(self, status: int, body: dict = None):
        self.status = status
        self.body = body
