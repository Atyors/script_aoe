import tkinter as tk
import ImageRobot.Focus


# ==============================================================================
# Global
# ==============================================================================

# Name of the build order to load.
BUILD_ORDER = "fast_castle_mayan.txt"

# Name of the game to focus.
PROGRAM = "Age of Empire"

# Message telling build order is over.
ENDED_BO = "BO terminé."

# Width of the window.
WIDTH_SIZE = 265

# Height of the window.
HEIGHT_SIZE = 105

# Tool to focus window.
FOCUSER = ImageRobot.Focus()

# Posiiton of the file reading.
pointer = 0


# ==============================================================================
# Functions
# ==============================================================================

def load_next_step():
    global pointer


    # Focus the game window.
    FOCUSER.focus_window_containing(PROGRAM)

    # Output for the text.
    tmp = ""

    # Number of steps to load.
    steps_quantity = 6

    # If the pointer has been reset.
    if pointer == 0:
        # Get the name of the build order.
        build_name = ""

        # Name is given in the 3 first lines.
        for i in range(3):
            # Add content of each line in the build name variable.
            build_name += LINES[i]

        # Add 3 to the pointer position.
        pointer += 3

        # Set the build name to the main button.
        ACTION["text"] = build_name

        # Set the window on top.
        ROOT.attributes("-topmost", True)

        # Exit the function.
        return

    # Loop for loading the steps.
    for i in range(steps_quantity):
        # Calcultate the position depending on the pointer position.
        position = pointer + i

        # If the position is not over the number of lines.
        if not position >= len(LINES):
            # Add lines in the text variable for replacement.
            tmp += LINES[pointer + i]

    # Update the pointer position.
    pointer += steps_quantity

    # If the build order is over.
    if pointer - (steps_quantity - 1) > len(LINES):
        # Remove the attribute making the window on top.
        ROOT.attributes("-topmost", False)

        # Reset the pointer at the beginning.
        pointer = 0

        # Set the text to build order over.
        tmp = ENDED_BO

    # Update the text in the button.
    ACTION["text"] = tmp


def close_program(event=None):
    ''' Kill the root window.
    '''

    ROOT.destroy()


# ==============================================================================
# Frames creation
# ==============================================================================

# Create the main window.
ROOT = tk.Tk()

# Set the title of the window.
ROOT.title("AoE II - BO helper")

# Put the window on top.
ROOT.attributes("-topmost", True)

# Disable resizable window.
ROOT.resizable(width=False, height=False)

# Set the window at a specific position for a full HD screen (1920*1080).
ROOT.geometry(str(WIDTH_SIZE) + "x" + str(HEIGHT_SIZE) + "+1260+" + str(1080 - HEIGHT_SIZE - 30))

# Create a bind on the Escape key to close the program.
ROOT.bind("<Escape>", close_program)



# ==============================================================================
# Widgets creation
# ==============================================================================

# Create the button filling all the space.
ACTION = tk.Button(ROOT, width=WIDTH_SIZE, height=HEIGHT_SIZE, command=load_next_step)
# Pack the button in the window.
ACTION.pack(side=tk.TOP)


# ==============================================================================
# Setup environment
# ==============================================================================

# Get all the line of the file.
LINES = open(BUILD_ORDER, "r", encoding="UTF-8").readlines()

# Load the name of the build order.
load_next_step()


# ==============================================================================
# Window threading
# ==============================================================================

ROOT.mainloop()
