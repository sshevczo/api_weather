class EmailStorageService:
    def __init__(self):
        self.email_results = []

    def save_result(self, result):
        self.email_results.append(result)

    def get_results(self):
        return self.email_results
    
    def delete_result(self, index):
        if 0 <= index < len(self.email_results):
            del self.email_results[index]
