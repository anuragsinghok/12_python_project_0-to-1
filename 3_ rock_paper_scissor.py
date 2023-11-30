import random 
def play():
    user = input("whats you choice : 'r' for rock ,'p'  for paper , ' s' for scissors ")
    computer = random.choice(['r', 'p' , 's']) # new things i learned that we can give choice also
    # print(computer)
    if user == computer:
        return 'its a tie'
    
    #r > s, s > p , p>r
    if is_win(user,computer):
        return 'you won!'
    
    return 'you lost'

    
def is_win(player,opponent):
    #return true if player wins
    # r >s, s> p ,p>r  
    if (player =='r' and opponent == 's') or (player =='s' and opponent =='p') \
    or (player == 'p' and opponent =='r'):
        return True
     
print(play())
