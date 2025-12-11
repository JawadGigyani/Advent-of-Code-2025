def max_joltage_12(bank: str) -> int:
    k = 12
    stack = []
    to_remove = len(bank) - k
    for digit in bank:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        if len(stack) < k:
            stack.append(digit)
        else:
            to_remove -= 1  # skip this digit if stack is already full
    return int(''.join(stack))

def main():
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                total += max_joltage_12(line)
    print(total)

if __name__ == "__main__":
    main()