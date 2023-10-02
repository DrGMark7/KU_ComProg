# Shuffle a deck of cards using a Python random module
import random
from random import shuffle

# Define a class to create all type of cards
class Cards:
    global suites, values, SEP
    # 'diamonds (♦)', 'clubs (♣)', 'hearts (♥)', 'spades (♠)'
    suites = ['♥', '♦', '♣', '♠']
    values = ['A', '2', '3', '4', '5', '6', '7', '8']
    values += ['9', '10', 'J', 'Q', 'K']
    SEP = '-'
    def __init__(self):
        pass

# Define a class to categorize each card
class Deck(Cards):
    def __init__(self):
        super().__init__()
        self.mycardset = []
        for n in suites:
            for c in values:
                self.mycardset.append(c+ SEP +n)
    # Method to remove a card from the deck
    def popCard(self):
        if len(self.mycardset) == 0:
            return "NO CARDS CAN BE POPPED FURTHER"
        else:
            cardpopped = self.mycardset.pop()
            print("Card removed is", cardpopped)

# Define a class gto shuffle the deck of cards
class ShuffleCards(Deck):
  # Constructor
    def __init__(self):
        super().__init__()
    # Method to shuffle cards
    def shuffle(self, seed=0):
        '''use integer seed != 0 to generate the same random number'''
        if seed != 0:
            random.seed(seed)
        shuffle(self.mycardset)
        return self.mycardset
    # Method to remove a card from the deck
    def popCard(self):
        if len(self.mycardset) == 0:
            return "NO CARDS CAN BE POPPED FURTHER"
        else:
            cardpopped = self.mycardset.pop()
            return (cardpopped)


# student code, ie. Game class, below this line
###---------------------------- BEGIN Student work ----------------------------

class Game(ShuffleCards):
    def __init__(self) -> None:
        super().__init__()   #* Genarate many key on class Player
        self.Player = self.Player  
        pass

    class Player:
        def __init__(self,name) -> None:
            self.name = name
            self.myCards = []
            self.score = 0
        
        def calculate_score(self):
            hands = self.myCards
            score, A_count = 0, 0
            normal_values, face_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10'], ['J', 'Q', 'K', 'A']

            for card in hands:
                key, label = card.split("-")
                
                if key in normal_values:
                    score += int(key)
                elif key in face_values[:3]:  # J, Q, K
                    score += 10
                elif key == face_values[-1]:  # Ace (A)
                    score += 11
                    A_count += 1
            
            while A_count > 0 and score > 21:
                score -= 10
                A_count -= 1

            self.score = score
            return self.score

        def get_myCards(self):
            return self.myCards
        
        def add_myCards(self,card):
            self.myCards.append(card)

        def get_displays(self):
            return f" {self.name}: {', '.join(self.myCards)}, ({self.score()}) "
        
    
    def play_game(self,seed=0):

        #* Step 1 Ready Process to play

        Player_name = str(input("Player1 name: "))
        print("Welcome to Simple BackJack.. ©2023 MikeLab.Net")

        #* Step 2 Make Object in Game
        ObjDeck = ShuffleCards()
        ObjDeck.shuffle(seed=seed)
        User , Bot = self.Player(Player_name),self.Player("Computer")

        #* Step 3 Start First Game

        for _ in range(2):
            User.add_myCards(ObjDeck.popCard())
            Bot.add_myCards(ObjDeck.popCard())

        print(f"   {Player_name}: {', '.join(User.get_myCards())}, ({User.calculate_score()})  Computer: {', '.join(Bot.get_myCards())}, ({Bot.calculate_score()})")

        #* Step 4 User Rounddd

        while True:  
            if User.calculate_score() <= 21:
                Answer = input(f"{Player_name}, would you (H)it or (S)tand..? ").lower()
                if Answer == "h":
                    User.add_myCards(ObjDeck.popCard())
                    print(f"   {Player_name}: {', '.join(User.get_myCards())}, ({User.calculate_score()})  Computer: {', '.join(Bot.get_myCards())}, ({Bot.calculate_score()})")
                else:
                    break
            else:
                break

        #* Step 5 Today it's AI turn
        print("Now, it is my turn..")

        while True:
            print(f"   {Player_name}: {', '.join(User.get_myCards())}, ({User.calculate_score()})  Computer: {', '.join(Bot.get_myCards())}, ({Bot.calculate_score()})")

            #* Step 5.1 Analyze the results of the game.
            if User.calculate_score() > 21 or (Bot.calculate_score() == User.calculate_score()):
                break
            
            if Bot.calculate_score() > User.calculate_score():
                break
            elif Bot.calculate_score() < 21 :
                Bot.add_myCards(ObjDeck.popCard())
            else:
                break

        #* Step 6 Arbitrate Game !!
        print("Who wins?")

        print(f"   {Player_name}: {', '.join(User.get_myCards())}, ({User.calculate_score()})  Computer: {', '.join(Bot.get_myCards())}, ({Bot.calculate_score()})")
        
        score_user , score_bot = User.calculate_score() , Bot.calculate_score()

        if score_user > 21:
            print("[Computer] wins this round")
        elif score_bot > 21:
            print(f" {Player_name} wins this round")
        elif score_bot > score_user:
            print(f"[Computer] wins this round")
        elif score_user > score_bot:
            print(f" {Player_name} wins this round")
        else:
            print("DRAW..")

            
###---------------------------- END Student work ----------------------------

##### main driver code for the above student work, ie. Game class.
while True:
    doc = '''Just press ENTER to let the card deck be shuffled
randomly, or any integer N to run random.seed(N)
with the same shuffle pattern, or (q)uit!'''
    #print('X'*50)
    print(doc, end='')
    intSeed = input(': ')
    #print('X'*50)
    if intSeed.upper()=='Q':
        print('Bye.')
        break
    try:
        if intSeed=='':
            g = Game()
            g.play_game()
        else:
            g = Game()
            g.play_game(int(intSeed))
    except ValueError:
        print(f'ERROR: You entered a wrong input: [{intSeed}]!!')

