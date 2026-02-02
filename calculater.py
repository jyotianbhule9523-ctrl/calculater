"""history_file = "history.txt"

def show_history():
    file = open(history_file,'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("no history found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.closed()

def clear_history():
    file = open(history_file,'w')
    file.closed()
    print("cleared history")
def save_to_history(equationc, result):
    file = open(history_file,'a')
    file.write(equation = "=" + str(result) + "\n")
    file.closed()
def calculate(user_input):
    parts = user_input.split()
    if len(parts) !=3:
        print("invalid input use farmat :operator number")
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
            if num2 == 0:
                print('cannot be dividing  by 0')
                return
            result = num1 / num2
    else:
        print('invalid operator.use onle+-*/')
        return
    if int(result) == result:
        result = int(result)
    print("resut:", result)
    save_to_history(user_input, result) 
def main():
    print(' simple code for calculator')
    while True:
        user_input = input("enter calculation(+ - * /)or history clear command")
        if user_input =='exit' :
            print('goodbye')
            break
        elif user_input == 'history' :
            show_history()
        elif user_input == 'clear' :
            clear_history()
        else:
            calculate(user_input)
            main()"""


x = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

y = [[9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]]

# Matrix addition
add_res = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]

# Matrix subtraction
sub_res = [[x[i][j] - y[i][j] for j in range(len(x[0]))] for i in range(len(x))]


print("Matrix Addition:")
for row in add_res:
    print(row)

print("\nMatrix Subtraction:")
for row in sub_res:
    print(row)
    rows = int(input("rows: "))
col = int(input("columns: "))

matrix = [] 
print("entries row-wise:")

for i in range(rows):   
    row = []
    for j in range(col):
        row.append(int(input()))  
    matrix.append(row)  

print("\n2D matrix is:")

for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()


     
