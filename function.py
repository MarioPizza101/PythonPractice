Account_list = ["user1" , "user2" , "user3"]

username = "user2"

def account_check():
    if username in Account_list:
        print(f"{username} is an account.")
    else:
        print(f"{username} is not an account.")

account_check()
