from typing import List

def get_elf_with_maximum_calories(lines:List[str]) -> int:
    maximum_calories = 0
    current_calories = 0
    # Strips the newline character
    for line in lines:
        if line != '\n':
            current_calories = current_calories + int(line.strip())
        else:
            if current_calories > maximum_calories:
                maximum_calories = current_calories
            current_calories = 0
    return maximum_calories

def parse_str_list_to_integer_array(lines:List[str])->List[int]:
    int_list = []
    current_calories = 0
    for line in lines:
        if line != '\n':
            current_calories = current_calories + int(line.strip())
        else:
            int_list.append(current_calories)
            current_calories = 0
    return int_list

def get_top_n_elves_with_maximum_calories(input:List[str], n: int)->List[int]:
    int_list = parse_str_list_to_integer_array(input)
    int_list.sort(reverse=True)
    return sum(int_list[:n])



def main():
    input = open('1/input.txt', 'r')
    lines = input.readlines()
    print(f"Highest Calories carried by an Elf: {get_elf_with_maximum_calories(lines)}")
    n=3
    print(f"Sum of calories which the {n} Elves with the highest amount carrying in total {get_top_n_elves_with_maximum_calories(lines,n=n)}")

if __name__ == "__main__":
    main()