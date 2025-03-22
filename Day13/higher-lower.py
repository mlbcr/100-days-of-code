import random
from data import data
from art import logo

gameOn = True
pontos = 0
print(logo)

def game(pontuacao):
    print('--'*30)
    # Ver quantidade de pontos
    print(f'Pontos: {pontuacao}')

    # Sortear dois influenciadores aleatórios
    print("Choose the influencer that has more followers: ")
    influencer1 = influencer2 = []

    while influencer1 == influencer2:
        influencer1 = random.choice(data)
        influencer2 = random.choice(data)

    # Dizer para o jogador os influenciadores
    followers1 = influencer1['follower_count']
    followers2 = influencer2['follower_count']
    print(f"A: {influencer1['name']}, a {influencer1['description']}, from {influencer1['country']}.")
    print(f"B: {influencer2['name']}, a {influencer2['description']}, from {influencer2['country']}.")

    # Pedir para o jogador dizer se A ou B é maior
    if followers1 > followers2:
        maior = 'A'
    else:
        maior = 'B'

    palpite = input('\nA or B: ')
    if palpite == maior:
        print('Got it!')
    else:
        print(f'Sorry! You lost with {pontuacao} points!')
        global gameOn
        gameOn = False


while gameOn:
    game(pontos)
    pontos += 1
