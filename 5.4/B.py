class Comment:
    def __init__(self, name, datetime, text):
        self.name = name
        self.date, self.time = datetime.split()
        self.text = text
        self.approved = False
        self.edited = False

    def get_author(self):
        return self.name

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_text(self):
        return self.text

    def approve(self):
        self.approved = True

    def is_approved(self):
        return self.approved

    def set_text(self, new_text):
        self.text = new_text
        self.approved = False
        self.edited = True

    def is_edited(self):
        return self.edited

    def __str__(self):
        return f"{self.text}\n[{self.name} ({self.date} {self.time})]\n"
