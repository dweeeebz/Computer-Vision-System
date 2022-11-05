# Computer-Vision-System

My Second AiCore Project was to create a computer vision system. It detects whether a user is showing rock, paper or scissors to the camera.

Using [Teachabe-Machine](https://teachablemachine.withgoogle.com/train/image), I first created the model. The model was created by four different classes, corresponding to rock, paper, scissors or nothing.

I then downloaded the model file. These contain the structure and the parameters of a deep learaning model. 

`keras_model.h5` and `labels.txt`

These files do not run.
## Milestone 1 - Setting up the virtual envrionement

Installing the dependencies and creating a virtual Environment.

First install `virtualenv` in the file that I want it in

`python -m pip install virtualenv`

First created a virtual environment using the powershell terminal.

`python -m venv virtual_env` where the name of the virtual environment (in this case it was `virtual_env` ) was the argument for the prompt.

Then I installed the libaries.

`python -m pip install <libary>`

The installed the libaries that the model **depends** on.
`opencv-python`, `ipykernel` and `tensorflow`

I ran into some issues when downloading Tensorflow. Following error was being raised.

`ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory:`

After some googling, I changed my laptops **enablelongpaths** from 0 to 1 in **Registry Editor**. I was then able to install tensorflow.

Then I completed the installation of the dependencies.

`pip install ipykernel`

Lastly I created a requirements.txt file by running the following command:

`pip list > requirements.txt` This file allows other users that want to use my computer to install the exact dependencies by running

`pip install requirements.txt.`

## Milestone 2 - Creating a computer vision system (The model)
This model detects what the user has chosen from rock, paper and scissors. 

## Milestone 3 - Install the dependencies 
A few libaries and modules are needed for the project.

## Milestone 4 - Creating the Rock, Paper & Scissors game.
First creating a script that plays the game without the use of a camera. 
Milestone 4

## Milestone 5 - Creating the camera version to play the game.
get_prediction draws frame until the user quits or when the 5 second countdown finishes. It then returns a prediction of what the user has chosen.
The model prints out a list of probabilities for each class. Then chooses the class with the highest probability. Whatever the probability corresponds to from the list is the users output.
In milestone 5 includes combines everythong together to play game of rock paper scissors between the computer and the user thorugh a webcam. The player that wins 3 rounds is the winner.

Note we can not use a while loop inside the main code block that is capturing and showing the image of the user. This is because the code won't run.
![CVP](https://user-images.githubusercontent.com/52679005/200125362-92a354e2-88b9-4ff6-8f7d-2ccf822084d5.JPG)

