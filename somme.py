class somme:
    def __init__(self,note1,note2):
        self.note1=note1
        self.note2=note2
    def som(self,note1,note2):
        resultat = note1 + note2
        return resultat
nomb_ut1 = int(input("entrer le nombre 1 "))
nomb_ut2 = int(input("entrer le nombre 2 "))

som1= somme( nomb_ut1 , nomb_ut2 )

print(f"la somme de {nomb_ut1} et {nomb_ut2} = {som1.som(nomb_ut1,nomb_ut2)}" )