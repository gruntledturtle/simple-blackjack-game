import random


class Player:
    card_total = 0
    hand = []
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,]
    computer_cards = [16, 17, 17, 18, 19, 20, 21, 22]
    game = True
    done = 0
    computer_card_total = 0
    money = 100

def loose():
    Player.money -= 25
    main_menu()

def win():
    Player.money += 50
    main_menu()

def draw():
    main_menu()

def main_menu():
    print("==============")
    print("| Money: "+str(Player.money)+" |")
    print("==============")

    if Player.money <= 0:
        print("Game Over!")
        exit(0)
    new_game = input('\n$25 bets\nNew Game (Y/n): ').lower()
    if new_game == 'n':
        exit(0)
    game()

def sit():
    print("Sitting on :" + str(Player.card_total))
    Player.computer_card_total += random.choice(Player.computer_cards)
    input("Computer got: " + str(Player.computer_card_total))
    if Player.computer_card_total == Player.card_total:
        print("Its a draw")
        main_menu()
    if Player.computer_card_total == 22:
        print("You win")
        win()
    if Player.computer_card_total > Player.card_total:
        if Player.computer_card_total != 22:
            print("you loose")
            loose()
    else:
        print("you win")
        win()

def game():
    while Player.game:
        if Player.done > 1:
            break
        Player.card_total = 0
        Player.hand = []
        Player.computer_card_total = 0
        c1 = random.choice(Player.cards)
        c2 = random.choice(Player.cards)
        Player.hand.append(c1)
        Player.hand.append(c2)
        Player.card_total += c1 + c2
        print("\n\n\n\n")
        print(Player.hand)
        print("Total: " + str(Player.card_total))
        first_hand = input("hit (Y/n)").lower()
        if first_hand == "y":
            c3 = random.choice(Player.cards)
            Player.card_total += c3
            print("\n")
            print("|" + str(c3) + "|")
            print("\n")
            if Player.card_total > 21:
                print(Player.hand)
                print("Total: " + str(Player.card_total))
                print("BUST")
                loose()
            print(Player.hand)
            print("Total: " + str(Player.card_total))
            second_hand = input("\nhit (Y/n)").lower()
            if second_hand == "y":
                c4 = random.choice(Player.cards)
                Player.card_total += c4
                print("\n")
                print("|" + str(c3) + "|" + str(c4) + "|")
                print("\n")
                if Player.card_total > 21:
                    print(Player.hand)
                    print("Total: " + str(Player.card_total))
                    print("BUST")
                    loose()
                print(Player.hand)
                print("Total: " + str(Player.card_total))
                third_hand = input("\nhit (Y/n)").lower()
                if third_hand == "y":
                    c5 = random.choice(Player.cards)
                    Player.card_total += c5
                    print("\n")
                    print("|" + str(c3) + "|" + str(c4) + "|" + str(c5) + "|")
                    print("\n")
                    if Player.card_total > 21:
                        print(Player.hand)
                        print("Total: " + str(Player.card_total))
                        print("BUST")
                        loose()
                    print(Player.hand)
                    print("Total: " + str(Player.card_total))
                    fourth_hand = input("\nhit (Y/n)").lower()
                    if fourth_hand == "y":
                        c6 = random.choice(Player.cards)
                        Player.card_total += c5
                        print("\n")
                        print("|" + str(c3) + "|" + str(c4) + "|" + str(c5) + "|" + str(c6) + "|")
                        print("\n")
                        if Player.card_total > 21:
                            print(Player.hand)
                            print("Total: " + str(Player.card_total))
                            print("BUST")
                            loose()
                        else:
                            print(Player.hand)
                            print("Total: " + str(Player.card_total))
                            print("You win!")
                            win()
                    else:
                        sit()
                else:
                    sit()
            else:
                sit()
        else:
            sit()


main_menu()
