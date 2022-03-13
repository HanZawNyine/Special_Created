class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result


class IllegalCharacterError(Error):
    def __init__(self, details):
        super().__init__("Illegal Character ", "'" + details + "'")


if __name__ == '__main__':
    print(IllegalCharacterError("d").as_string())
