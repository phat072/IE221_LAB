class String:
    def __init__(self, string=""):
        self.string = string

    def set_string(self, string):
        self.string = string

    def get_string(self):
        return self.string

    def length(self):
        return len(self.string)

    def concatenate(self, other):
        return String(self.string + other.string)

    def reverse(self):
        return String(self.string[::-1])

    def __str__(self):
        return self.string

