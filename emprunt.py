def main(*args, **kwargs):

    print('\n')

    montant_emprunt = input("Montant de l'emprunt (en kilo euros): ")
    montant_emprunt = float(montant_emprunt) * 1e3

    taux =            input("Taux annuel (en pourcents):           ")
    taux = float(taux) / 12 / 100

    n_mois =          input("Duree du pret (en annees):            ")
    n_mois = float(n_mois) * 12

    emprunt_bancaire = EmpruntBancaire(montant_emprunt, taux, n_mois)

    emprunt_bancaire.calcul_tout()

    print('\n')
    a = int(emprunt_bancaire.mensualite)
    b = int(emprunt_bancaire.montant_total_rembourse)
    c = int(emprunt_bancaire.cout_emprunt)
    d = int(emprunt_bancaire.cout_emprunt_mensuel)
    print("Mensualite:                " + str(a))
    print("Montant total rembourse:   " + str(b))
    print("Cout total de l'emprunt:   " + str(c))
    print("Cout mensuel de l'emprunt: " + str(d))
    print('\n')

class EmpruntBancaire():

    def __init__(self, montant_emprunt, taux, n_mois):
        self.montant_emprunt = montant_emprunt
        self.taux = taux
        self.n_mois = n_mois

    def calcul_tout(self):
        self.calcul_mensualite()
        self.calcul_montant_total_rembourse()
        self.calcul_cout_emprunt()

    def calcul_mensualite(self):
        alpha = 1 / (1 - (1 + self.taux)**(-self.n_mois))
        self.mensualite = self.montant_emprunt * self.taux * alpha

    def calcul_montant_total_rembourse(self):
        self.montant_total_rembourse = self.mensualite * self.n_mois

    def calcul_cout_emprunt(self, total_et_mensuel=True):
        self.cout_emprunt = self.montant_total_rembourse - self.montant_emprunt
        if(total_et_mensuel):
            self.cout_emprunt_mensuel = self.cout_emprunt / self.n_mois


if __name__ == '__main__':
    main()
