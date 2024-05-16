

nombre1= int (input ("entrer un nombre"))
nombre2=int (input("enter un nombre "))
symbole=input("entrer le sympole")
reponse=nombre1+nombre2
match symbole:
        
    case "+":
            reponse=nombre1+nombre2
            print(reponse)
    case "*":
            reponse=nombre1*nombre2
            print(reponse)
    case "/":
            reponse=nombre1/nombre2
            print(reponse)  
    case "-":
            reponse=nombre1-nombre2
            print(reponse)   
    case _: 
            print("signe non reconnu")