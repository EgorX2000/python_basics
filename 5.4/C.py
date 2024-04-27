class Comment:
    def __init__(self, name, datetime, text):
        self.name = name
        self.date, self.time = datetime.split()
        self.text = text
        self.approved = False
        self.edited = False
        self.sub_comments = list()

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

    def __repr__(self):
        return f"Comment({self.name}, {self.date}, {self.time})"

    def get_sub_comments(self):
        return self.sub_comments

    def __iadd__(self, other):
        other.parent = self
        self.sub_comments.append(other)
        return self

    def __lt__(self, other):
        if not self.sub_comments:
            return False
        else:
            return other in self.sub_comments


class SubComment(Comment):
    def __init__(self, name, datetime, text, parent=None):
        super().__init__(name, datetime, text)
        self.parent = parent
        if parent is not None:
            parent.sub_comments.append(self)

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent
        parent.sub_comments.append(self)

    def __repr__(self):
        return f"SubComment({self.name}, {self.date}, {self.time}, {repr(self.parent)})"
