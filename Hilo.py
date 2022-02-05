
import random
class Card:

    def __init__(self):
        self.value = random.randint(1, 13)
        self.next_card = 0

    #def get_next_card(self):
        #new_card =  random.randint(1, 13)
        #self.next_card = new_card
    #Does the (1, 13) need to start (0, 12) or does the first option require starting at 0? A: keep as 1, 13 as it will only work for lists if laid out as (0, 12)

    #def get_current_card(self):
        #new_card =  random.randint(1, 13)
        #self.current_card = new_card

class Director:

    #random.seed(1)
    # [3 10, 13 13, 2 5, 2 8, 13 8, 8 11, 7 11, 4 2, 8 1]

    def __init__(self):
        self.score = 400
        self.user_guess = ""

    def start_game(self):
        replay = "y"
        while self.score > 0 and replay == "y":
            card = self.get_inputs()
            self.do_updates(card)
            self.do_outputs()
            if self.score <= 0:
                print("You Lose, Game Over")
            else:
                replay = input('Do you want to play again? (y/n): ')
                while replay not in ("y", "n"):
                    replay = input('Do you want to play again? (y/n): ')    
            #if elif statement to continue or end game.

    def get_inputs(self):
        current_card = Card()
        print(f"This card is: {current_card.value}")
        self.user_guess = input("Higher or lower? [h/l]: ")
        return current_card

    def do_updates(self, current_card):
        card = Card()
        print(f"Next card is: {card.value}")
        #print(f"{current_card.value}")
        if current_card.value > card.value and self.user_guess == "h":
            self.score -= 75
        elif current_card.value < card.value and self.user_guess == "l":
            self.score -= 75
        else:
            self.score += 100

    def do_outputs(self):
        print(f"Your score is: {self.score}")


def main():
    game = Director()
    game.start_game()

if __name__ == "__main__":
    main()
