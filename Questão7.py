# Solicita o número de switches na rede
num_switches = int(input("Quantos switches existem na rede? "))
total_portas_ocupadas = 0

for i in range(num_switches):
    portas_ocupadas = int(input(f"Quantas portas estão ocupadas no switch {i + 1}? "))
    total_portas_ocupadas += portas_ocupadas

print(f"Total de portas ocupadas na rede: {total_portas_ocupadas}")
