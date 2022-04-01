# Imports
import os

# Definitions
filename = input("Enter project name: ")
code_path = filename + "/code"
main_file = code_path + "/main.py"
batch_file = filename + "/run.bat"


# Checks if the folder and files already exists, if not it creates
if not os.path.exists(filename):
    if not os.path.exists(main_file):   
        os.makedirs(filename)
        os.makedirs(code_path)

        # Writes everything to main.py
        with open(main_file, 'w') as file:
            file.write("import pygame\n")                                       # yup imports pygame
            file.write("background_color = (255,255,255)\n")                    # Defines the background color
            file.write("(width, height) = (1280, 720)\n")                       # defines the resolution
            file.write("screen = pygame.display.set_mode((width, height))\n")   # Sets the resolution
            file.write("pygame.display.set_caption('" + filename + "')\n")      # Sets window name
            file.write("screen.fill(background_color)\n")                       # Sets the background color 
            file.write("pygame.display.flip()\n")           
            file.write("running = True\n")  
            file.write("while running:\n")                                      # Main game loop
            file.write("    for event in pygame.event.get():\n")
            file.write("        if event.type == pygame.QUIT:\n")               # Checks if quit event triggered
            file.write("            running = False\n")                         # Nope running shouldn't be True    
            file.close()
            
        # Writes the batch file to run the game
        with open(batch_file, "w") as file:
            file.write("python code/main.py")                                   # sets the path to main.py for the batch
            