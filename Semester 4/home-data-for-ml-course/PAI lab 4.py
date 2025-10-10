def print_board(board, n):
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i] == j:
                row += "Q "
            else:
                row += ". "
        print(row)
    print("\n")


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)


def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)

    if len(solutions) == 0:
        print(f"No solution exists for {n}-Queens.\n")
    else:
        print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
        for sol in solutions:
            print_board(sol, n)


# Main loop
while True:
    user_input = input("Enter N for N-Queens (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("come back again Jal Ga")
        break

    if not user_input.isdigit():
        print("Please enter a valid number.\n")
        continue

    n = int(user_input)
    solve_n_queens(n)


