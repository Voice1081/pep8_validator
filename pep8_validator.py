class PEP8Validator:
    def __init__(self, *validators):
        self.validators = []
        self.register(*validators)

    def register(self, *validators):
        for v in validators:
            self.validators.append(v)

    def validate(self, string):
        for v in self.validators:
            string = v.validate(string)
        return string
