# Import da biblioteca de randomização
import random

# Definindo o limite que o rand irá
num_a = random.randint(0,5)

# Recebendo o numero do usuario
aux = int(input("adivinhe o numero de 0 a 5: "))

# Logica para comparar o numero inserido e o gerado pelo RAND
if (num_a == aux):
    print ("acertou!")
else : (print("errou!"))

#confirmando o numero que foi gerado RAND
print("o numero era: ", num_a)
