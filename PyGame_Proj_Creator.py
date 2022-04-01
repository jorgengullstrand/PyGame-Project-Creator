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
            file.write("import pygame\n")
            file.write("background_colour = (255,255,255)\n")
            file.write("(width, height) = (1280, 720)\n")
            file.write("screen = pygame.display.set_mode((width, height))\n")
            file.write("pygame.display.set_caption('" + filename + "')\n")
            file.write("screen.fill(background_colour)\n")
            file.write("pygame.display.flip()\n")
            file.write("running = True\n")
            file.write("while running:\n")
            file.write("    for event in pygame.event.get():\n")
            file.write("        if event.type == pygame.QUIT:\n")
            file.write("            running = False\n")
            file.close()
            
        # Writes the batch file to run the game
        with open(batch_file, "w") as file:
            file.write("python code/main.py")