class Drug:

    name = ""
    description = ""
    indication = ""
    toxicity = ""
    products = ""

    def __init__(self, n, d, i, t, p):
        self.name = n
        self.description = d
        self.indication = i
        self.toxicity = t
        self.products = p
