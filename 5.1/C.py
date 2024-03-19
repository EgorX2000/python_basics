class RedButton:
    def __init__(self):
        self.click_count = 0

    def click(self):
        print("Тревога!")
        self.click_count += 1

    def count(self):
        return self.click_count
