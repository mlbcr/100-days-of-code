import random
import content

word_list = content.words
lives = 6

print(content.logo)
random_word = random.choice(word_list)
print(f'Pssst, the solution is {random_word}.')

answer = list(random_word)
display = []
new_display = []

for _ in range(len(answer)):
    display.append('_')
print(display)

while display != answer:
    guess = input('Guess a letter: ').lower()
    new_display = display
    for position in range(len(answer)):
        letter = answer[position]
        if guess == letter:
            display[position] = letter
    if guess not in answer:
        print(f'{guess} is not in the word')
        lives -= 1
    print(content.stages[lives])
    if lives == 0:
        print('You lose.')
        break
    print(display)
if display == answer:
    print('You win!')