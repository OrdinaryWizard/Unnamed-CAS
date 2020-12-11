alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
operator = ['+', '-', '*', '/', '=']

print("OrdinaryCAS beta\nOther features coming soon")

         
#expression lexer function
def lexer(input_str):
    input_str = input_str + " "
    out_char = ""
    expression = []
    tokens = []

    for x in range(len(input_str)):
        char = input_str[x]
        if char.isalpha():
            out_char = out_char+char

        elif char.isdigit():
            out_char = out_char+char

        elif char == "+" or char == "-" or char == "*" or char == "/" or char == "^" or char == "=":
            expression.append(out_char)
            out_char = ""
            out_char = out_char+char
            expression.append(out_char)
            out_char=""
        
        elif char.isspace():
            expression.append(out_char)
            out_char = ""

        



    return expression


#solver function
def solve(string):
    input_expr = string
    limit = int(input("limit: "))
    try:
        expr = input_expr.split("=")
    except IndexError:
        print("input must be an equation. expressions will raise an error")
        input_expr = input_expr + "=0"
        expr = input_expr.split("=")
    
    side_one = []
    side_two = []
    for x in range(-(limit), limit):
        coor_one = []
        coor_two = []

        coor_one.append(x)
        coor_one.append(eval(expr[0]))

        coor_two.append(x)
        coor_two.append(eval(expr[1]))

        side_one.append(coor_one)
        side_two.append(coor_two)

    sol = []
    for i in range(len(side_one)):
        if side_one[i] == side_two[i]:
            sol.append(side_one[i][0])
    
    return sol


#function that converts mathematically natural language to computer understandable text
def naturalise(input_str):
    output = input_str
    output_string = ""
    for x in range(len(output)):
        element = output[x]
        for i in range(len(element)):
            char = element[i]
            if char in alpha and element[i-1] not in number:
                output_string = output_string + "x"

            if char in alpha and element[i-1] in number:
                output_string = output_string + "*x"
            
            if char in number:
                output_string = output_string + char

            if char in operator:
                output_string = output_string + char

            if char == "^":
                output_string = output_string + "**"
    
    return output_string
