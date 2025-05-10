porta =  int(input("Digite uma porta TCP: "))

#Portas válidas (conhecidas)
if porta >= 1 and porta <= 1024: 
     print("porta conhecida")
     print(porta, "É uma porta válida")
else:
     print("porta desconhecida")