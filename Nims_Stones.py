#Two players sit in front of a pile of 100 stones. They take turns,
#each removing between 1 and 5 stones (assuming there are at least 5
#stones left in the pile). The person who removes the last stone(s) wins.

pile = 100
turn = 2
import math

#directions that no one will pay attention to
print """There are 100 stones in the pile! Remove 1 to 5 stones per turn, 
as long as there are that many stones left in the pile. 
The person who removes the last stones wins!"""

print 


#Game is happening
while pile >= 1:

#Player 1 turn
    while pile >= 1 and turn % 2 == 0:
        player_1 = math.ceil(input("""Playper 1: Right now there are %d stones in the pile.
How many do you want to remove?"""%(pile)))
        print
    
#function to define a valid answer
        def is_the_choice_valid(choice):
            if choice > 0 and choice <= 5 and choice <= pile:
                return True

#test player 1's choice
        if is_the_choice_valid(player_1) == True:
            pile -= player_1
            turn += 1

        
        elif is_the_choice_valid(player_1) != True:
            if player_1 < 0:
                print """You can't remove a negative number of stones.
Choose a number of stones to remove between 1 and 5 without choosing a number
greater than the number of stones that remain."""
                print
            elif player_1 == 0:
                print """You cannot choose to remove zero stones.
Choose a number of stones to remove between 1 and 5 without choosing a number
greater than the number of stones that remain."""
                print
            elif player_1 > 5:
                print """You muse choose a number of stones between 1 and 5."""
                print
            elif player_1 > pile:
                print """You chose a number greater than the number of
stones that are left in the pile."""
                print
           
        
#Player 2 turn
    while pile >= 1 and turn % 2 == 1:
        player_2 = math.ceil(input("""Playper 2: Right now there are %d stones in the pile.
How many do you want to remove?"""%(pile)))
        print
    
#function to define a valid answer
        def is_the_choice_valid(choice):
            if choice > 0 and choice <= 5 and choice <= pile:
                return True

#test if player 2's choice is valid
        if is_the_choice_valid(player_2) == True:
            pile -= player_2
            turn += 1


#Account for errors in player 2's choice      
        elif is_the_choice_valid(player_2) != True:
            if player_2 < 0:
                print """You can't remove a negative number of stones.
Choose a number of stones to remove between 1 and 5 without choosing a number
greater than the number of stones that remain."""
                print
            elif player_2 == 0:
                print """You cannot choose to remove zero stones.
Choose a number of stones to remove between 1 and 5 without choosing a number
greater than the number of stones that remain."""
                print
            elif player_2 > 5:
                print """You muse choose a number of stones between 1 and 5."""
                print
            elif player_2 > pile:
                print """You chose a number greater than the number of
stones that are left in the pile."""
                print


else:
    print "Game Over!"
    if turn % 2 == 0:
        print "Player 1 Wins!!!"
    if turn % 2 == 1:
        print "Player 2 Wins!!!"
