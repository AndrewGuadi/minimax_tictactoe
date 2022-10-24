from cmath import inf
import random

class Board:

    possible_wins = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (7,5,3)]

    def __init__(self):
        self.moves = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
        self.current_player = self.player_turn(self.moves)



    def print_board(self):
        print(f"   {self.moves[1]}|  {self.moves[2]} | {self.moves[3]}\n____|____|____\n   {self.moves[4]}|  {self.moves[5]} | {self.moves[6]}\n____|____|____\n   {self.moves[7]}|  {self.moves[8]} | {self.moves[9]}\n    |    | \n\n\n")
    

    def player_make_move(self):
        
        while True:
            try:
                move = int(input("Make Move: "))
                if move in self.actions(self.moves):
                    self.moves[move] = self.current_player
                    break
            except (TypeError, ValueError):
                print("Please Pick A Valid Value")


    def computer_make_move(self):
        
        copy_state = {}
        for value in self.moves:
            copy_state[value] = self.moves[value]

        comp_move = (self.min_value(copy_state))[1]
        self.moves[comp_move] = self.player_turn(self.moves)
    
    def player_turn(self, state):
        
        current_player = None
        count = 0 
        for value in state:
            if state[value] in ["X", "O"]:
                count += 1
        if count % 2 == 0:
            return "X"
        elif count % 2 == 1:
            return "O"

    def actions(self, state):
        possible_moves = []
        for value in state:
            if type(state[value]) == int:
                possible_moves.append(state[value]) 
        return possible_moves


    def result(self, state, action):
        state[action] = self.player_turn(state)
        return state


    def terminal(self, state):
        players = ["X", "O"]
        if len(self.actions(state)) == 0:
            return True
        for player in players:
            for win in self.possible_wins:
                count = -3
                for number in win:
                    if number in [value for value in state if state[value] == player]:
                        count +=1
                if count >= 0:
                    return True

        return False

    def utility(self, state):
        players = ["X", "O"]
        for player in players:
            for win in self.possible_wins:
                count = -3
                for number in win:
                    if number in [value for value in state if state[value] == player]:
                        count +=1
                if count >= 0:
                    if player == "X":
                        return 1
                    elif player == "O":
                        return -1
        return 0


    def minimax(self, state):

        if self.player_turn(self.moves) == "X":
            print("I dont think it is supposed to be my turn")
            return random.choice(self.actions(self.moves))

        elif self.player_turn(self.moves) == "O":
            return self.min_value(state)[1]



    def max_value(self, state):

        if self.terminal(state):
            return [self.utility(state), None]
        v = -inf
        pos = None

        for action in self.actions(state):
            copy_state = {}
            for value in state:
                copy_state[value] = state[value]

            test = v
            v = max(v, self.min_value(self.result(copy_state, action))[0])

            if v > test:
                pos = action

        return [v, pos]

    def min_value(self, state):

        if self.terminal(state):
            return [self.utility(state), None]

        v = inf
        pos = None

        for action in self.actions(state):
            copy_state = {}
            for value in state:
                copy_state[value] = state[value]

            test = v
            v = min(v, self.max_value(self.result(copy_state, action))[0])

            if v < test:
                pos = action

        return [v, pos]

        





board = Board()
game_over = False
board.print_board()
while not game_over:

    board.player_make_move()
    game_over = board.terminal(board.moves)
    if game_over:
        break

    board.computer_make_move()
    board.print_board()
    game_over = board.terminal(board.moves)
