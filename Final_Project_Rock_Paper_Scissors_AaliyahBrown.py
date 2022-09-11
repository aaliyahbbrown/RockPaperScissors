"""
Course: Introduction to Python Programming
Student Name: Aaliyah Brown
"""
#%%
from random import randint
#note: x=randint(0, 10) will generate a random integer x and 0<=x<=10
# %%
def HumanPlayer(GameRecord):
    flag=0
    while (flag !=1):
        '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfHumanPlayer, a string that can only be rock, paper, scissors, or quit
    Description:
        This function asks the user to make a choice (i.e. input a string)
        This function will NOT return/exit until it gets a valid input from the user
        valid inputs are: rock or r, paper or p, scissors or s, game or g, quit or q
        quit means the user wants to quit the game
        game means the user wants to see the GameRecord
         '''
        print("-"*100)
        print("Welcome to rock-paper-scissors!")
        print("Let's play......GOOD LUCK!")
        print("")
        print("Choose: rock(r), paper(p) or scissors(s)?")
        print(" ")
        print("Would you like to see a record of the game (g)?")
        print("")
        print("Would you like to quit (q)?")
        print("")
        ChoiceofHumanPlayer=input("Please enter your decision:")
        print(" ")

        if ChoiceofHumanPlayer in ('rock','r','paper', 'p', 'scissors', 's','g','q'):
            flag=0
            return ChoiceofHumanPlayer
        else:
            print("Invalid Entry.Try again")
            flag=1
# %%
def ComputerPlayer(GameRecord):
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfComputerPlayer, a string that can only be rock, paper, scissors
    Description:
        ComputerPlayer will randomly make a choice
        ComputerPlayer should not look at the current choice of HumanPlayer
    '''
    x=randint(1,3)
    if x==1:
        return 'rock'
    elif x==2:
        return 'paper'
    elif x==3:
        return 'scissors'

# %%
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: Outcome
        Outcome is 0 if it is a draw/tie
        Outcome is 1 if ComputerPlayer wins
        Outcome is 2 if HumanPlayer wins
    Description:
        this function determines the outcome of a game
    '''

    if ChoiceOfComputerPlayer == ChoiceOfHumanPlayer:
        return 0
    elif ChoiceOfComputerPlayer in ('rock','r') and ChoiceOfHumanPlayer in ('scissors','s'):
        return 1
    elif ChoiceOfComputerPlayer in ('rock','r') and ChoiceOfHumanPlayer in ('paper','p'):
        return 2
    elif ChoiceOfComputerPlayer in ('paper','p') and ChoiceOfHumanPlayer in ('rock','r'):
        return 1
    elif ChoiceOfComputerPlayer in ('paper','p') and ChoiceOfHumanPlayer in ('scissors','s'):
        return 2
    elif ChoiceOfComputerPlayer in ('scissors','s') and ChoiceOfHumanPlayer in ('paper','p'):
        return 1
    elif ChoiceOfComputerPlayer in ('scissors','s') and ChoiceOfHumanPlayer in ('rock','r'):
        return 2
# %%
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        Outcome is from Judge
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: None
    Description:
        print Outcome, Choices and Players to the console window
        the message should be human readable
    '''
    print("-"*20, "OUTCOME","-"*20)

    if Outcome ==0:
            print("Tie! The computer chose!", ChoiceOfComputerPlayer,"You chose:", ChoiceOfHumanPlayer)
    elif Outcome==1:
            print("You lose! Computer chose:", ChoiceOfComputerPlayer, "You chose",ChoiceOfHumanPlayer)
    elif Outcome==2:
            print("You won! Computer chose:", ChoiceOfComputerPlayer, "You chose",ChoiceOfHumanPlayer)
            print("-"*50)
# %%
def UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    '''
    Parameters:
        GameRecord is the record of both players' choices and and outcomes
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
        Outcome is an integer from Judge
    Return: None
    Description:
        this function updates GameRecord, a list of three lists
    '''
# %%
def PrintGameRecord(GameRecord):
    '''
    Parameters: GameRecord (the record of both players' choices and outcomes)
    Return: None
    Description: this function prints the record of the game (see the sample run)
        the number of rounds. human wins x rounds. computer wins y rounds.
        the record of choices.
    '''
    print("-"*7,"Game Record","-"*7)
    print ("Number of rounds:",len(GameRecord))
    human_victory =0
    computer_victory =0
    for i in GameRecord:
        if i[2]==1:
                computer_victory+=1
        if i[2]==2:
                human_victory+=1
    print("You win",human_victory,"round(s)")
    print("Computer wins", computer_victory,"round(s)")
    print("Human",",","Computer")

    for i in GameRecord:
        print(i[0],",",i[1])

# %% the game
def PlayGame():
    '''
    This is the "main" function
    In this function, human and computer play the game until the human/user wants to quit
    '''
    GameRecord=[]
    print("COME PLAY OUR GAME!")
    print(" ")
    ChoiceofHumanPlayer=-1

    while(True):
        ChoiceofHumanPlayer=HumanPlayer(GameRecord)

        if ChoiceofHumanPlayer in ('rock','r','paper','p','scissors','s'):
            ChoiceofComputerPlayer=ComputerPlayer(GameRecord)
            Outcome=Judge(ChoiceofComputerPlayer, ChoiceofHumanPlayer)
            PrintOutcome(Outcome, ChoiceofComputerPlayer, ChoiceofHumanPlayer)
            UpdateGameRecord(GameRecord, ChoiceofComputerPlayer,ChoiceofHumanPlayer, Outcome)
        elif ChoiceofHumanPlayer=='g':
            PrintGameRecord(GameRecord)
            print("-"*20)
        elif ChoiceofHumanPlayer=='q' or ChoiceofHumanPlayer=='quit':
            print("Bye-Bye.")
            break

# %% do not modify anything below
if __name__ == '__main__':
    PlayGame()
