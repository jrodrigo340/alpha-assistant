class MemoryService:
    def __init__(self):
        self.last_search = None

    def save_search(self, term):
        self.last_search = term

    def get_last_search(self):
        return self.last_search