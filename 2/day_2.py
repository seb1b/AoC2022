from typing import List
from collections import defaultdict

ROCK = 1 
PAPER = 2
SCISSOR = 3

WIN = 6
DRAW = 3
LOSE = 0

game_mapping = defaultdict(dict)
game_mapping2 = defaultdict(dict)

#ROCK
game_mapping['A']['X']=ROCK+DRAW #rock
game_mapping['A']['Y']=PAPER+WIN #paper
game_mapping['A']['Z']=SCISSOR+LOSE #scissor SCISSOR
#PAPER
game_mapping['B']['X']=ROCK+LOSE #rock
game_mapping['B']['Y']=PAPER+DRAW #paper
game_mapping['B']['Z']=SCISSOR+WIN #scissor
#SCISSOR
game_mapping['C']['X']=ROCK+WIN #rock
game_mapping['C']['Y']=PAPER+LOSE #paper
game_mapping['C']['Z']=SCISSOR+DRAW #siccor


# X lose, Y draw, Z  win
#rock
game_mapping2['A']['X']=SCISSOR+LOSE 
game_mapping2['A']['Y']=ROCK+DRAW 
game_mapping2['A']['Z']=PAPER+WIN 
#paper
game_mapping2['B']['X']=ROCK+LOSE 
game_mapping2['B']['Y']=PAPER+DRAW
game_mapping2['B']['Z']=SCISSOR+WIN
#siccsor
game_mapping2['C']['X']=PAPER+LOSE 
game_mapping2['C']['Y']=SCISSOR+DRAW
game_mapping2['C']['Z']=ROCK+WIN


def calculate_total_score(input_lines:List[str])->int:
    total_sum = 0
    for line in input_lines:
        game = line.split()
        total_sum += game_mapping[game[0]][game[1]]
    return total_sum

def calculate_optimized_strategy(input_lines:List[str])->int:
    total_sum = 0
    for line in input_lines:
        game = line.split()
        total_sum += game_mapping2[game[0]][game[1]]
    return total_sum

def main():
    input = open('2/input.txt', 'r')
    lines = input.readlines()
    sum = calculate_total_score(lines)
    print(f"Total Won {sum}.")
    print(f"Total Won with Opt Strategy {calculate_optimized_strategy(lines)}.")

if __name__ == "__main__":
    main()