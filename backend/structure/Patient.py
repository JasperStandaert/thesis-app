class Patient:
    # Klasse van de patient
    # Bevat patient info en medicatie (druglijst)
    name = ""
    surname = ""
    age = 0
    condition = ""
    medication = []

    def __init__(self, n, s, a, c, m):
        self.name = n
        self.surname = s
        self.age = a
        self.condition = c
        self.medication = m
