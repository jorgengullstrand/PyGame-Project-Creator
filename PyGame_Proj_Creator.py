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
            file.write("import pygame                                           # yup imports pygame\n\n")
            file.write("background_color = (255,255,255)                        # Defines the background color\n")
            file.write("(width, height) = (1280, 720)                           # defines the resolution\n")
            file.write("screen = pygame.display.set_mode((width, height))       # Sets the resolution\n\n\n")
            file.write("pygame.display.set_caption('" + filename + "')          # Sets window name\n")
            file.write("screen.fill(background_color)                           # Sets the background color\n")
            file.write("pygame.display.flip()                                   \n\n\n")           
            file.write("running = True                                          \n")  
            file.write("while running:                                          # Main game loop\n")
            file.write("    for event in pygame.event.get():                    \n")
            file.write("        if event.type == pygame.QUIT:                   # Checks if quit event triggered\n")
            file.write("            running = False                             # Nope running shouldn't be True\n")    
            file.close()
            
        # Writes the batch file to run the game
        with open(batch_file, "w") as file:
            file.write("python code/main.py")                                   # sets the path to main.py for the batch
