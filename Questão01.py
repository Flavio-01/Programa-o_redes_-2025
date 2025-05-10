#Velocidade do Download
while True:

    velocidade = int(input("Digite a velocidade Mbps: ")) 
    if velocidade <10:
         print("Velocidade lenta")
    elif velocidade >= 10 and  velocidade <= 100:
         print("Velocidade Normal")
    else: 
        print("Velocidade Rapida")