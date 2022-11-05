import manual_rps
import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')

def get_prediction():
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Text settings
    font = cv2.FONT_HERSHEY_SIMPLEX
    center_of_frame = (50, 50)
    fontScale = 2
    fontColor = (255, 255, 255)
    thickness = 5
    lineType = 2
    print(f"Get ready!")
    start = time.time()
    end = start + 5
    while time.time() < end and True:
        #while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        # Prints countdown in frames
        cv2.putText(frame,
            'Countdown in {:0.2f}s'.format((time.time())-start, frame),center_of_frame,
            font,
            fontScale,
            fontColor,
            thickness,
            lineType)

        cv2.imshow('frame', frame)
        max_value_index = np.argmax(prediction[0], axis=0) # index of highest probability in prediction list
        choice = {0: "rock",  1: "scissors", 2: "paper", 3: "Nothing"}
        user_choice =  choice[max_value_index]
         # Press q to close the window
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            print("You quit the game :(. To play again re-run the game")
            cv2.destroyAllWindows()
            user_choice = None
            break
        elif time.time() == end:
            return user_choice
    cap.release()
    return str(user_choice)

def get_winner(computer_choice, user_choice):
    print(f"Computer Chooses {computer_choice} and user chooses {user_choice}")
    if computer_choice == user_choice:
        print("It's a draw!")
        result = "No One"
    # Combinations for user to win
    elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
        result = "User"
    # All other Combinations means Computer wins
    else:
        result = "Computer"
    return result

def rock_paper_scissors():
    '''
    Code that runs the game until a player wins three rounds
    '''
    computer_wins = 0
    user_wins = 0
    round = 1
    while not( computer_wins == 3 or user_wins == 3):
    # while computer_wins != 3 or user_wins != 3:
        print(f"Round {round}. Scores are: Computer {computer_wins} VS. You {user_wins}")
        computer_choice = str(manual_rps.get_computer_choice())
        user_choice = get_prediction()
        game = get_winner(computer_choice, user_choice)
        round+=1
        print(f"winner of round {round} is {game}!")
        if game == "Computer":
            computer_wins += 1
        elif game == "User":
            user_wins += 1
        else:
            pass
        
    if computer_wins == 3 and computer_wins > user_wins:
        print("Computer is the winner!")
    elif user_wins == 3 and user_wins > computer_wins:
        print("Congratulations the User Wins!")
    else:
        pass
    print(f"Final scores are: Computer {computer_wins} VS. You {user_wins}")
    # Destroy all the windows after the game ends
    cv2.destroyAllWindows() # cv2.destroyAllWindows() line and the cap.release() will release the camera and destroy the camera window.
    #return f"Final scores are: Computer {computer_wins} VS. You {user_wins}"

# def main():
#     get_prediction()
#     get_winner()
#     rock_paper_scissors()

# if __name__ == "__main__":
#     main()# Executed when invoked directly
