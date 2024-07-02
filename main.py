import pyautogui
import time
from PIL import ImageOps
import pyscreeze
import numpy as np


x1, y1 = 300, 570  # Top left corner of the game
x2, y2 = 430, 700  # Bottom right corner of the game

def restart_game():
    pyautogui.click(x1 + 50, y1 + 50)
    time.sleep(1)


def press_space():
    pyautogui.keyDown('space')
    time.sleep(0.1)
    pyautogui.keyUp('space')


def is_obstacle(image):
    # Convert image to grayscale
    gray_image = ImageOps.grayscale(image)
    # Convert to numpy array
    a = np.array(gray_image)
    # Calculate the mean brightness
    mean_brightness = np.mean(a)
    # Return if brightness is below a value
    return mean_brightness < 250


def capture_screen():
    return pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))


def main():
    restart_game()
    while True:
        screen = capture_screen()
        if is_obstacle(screen):
            press_space()


if __name__ == "__main__":
    main()
