import random


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            player_input = input("Rock, Paper or Scissors? ")
            if player_input.lower() not in moves:
                print("Invalid move. Please try again!")
            else:
                return(player_input.lower())

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        self.move_temp = "rock"

    def move(self):
        return self.move_temp

    def learn(self, my_move, their_move):
        self.move_temp = their_move

class CyclePlayer(Player):
    def __init__(self):
        self.move_temp = "rock"
    def move(self):
        return { 
            "rock": "paper",
            "paper": "scissors", 
            "scissors": "rock", 
        }[self.move_temp]
    def learn(self, my_move, their_move):
        self.move_temp = my_move

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("- TIE -")
        elif beats(move1, move2) is True:
            print("- YOU WIN -")
            self.p1_score += 1
        elif beats(move2, move1) is True:
            print("- OPPONENT WINS -")
            self.p2_score += 1
        print(f"The score so far is {self.p1_score} to {self.p2_score}\n")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round+1}:")
            self.play_round()
        print("Game over!")
        print(f"Final score is {self.p1_score} to {self.p2_score}")
        if self.p1_score > self.p2_score:
            print("Congratulations you won!")
        elif self.p1_score < self.p2_score:
            print("You lose!")
        else:
            print("Tie!")


if __name__ == '__main__':
    moves = ['rock', 'paper', 'scissors']
    opponent_choice = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    opponent = int(input("\nChoose opponent: "
                         "\n 0 for RandomPlayer\n"
                         " 1 for ReflectPlayer\n"
                         " 2 for CyclePlayer\n"))
    if opponent in range(3):
        game = Game(HumanPlayer(), opponent_choice[opponent])
    game.play_game()
