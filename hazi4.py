class Team:
    def __init__(self, name, project, position):
        self.name = name
        self.project = project
        self.position = position
        print(self)

    def __str__(self):
        return f"-- Developer létrehozva. --\n{self.name} a {self.project}-en dolgozik {self.position} szerepkörben."

workers = []

workers.append(Team("Ricsi", "SolArch", "Frontend"))
workers.append(Team("Angéla", "ZerTeng", "Tesztelő"))
workers.append(Team("Peti", "KefERP", "Backend"))
workers.append(Team("Éva", "KefERP", "Frontend"))

for x in workers:
    for y in workers:
        if x.project == y.project:
            if x.name > y.name and x.name != y.name:
                print(f"\n{x.name} és {y.name} dolgoznak egy projekten.")