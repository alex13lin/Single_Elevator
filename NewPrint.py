TO_PRINT = True


class NewPrint(object):
    def __init__(self, message):
        self.message = message
        self.run()

    def run(self):
        if TO_PRINT:
            print(self.message)
