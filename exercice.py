class etudiant:
    def __init__(self,nom,note1,note2):
        self.nom=nom
        self.note1=note1
        self.note2=note2

    def calcul_moyen(self,nom,note1,note2):
        self.note1=note1
        self.note2=note2
        note = [note1,note2]
        somme = sum(note)
        moyenne=somme/2
        return moyenne
    def AffNomMoyenne(self,nom,moyenne):
        self.nom=nom
        self.moyenne=moyenne
        AffNomMoyenne=f"l'etudiant {nom} a eu comme Moyenne {moyenne}"
        print(AffNomMoyenne)

nom= input("entrer le nom de l'etudiant ")
note1= float(input("entrer la note 1 "))
note2= float(input("entrer la note 2 "))

moyenne = etudiant(nom,note1,note2)
moyenne_calcul = moyenne.calcul_moyen(nom,note1,note2)

affiche = etudiant(nom,note1,note2)
affiche.AffNomMoyenne(nom,moyenne_calcul)
