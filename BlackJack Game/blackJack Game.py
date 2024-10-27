

# BlackJack Game 
import random
import art

def total(get_cards):
    """ The function is used to count the total value of the cards
    as value of cards for 'J' ,'Q' , 'K' is set to be 10 """
    sum = 0
    for number in get_cards:
        if number in ["J","Q","K"]:
           number = 10 
        sum+=number
    return sum

cards = [2,3,4,5,6,7,8,9,10,"J","Q","K"]

print(art.text2art(" BlackJack "))
player = random.sample(cards,2)
current_total = total(player)
print(f"Your cards {player}   current_total = {current_total}" )
computer = random.sample(cards,1)
print(f"Computer cards {computer} " )


while True:
    options = input("Type 'Y' to get another card , type 'N' to pass ? :")
    if options == "Y":
        n_one = random.sample(cards,1)
        player.append(n_one[0])
        current_total = total(player)
        print(f"Your cards {player}   current_total = {current_total}" )
        
        
        if current_total > 21:
            print("It exceeds. You Lose")
            break
        continue
    
    
    elif options == "N":
            while total(computer) < 17:
                com = random.sample(cards, 1)[0]
                computer.append(com)
                ans = total(computer)
            print(f"Computer cards {computer} current_total = {ans}")
            
            
            if ans > 21:
                print("Player wins")
                break
            
            
            if current_total > ans and current_total < 21:
                    print("Player Won")
                    break
            
            if current_total == ans:
                print("Draw")
                break
    
    else:
        print("Computer Won")
        break
    

