import art
print(art.logo)
print('Welcome to the secret auction program.')
participants = {}

answer = 'yes'
while answer == 'yes':
    name = input('What is your name?: ')
    bid = int(input('What\'s your bid?: $'))
    participants[name] = bid
    answer = input('Are there any other bidders? Type \'yes\' or \'no\'.\n')
biggest_bid = 0
biggest_bid_person = ''
for name in participants:
    if participants[name] > biggest_bid:
        biggest_bid = participants[name]
        biggest_bid_person = name

print(f'The winner is {biggest_bid_person} with a bid of ${biggest_bid}.')