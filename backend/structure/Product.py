class Product:

    name = ""
    dosageForm = ""
    strength = ""
    route = ""

    def __init__(self, n, d, s, r):
        self.name = n
        self.dosageForm = d
        self.strength = s
        self.route = r
