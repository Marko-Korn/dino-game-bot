# dino-game-bot
A simple Python based script made using NumPy, Pyautogui and PIL.

# Features
First the script needs to get the coordinates of a portion of the game window and uses pyautogui to get screenshot of the area, converts the screenshot into a grayscale and calculates the mean brightness. If the brightness is below a certain value then it detects an obstacle.
