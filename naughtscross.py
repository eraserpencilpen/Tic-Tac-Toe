
import random

grid = {
    "tl": "tl", "tm": "tm", "tr": "tr",
    "ml": "ml", "mm": "mm", "mr": "mr",
    "bl": "bl", "bm": "bm", "br": "br"
}



def win():
    if (grid["tl"] == grid["tm"] == grid["tr"]) or (grid["ml"] == grid["mm"] == grid["mr"]) or (
            grid["bl"] == grid["bm"] == grid["br"]) or (grid["tl"] == grid["ml"] == grid["bl"]) or (
            grid["tm"] == grid["mm"] == grid["bm"]) or (grid["tr"] == grid["mr"] == grid["br"]) or (
            grid["tl"] == grid["mm"] == grid["br"]) or (grid["tr"] == grid["mm"] == grid["bl"]):
        return True
    return False


def PrintGrid():
    print(f'''
    {grid["tl"]} | {grid["tm"]} | {grid["tr"]}   
    ---+----+----
    {grid["ml"]} | {grid["mm"]} | {grid["mr"]}
    ---+----+----
    {grid["bl"]} | {grid["bm"]} | {grid["br"]}
    ''')


def PlayerInput(char,p=""):
    print(f"Player{p}")
    global player
    player = input()
    while player not in grid or not grid[player].isalpha():
        print("Try Again")
        player = input()
    grid[player] = char
    PrintGrid()


def AddLastPlace(Char):
    v = ["O", "X"]
    if Char == "X":
        v = ["X", "O"]

    for char in v:
        values = {
            "top": ["tl", "tm", "tr"],
            "middle": ["ml", "mm", "mr"],
            "bottom": ["bl", "bm", "br"],
            "left": ["tl", "ml", "bl"],
            "Middle": ["tm", "mm", "bm"],
            "right": ["tr", "mr", "br"],
            "diagonal1": ["tl", "mm", "br"],
            "diagonal2": ["tr", "mm", "bl"]
        }
        # adds grid information to values dictionary
        for i in grid:
            if grid[i] == char:
                for j in values:
                    if i in values[j]:
                        values[j].remove(i)
        # Makes and randomizes a list of possible inputs 
        possible = []
        for a in values:
            if len(values[a]) == 1:
                possible.append(values[a][0])

        # Placing the value
        for x in possible:
            if grid[x] != "O" and grid[x] != "X":
                grid[x] = Char
                PrintGrid()
                return True
    raise Exception("There are no last places.")



###############
# Actual Game #  
###############
print("Naughts and Crosses!")


