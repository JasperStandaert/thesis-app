class Drug:

    name = ""
    description = ""
    indication = ""
    toxicity = ""
    interactions = []
    products = []

    #def __init__(self, n, d, i, t, inter, p):
    #    self.name = n
    #    self.description = d
    #    self.indication = i
    #    self.toxicity = t
    #    self.interactions = inter
    #    self.products = p

    def __init__(self, druginfo):
        self.name = druginfo[0]
        self.description = druginfo[1]
        self.indication = druginfo[2]
        self.toxicity = druginfo[3]
        self.interactions = druginfo[4]
        self.products = druginfo[5]
