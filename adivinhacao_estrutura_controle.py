import random

numero_sorteado = random.randint(1, 10) # Será escolhido um número de 1 a 10.
tentativas = 3 # Você possui 3 tentativas para acertar.

while tentativas > 0: # Equanto a tentativa for maior que 0
    palpite = int(input("Adivinhe um número de 1 a 10: ")) # você poderá dar um palpite para acertar.
    
    if palpite == numero_sorteado: # Se o palpite for o mesmo número sorteado.
        print("Parabéns, você acertou!") # Aparecerar "parabens, você acertou".
        break # Sistema para.
    elif palpite > numero_sorteado: # Se o palpite for maior do que o número sorteado.
        print("O número é menor.") # Aparecerar que o número sorteado é menor
    else: # caso o contrario.
        print("O número é maior.") # Aparecerar que o número sorteado é maior
    
    tentativas -= 1 # Todo vez que errar, perderá uma tentativa.

if tentativas == 0: # Se tiver 0 tentavivas restantes.
    print(f"Você perdeu! O número era {numero_sorteado}.") # Aparecerar que você perdeu e logo em seguida apresentará o número sorteado.