from time import sleep
delay = 1
print('Welcome agent...')
sleep(delay)
print('Before we get started, we need you to fill out the following information...')
sleep(delay)
first = input('What is your first name? ')
last = input('What is your last name? ')
sleep(delay)
print(f'I see... So your name is, {first.capitalize()} {last.capitalize()}...')
sleep(delay)
print(f'Well, agent {last}. Now that that is out of the way, your first step to becoming a cool spy has begun...')
sleep(delay)
print(f'From now on agent when you do somethnig cool, and someone ask your name make sure you say...')
sleep(delay)
print(f'The name is {last.capitalize()}, {first.capitalize()} {last.capitalize()}!')
