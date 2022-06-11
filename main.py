# rock-paper-scissors

player_one_answer= "r"
player_one_and_player_two_answer= "s"
player_two_answer="p"

player_one_guess= input('call your guess:')
print(type(player_one_guess))

player_one_guess= (player_one_guess)
print(type(player_one_guess))

player_one_and_player_two_guess = input('call your guess:')
print(type(player_one_and_player_two_guess))

player_one_and_player_two_guess= (player_one_and_player_two_guess)
print(type(player_one_and_player_two_guess))

player_two_guess=input('call your guess:')
print(type(player_two_guess))

player_two_guess = (player_two_guess)
print(type(player_two_guess))

if player_one_guess == player_one_answer:
    print(" congratulations!player one, you won.You guessed the right answer: " + (player_one_answer))

if  player_one_and_player_two_guess == player_one_and_player_two_guess:
    print("oh! it a tie. you both guessed paper, play again:"  + (player_one_and_player_two_answer) ) 


if player_two_guess != player_two_answer:
    print("sorry!player two, you lose.you have guessed wrong: " + (player_two_answer))
    


    
