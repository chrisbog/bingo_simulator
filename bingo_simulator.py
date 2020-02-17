import random


class Bingo:
    '''
    This Class represents a bingo Class that will allow us to simulate bingo games
    '''


    card=[]

    # These masks represents the masks of a successful winning card.   1's represent the location should be matched
    coverall = [[1,1,1,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    stamps = [[1,1,0,1,1],[1,1,0,1,1],[0,0,0,0,0],[1,1,0,1,1],[1,1,0,1,1]]
    e = [[1,1,1,1,1],[1,0,1,0,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,1,0,1]]
    x = [[1,0,0,0,1],[0,1,0,1,0],[0,0,0,0,0],[0,1,0,1,0],[1,0,0,0,1]]


    def __init__(self):
        card=[]

    def generate_card(self):
        '''
        This function will generate a new random Bingo card.

        :return: None
        :rtype: None
        '''
        card_b = random.sample(range(1, 15), 5)
        card_i = random.sample(range(16, 30), 5)
        card_n = random.sample(range(31, 45), 4)
        card_n.insert(2, 0)
        card_g = random.sample(range(46, 60), 5)
        card_o = random.sample(range(61, 75), 5)

        self.card = [card_b,card_i,card_n,card_g,card_o]

    def __str__(self):
        '''
        This function will override the str function so that you can print out a bingo card in the proper format
        :return: Bingo card output
        :rtype: str
        '''

        out = "{:2}  {:2}  {:2}  {:2}  {:2}\n".format("B","I","N","G","O")
        for i in range(5):
            out += "{:2}  {:2}  {:2}  {:2}  {:2}\n".format(self.card[0][i], self.card[1][i],self.card[2][i],
                                                           self.card[3][i],self.card[4][i])
        return out

    def play_game(self,roles, type):
        '''

        :param roles: Represents the number of balls that will be drawn
        :type roles: int
        :param type: represents the type of game that should be chosen
        :type type: list type that represents the masks of the wining card
        :return: game_won - Boolean value to demo if the game_won,
                 num_found - Number of balls that were found in out card
                 num - Total number of wining balls on a successful card
        :rtype: Boolean, int, int
        '''

        wining_card = self.create_card_mask(type)

        num=0
        for i in range(5):
            for j in range(5):
                if (wining_card[i][j]>0):
                    num += 1

        #print(wining_card)
        selected = random.sample(range(1,75),roles)
        #print(selected)
        num_found = 0
        for i in selected:
            for count in range(5):
                if i in wining_card[count]:
                    #print("Found {:2}".format(i))
                    num_found += 1

        if num_found >= num:
            game_won= True
        else:
            game_won = False

        return game_won,num_found,num

    def create_card_mask(self,type):
        '''
        This function produces a simple mask for a successful card.   It basically multiplies the current bingo card
        with the game type mask.   This will then produce either a number or a 0 in each square.   If the square is a
        0 then we don't need that square to win.

        :param type: mask of the game we are playing
        :type type: list
        :return: winning_mask game board that should be matched
        :rtype: list
        '''
        winning_mask = [[ 0 for i in range(5)]for j in range(5)]
        for i in range(5):
            for j in range(5):
                winning_mask[i][j] = type[i][j]*self.card[i][j]
        return winning_mask


print("Welcome to a Simple Bingo Simulator")

print("Please select the type of bingo game you want to simulate:")
print("   1. Coverall")
print("   2. Stamps (or four corners")
print("   3. X pattern")
print("   4. E pattern\n")
good=False

while not good:
    game_type = input("Enter game type: ")

    if game_type not in ['1', '2', '3','4']:
        print("Invalid Entry.")
    else:
        good=True

total_simulations = int(input("Enter the total number of simulations: "))
drawn_numbers = int(input("Enter the total number of balls drawn: "))


won=0
for i in range(total_simulations):

    card = Bingo()
    card.generate_card()

    if game_type == '1':
        game = card.coverall
    elif game_type == '2':
        game = card.stamps
    elif game_type == '3':
        print (game_type)
        game = card.x
    elif game_type == '4':
        game = card.e

    success, num_found, total = card.play_game(drawn_numbers,game)

    if success:
        print("Game #{} Won: {}, {} out of {} numbers found.".format(i, str(success), num_found, total))
        won += 1

print("Total Games Won {} out of {} games.  The wining percentage {:6.2f}%".format(won,total_simulations,(won/total_simulations)*100))
