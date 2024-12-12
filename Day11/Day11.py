def split_number(num):
    """Splits a number with an even number of digits into two halves."""
    num_str = str(num)
    mid = len(num_str) // 2
    left = int(num_str[:mid])
    right = int(num_str[mid:])
    return left, right

def simulate_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                left, right = split_number(stone)
                new_stones.extend([left, right])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)

# Load numbers from a text file
def load_stones_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        # Split the content into integers (assuming space or newline separation)
        stones = list(map(int, content.split()))
    return stones

# Main program
filename = "input.txt"  # Replace with the path to your file
initial_stones = load_stones_from_file(filename)

# Number of blinks
blinks = 75

# Calculate the number of stones after 25 blinks
result = simulate_stones(initial_stones, blinks)
print(f"Number of stones after {blinks} blinks: {result}")