choice = ""
while choice != "T" or choice != "O":
    Pone = ""
    Ptwo = ""
    moves = 0
    
    Choice = ""
    Moves = 0
    print("Two Players or One?(T/O): ")
    choice = input()
    if choice == "T":
        PrintGrid()
        while True:
            PlayerInput("O","1")
            moves += 1
            
            if win():
                print("Player one has won!")
                break
            elif moves >= 9:
                print("Draw")
                break
            PlayerInput("X","2")
            moves += 1
            
            if win():
                print("Player two has won!")
                break
            elif moves >= 9:
                print("Draw")
                break
    else:
        grid = {
            "tl": "tl", "tm": "tm", "tr": "tr",
            "ml": "ml", "mm": "mm", "mr": "mr",
            "bl": "bl", "bm": "bm", "br": "br"
        }
        CORNERS = ["tl","tr","bl","br"]
        EDGES = ["tm", "ml", "mr", "bm"]
        MMcorners = {"tl": "br", "br": "tl", "tr": "bl", "bl": "tr"}
        CEedges = {"tm":"bm","ml":"mr","mr":"ml","bm":"tms"}

        while Choice != "y" and Choice != "n":
            print("Player goes first?(Y/N): ")
            Choice = input().lower()

        MOVES = []
        if Choice == "y":
            
            PrintGrid()
            PlayerInput("O")
            MOVES.append(player)
            if player in CORNERS or player in EDGES:
                grid["mm"] = "X"
                PrintGrid()

                
                PlayerInput("O")
                MOVES.append(player)
                
                print(MOVES[-1][0] == MOVES[-2][0])
                print(MOVES[-1][1] == MOVES[-2][1])
                # PERFECT GAME
                if MOVES[-2] in MMcorners and MMcorners[MOVES[-2]] == MOVES[-1]:
                    print(MOVES[-2],MMcorners[MOVES[-2]])
                    grid[random.choice(EDGES)] = "X"
                    PrintGrid()
                    moves = 0
                    while True:
                        PlayerInput("O")
                        moves += 1
                        if moves >= 5:
                            break
                        AddLastPlace("X")
                        moves += 1
                        if win() or moves >= 5:
                            break


                # SAME ROW OR COLUMN

                ##################
                # TESTING NEEDED #
                ##################
                # elif MOVES[-1][0] == MOVES[-2][0] or MOVES[-1][1] == MOVES[-1][1]:
                elif False or False:
                    print("why bro")
                    AddLastPlace("X")
                    
                    PlayerInput("O")
                    try:
                         AddLastPlace("X")
                    except Exception:
                        grid[random.choice([i for i in grid if grid[i] != "O" and grid[i] != "X" ])] = "X"
                        PrintGrid()

                        PlayerInput("O")
                        
                        AddLastPlace("X")

                        PlayerInput("O")
                        for i in grid:
                            if grid[i] != "O" and grid[i] != "X":
                                grid[i] = "X"

                else:
                    EdgePossible = EDGES.copy()
                    EdgePossible.remove(player)
                    EdgePossible.remove(CEedges[player])
                    grid[random.choices(EdgePossible)] = "X"
                    PrintGrid()

                    PlayerInput("O")

            elif player in EDGES:
                grid["mm"] = "X"

                
        elif Choice == "n":

            m1 = random.choice(CORNERS)
            grid[m1] = "O"
            MOVES.append(m1)
            PrintGrid()


            PlayerInput("X")

            # THIS WAS NOT HERE BEFORE
            MOVES.append(player) 

            # Places at Middle Game
            if player == "mm":
                
                grid[MMcorners[MOVES[-2]]] = "O" # Initially MOVES[-1]
                PrintGrid()
                moves = 0
                while not win() or moves >= 7:
                     
                    PlayerInput("X")

                    AddLastPlace("O")

            # CORNERS GAME
            # VERY FUN
            elif player in CORNERS:
                Cpossible = CORNERS.copy()
                for i in MOVES:
                    if i in Cpossible:
                        Cpossible.remove(i)

                move = random.choice(Cpossible)
                grid[move] = "O"
                PrintGrid()

                Cpossible.remove(move)

                 
                PlayerInput("X")

                try:
                    AddLastPlace("O")
                except Exception:
                    grid[Cpossible[0]] = "O"
                    PrintGrid()
                    while not win():
                        PlayerInput("X")
                        AddLastPlace("O")

            # Next to and Same Row
            elif player[0] == MOVES[-2][0] and player in EDGES:
                NRcorners = {"tl":["bl","br"],"tr":["br","bl"],"bl":["tl","tr"],"br":["tr","tl"]}
                grid[NRcorners[MOVES[-2]][0]] = "O"
                PrintGrid()

                 
                PlayerInput("X")
                PrintGrid()

                try:
                    AddLastPlace("O")
                except Exception:
                    grid[random.choice(["mm",NRcorners[MOVES[-1]][1]])] = "O"
                    PrintGrid()

                    PlayerInput("X")

                    AddLastPlace("O")

            # ONE MORE CONDITION TO WRITE HERE
            # ON TOP OF SAME COLUMN
            else:
                TCcorners = {"tl":["tr","br"],"tr":["tl","bl"],"br":["bl","tl"],"bl":["br","tr"]}
                grid[TCcorners[player][0]] = "O"
                PrintGrid()

                PlayerInput("X")
                try:
                    AddLastPlace("O")
                except Exception:
                    grid[TCcorners[player][1]] = "O"
                    PrintGrid()
                    PlayerInput("X")
                    AddLastPlace("O")


    print("Play again?")
    print("Press Ctrl+C to quit")
    input()
