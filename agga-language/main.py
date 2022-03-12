from lexr import run

if __name__ == "__main__":

    while True:
        text = input('Agga (Multi)> ')
        result, error = run('<stdin>', text)

        if error:
            print(error.as_string())
        else:
            print(result)
