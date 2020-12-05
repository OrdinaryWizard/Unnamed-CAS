while True:
    input_expr = input("\n[in]: ")
    limit = int(input("limit: "))
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
    
    print("[out]: "+str(sol))
        
    
