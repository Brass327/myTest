P1wins = 0
P2wins = 0
Draws = 0
while True:
    while True:
        P1choice = input("\nPlayer 1, please choose rock(r), paper(p), or scissors(s): ")
        if P1choice == "r" or P1choice == "p" or P1choice == "s":
            print("\nChoice confirmed.")
            break
        else:
            print("\nThat is not a valid selection. Please enter 'r', 'p', or 's'.")
    while True:
        P2choice = input("\nPlayer 2, please choose rock(r), paper(p), or scissors(s): ")
        if P2choice == "r" or P2choice == "p" or P2choice == "s":
            print("\nChoice confirmed.")
            break
        else:
            print("\nThat is not a valid selection. Please enter 'r', 'p', or 's'.")
    if P1choice == "r":
        if P2choice == "r":
            print("\nYou both chose rock! It's a draw.")
            Draws += 1
        if P2choice == "p":
            print("\nPlayer 2's paper obliterates Player 1's rock somehow! Player 2 wins!")
            P2wins += 1
        if P2choice == "s":
            print("\nPlayer 1's rock obliterates Player 2's scissors! Player 1 wins!")
            P1wins += 1
    if P1choice == "p":
        if P2choice == "r":
            print("\nPlayer 1's paper obliterates Player 2's rock somehow! Player 1 wins!")
            P1wins += 1
        if P2choice == "p":
            print("\nYou both chose paper! It's a draw.")
            Draws += 1
        if P2choice == "s":
            print("\nPlayer 2's scissors obliterate Player 1's paper! Player 2 wins!")
            P2wins += 1
    if P1choice == "s":
        if P2choice == "r":
            print("\nPlayer 2's rock obliterates Player 1's scissors! Player 2 wins!")
            P2wins += 1
        if P2choice == "p":
            print("\nPlayer 1's scissors obliterate Player 2's paper! Player 1 wins!")
            P1wins += 1
        if P2choice == "s":
            print("\nYou both chose scissors! It's a draw.")
            Draws += 1
    print("\nPlayer 1:",P1wins)
    print("Player 2:",P2wins)
    print("Draws:",Draws)
    if P1wins > P2wins:
        print("\nPlayer 1 is in the lead!")
    if P2wins > P1wins:
        print("\nPlayer 2 is in the lead!")
    if P1wins == P2wins:
        print("\nIt's all tied up!")
    Choice = input("\nWould you like to play again?: ")
    if Choice == "no" or Choice == "No":
        print("\nToo bad! Mwahahaha!")
    else:
        print("\nHere we go!")
        print("\n================================================")
        print("================================================")
    
