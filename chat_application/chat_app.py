import database
database.create_tables()
welcome = "-----WELCOME TO CHAT APPLICATION-------------"
print(welcome)
menu = """
1.ADD USER
2.SEND MESSAGE
3.CHAT HISTORY
4.EXIT
"""
while(user_input := input(menu)) != "4":
    if user_input == "1":
        username = input("ENTER THE USERNAME:")
        database.add_user(username)
        print(f"{username} ADDED SUCCESSFULLY")
    elif user_input == "2":
        sender_id = int(input("ENTER THE SENDER ID"))
        receiver_id = int(input("ENTER THE RECEIVER ID"))
        message = input("enter the message to send:")
        database.add_message(sender_id,receiver_id,message)
        print("MESSAGE SENT SUCCESSFULLY")
    elif user_input == "3":
        sender_id = int(input("ENTER THE SENDER ID"))
        receiver_id = int(input("ENTER THE RECEIVER ID"))
        

        database.chat_history(sender_id,receiver_id)
    else:
        print("INVALID INPUT")


