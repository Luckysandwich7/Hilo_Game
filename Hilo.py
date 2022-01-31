
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

    def __init__(self):
        self.score = 400
        self.user_guess = ""

    def start_game(self):
        while self.score >= 0:
            card = self.get_inputs()
            self.do_updates(card)
            self.do_outputs()
            print('Do you want to play again? (y/n): ')
            #if elif statement to continue or end game.

    def get_inputs(self):
        current_card = Card()
        print("This card is: {}".format(str(current_card.value)))
        #print("This card is:  {current_card.value} ")
        self.user_guess = input("Higher or lower? [h/l]: ")
        return current_card

    def do_updates(self, current_card):
        card = Card()
        print('Next card is: {}'.format(str(current_card.value)):)
        if current_card.value > card.value and self.user_guess == "h":
            self.score += 100
        else:
            self.score -= 75

    def do_outputs(self):
        print(f"Your score is: {self.score}")

    #Need to create if score = 0 to end game.


def main():
    game = Director()
    game.start_game()

if __name__ == "__main__":
    main()
