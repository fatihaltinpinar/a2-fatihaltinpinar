# REPL comments
from hash_password import create_hash


def print_list(comments):
    for i in range(len(comments)):
        print(i + 1, "-", comments[i])


def comment_menu():

    stop = False
    comments = []

    while not stop:
        new_comment = str(input("Enter your comment= "))

        if new_comment == 'quit':
            return comments
        elif new_comment == '':
            print('Entering empty comments are not welcome around here!')
        else:
            comments.append(new_comment)
            print_list(comments)
            print("Enter 'quit' to quit")

    return comments


# Password you must enter to add comments to the system
password = 'e4ba5cbd251c98e6cd1c23f126a3b81d8d8328abc95387229850952b3ef9f904'

if __name__ == '__main__':
    user_password = str(input('Enter your password to add comments: '))
    if password == create_hash(user_password):
        a = comment_menu()
    else:
        print("Wrong password bye bye!")

