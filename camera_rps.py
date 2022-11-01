
'''
Milestone 4
Replace the hard-coded user guess with the output of the computer vision model. Create a new file called camera_rps.py
where you will write the new code.

Create a new function called get_prediction that will return the output of the model you used earlier.

Remember that the output of the model you downloaded is a list of probabilities for each class. 
You need to pick the class with the highest probability. So, for example, assuming you trained the model in 
this order: "Rock", "Paper", "Scissors", and "Nothing", if the first element of the list is 0.8, the second element 
is 0.1, the third element is 0.05, and the fourth element is 0.05, then, the model predicts that you showed "Rock" to the 
camera with a confidence of 0.8.

The model can make many predictions at once if given many images. In your case you only give it one image at a time. 
That means that the first element in the list returned from the model is a list of probabilities for the four different 
classes. Print the response of the model if you are unclear of this.

Milestone5:
In the previous task, the script reads the input from the camera and then compares it with the computer's choice without
stopping. However, when you play a regular game, you usually count down to zero, and at that point you show your hand.

In this case, you need to add that countdown. An important thing to remember is that you can't use the sleep function
because it will stop the script, and during that time, the camera will not be able to capture the input.

Use the function time.time() to get how much time has passed since the script started. 
Print, for example, "you chose rock"
in the terminal when the countdown gets to zero.
time.time() returns the number of seconds that have passed since the epoch. 


MIlestone 5 Task 3
The game should be repeated until either the computer or the user wins three rounds.

Feel free to code the logic as you want, but a good start would be creating and updating two variables that count the 
number of wins for each player. Name these variables computer_wins and user_wins.

Quick tip here: You shouln't use a while loop inside the main while loop (the one capturing and showing your image).
The reason behind it is that, when you are inside the nested loop, the code in the main while loop won't run, and hence,
the camera won't show anything.
'''
# %%
import manual_rps
import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():
    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        max_value_index = np.argmax(prediction[0], axis=0) # index of highest probability in prediction list
        probability = prediction[0][max_value_index] # Returns highest probability in numpy array
        choice = {0: "rock",  1: "scissors", 2: "paper", 3: "Nothing"}
        user_choice =  choice[max_value_index]
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    start = time.time()
    end = start + 5
    while time.time() < end:
        pass
    print(f"You have chosen '{user_choice}'")
    return user_choice


print(
get_prediction()) # first prediction

print(f"2nd {get_prediction()}") # second prediction

# %%
def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        result = "Draw"
    # Combinations for user to win
    elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
        result = "User wins this round"
    # All other Combinations means Computer wins
    else:
        result = "Computer wins this round"
    print(result)
    return result

def play_round():
    '''
    Runs one round between a user and computer. Returns winner of a round or draw.
    '''
    computer_choice = manual_rps.get_computer_choice()
    user_choice = get_prediction()
    result = get_winner(computer_choice, user_choice)
    return result

def rock_paper_scissors():
    '''
    Code that runs the game until a player wins three rounds
    '''
    computer_wins = 0
    user_wins = 0
    round = 0
    while computer_wins != 3 or user_wins != 3:
        print(f"Round {round}. Scores are Computer: {computer_wins} and you: {user_wins} ")
        game = play_round() # returns winner of a round
        round+=1
        print(f"winner of {round} {game}")
        if game == "Computer wins this round":
            computer_wins += 1
        elif game == "User wins this round":
            user_wins += 1
        else:
            pass
    if round ==3 and computer_wins > user_wins:
        print("Computer is the winner!")
    elif round ==3 and user_wins > computer_wins:
        print("Congratulations the User Wins!")
    else:
        print("It's a draw")

rock_paper_scissors()

# Writing the game repeatedly 




# %%
def main():
    get_prediction()

if __name__ == "__main__":
    main()# Executed when invoked directly
# %%