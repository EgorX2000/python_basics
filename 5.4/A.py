class Comment:
    def __init__(self, name, datetime, text):
        self.name = name
        self.date, self.time = datetime.split()
        self.text = text

    def get_author(self):
        return self.name

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_text(self):
        return self.text
