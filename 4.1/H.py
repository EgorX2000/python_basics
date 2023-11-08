def is_palindrome(data):
    if type(data) is int:
        data = str(data)
    if data == data[::-1]:
        return True
    else:
        return False
