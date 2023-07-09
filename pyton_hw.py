import random


def play_coin_flip():
    player_wins = 0
    player_losses = 0

    while True:
        player_choice = input("Виберіть Орел (O) або Решка (Р), або натисніть (X) щоб завершити гру: ")
        player_choice = player_choice.upper()

        if player_choice == 'X':
            break

        while player_choice not in ['O', 'P']:
            player_choice = input("Виберіть Орел (O) або Решка (Р), або натисніть (X) щоб завершити гру: ")
            player_choice = player_choice.upper()

        if player_choice == 'O':
            player_choice_name = 'Орел'
        else:
            player_choice_name = 'Решка'

        options = ['O', 'P']
        computer_choice = random.choice(options)

        if computer_choice == 'O':
            computer_choice_name = 'Орел'
        else:
            computer_choice_name = 'Решка'

        print("Ваш вибір:", player_choice_name)
        print("Вибір комп'ютера:", computer_choice_name)

        if player_choice == computer_choice:
            print("Ви виграли!")
            player_wins += 1
        else:
            print("Ви програли!")
            player_losses += 1

        print("Кількість виграних ігор:", player_wins)
        print("Кількість програних ігор:", player_losses)
        print("---------------------")


play_coin_flip()