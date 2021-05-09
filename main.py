import random
from game_data import data
from art import logo, vs
from replit import clear

# 3.Format the account data into printable format
#code pulled up to put inside a separate, new function:
def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]#And this will go into that dictionary and pull out the value under the key 'name' and save it to this variable.
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

## 7.Use if statement to check it user is correct
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    

# 1.Display art
print(logo)
score = 0
game_should_continue = True
# 11.Making the accounts at position B become the next account at position A
account_b = random.choice(data)

# 10.Make game repeatable.
while game_should_continue:
    # 2.Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    # 2b. Check if counts are equal, in which case we will get a new b
    #changing if to a while loop so computer keeps checking if they are equal as they change each round
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)           
    print(f"Compare B: {format_data(account_b)}.")
    # 4.Ask the user for a guess

    guess = input("Which do you think has more Instagram followers, 'A' or 'B'?\n").lower() #akes everything lower case to accept A and a

    # 5.Check if User is correct
    ## 6.Get follower count of each account
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_answer(guess, a_followers, b_followers)
    print(f"A has {a_followers}.")
    print(f"B has {b_followers}.")
# 12.Clear previous output and displays fresh screen
    clear()
    print(logo)
    # 8.Give user feedback on their guess
    # 9.Score keeping
    if is_correct:
        score += 1
        print(f"Good job! Your score is {score}")
    else:
        game_should_continue = False
        print(f"Nope. Your final score is {score}")

