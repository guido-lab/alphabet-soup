import time

def checkAlphabetSoup(message, alphabet):

    message_list = list(message) # convert the message into an array
    alphabet_list = list(alphabet) # convert the alphabet taken from the bowl into an array
    is_included = True # boolean variable for checking the state of program

    # checking if the message is not empty 
    if len(message_list) > 0:
        # itrating into the list of message chars
        for msg_char in message_list:
            # checking if the current character of message is included to alphabet bowl array
            if msg_char in alphabet_list:
                alphabet_list.remove(msg_char) # remove the alphabet_list the character that have been found

            else:
                is_included = False # if the current character of message is included to alphabet bowl array then change the state of variable
                break # stop iterating 
    else:
        is_included = False # change the state because the message is empty

    return is_included


if __name__ == "__main__":
    start_time = time.time()
    print(checkAlphabetSoup("annastasia", "basnkaqltadlhflvkbaqqqqfdjwertyuioyusiofgnhjk"))
    print("Execution time is: %s seconds " % (time.time() - start_time))

