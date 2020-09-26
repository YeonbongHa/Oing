import random
card = ["Grape5", "Green Grape5", "Strawberry5", "Banana5", "Grape4", "Green Grape4", "Strawberry4", "Banana4", "Grape4", "Green Grape4", "Strawberry4", "Banana4", "Grape3", "Green Grape3", "Strawberry3", "Banana3", "Grape3", "Green Grape3", "Strawberry3", "Banana3", "Grape3", "Green Grape3", "Strawberry3", "Banana3", "Grape2", "Green Grape2", "Strawberry2", "Banana2", "Grape2", "Green Grape2", "Strawberry2", "Banana2", "Grape2", "Green Grape2", "Strawberry2", "Banana2", "Grape1", "Green Grape1", "Strawberry1", "Banana1", "Grape1", "Green Grape1", "Strawberry1", "Banana1", "Grape1", "Green Grape1", "Strawberry1", "Banana1", "Grape1", "Green Grape1", "Strawberry1", "Banana1", "Grape1", "Green Grape1", "Strawberry1", "Banana1"]
random.shuffle(card)
print(len(card))
computer_deck = []
computer_playing_deck = []
my_playing_deck = []
my_deck = []
put_computer =[]
put_my_deck = []
for i in range(0, 28):
    computer_deck.append(card.pop())
    my_deck.append(card.pop())
print(len(computer_deck))
while True:


    for letter in computer_deck[-1]:

        if letter.isdigit():

            x = int(letter)
    for letters in my_deck[-1]:
        if letters.isdigit():
            y = int(letters)

    sum = x + y

    answer = input("So the sum of the the cards is "+str(sum)+"!! Ring the Bell!! Press Y/N").upper()


    if answer == 'Y' and sum == 5:
        computer_playing_deck.append(computer_deck[-1])
        computer_deck.remove(computer_deck[-1])
        my_playing_deck.append(my_deck[-1])
        my_deck.remove(my_deck[-1])

        print("Oh You won!! You take all cards of computer's playing deck!!")
        put_my_deck.extend(my_playing_deck)
        put_my_deck.extend(computer_playing_deck)
        my_playing_deck.clear()
        computer_playing_deck.clear()

    elif answer == 'Y' and sum != 5:
        computer_playing_deck.append(computer_deck[-1])
        computer_deck.remove(computer_deck[-1])
        my_playing_deck.append(my_deck[-1])
        my_deck.remove(my_deck[-1])
        print("Oh You lost!! Computer takes all cards of your playing deck!!")
        put_computer.extend(computer_playing_deck)
        put_computer.extend(my_playing_deck)
        my_playing_deck.clear()
        computer_playing_deck.clear()

    elif answer == 'N' and sum == 5:
        computer_playing_deck.append(computer_deck[-1])
        computer_deck.remove(computer_deck[-1])
        my_playing_deck.append(my_deck[-1])
        my_deck.remove(my_deck[-1])
        print("Oh You lost!! Computer takes all cards of your playing deck!!")
        put_computer.extend(my_playing_deck)
        put_computer.extend(computer_playing_deck)
        my_playing_deck.clear()

    elif answer == 'N' and sum !=5:
        computer_playing_deck.append(computer_deck[-1])
        computer_deck.remove(computer_deck[-1])
        my_playing_deck.append(my_deck[-1])
        my_deck.remove(my_deck[-1])
    else:
        print("please state Y/N")
    if len(my_deck) == 0 or len(computer_deck) == 0:
        break
put_computer.extend(computer_playing_deck)
put_computer.extend(computer_deck)
put_my_deck.extend(my_playing_deck)
put_my_deck.extend(my_deck)
print(len(put_computer),len(put_my_deck))
if len(put_my_deck) > len(put_computer):
    print("Oh You won!!")
elif len(put_computer) > len(put_my_deck):
    print("OH poor you!! Computer won this game!!")
print(card)



#Computer starts first



