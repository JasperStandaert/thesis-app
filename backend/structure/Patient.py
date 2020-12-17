class Patient:
    # Klasse van de patient
    # Bevat patient info en medicatie (druglijst)
    name = ""
    surname = ""
    age = ""
    condition = ""
    status = ""
    medication = []

    def __init__(self, n, s, a, c, stat, m):
        self.name = n
        self.surname = s
        self.age = a
        self.condition = c
        self.status = stat
        self.medication = m
