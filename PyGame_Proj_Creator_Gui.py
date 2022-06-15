import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
import os 

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(QSize(440, 113))    
        self.setWindowTitle("PyGame Project Creator") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Project Name:')
        self.line = QLineEdit(self)

        self.line.move(120, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('Create', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(120, 60)        

    def clickMethod(self):
        # Definitions
        filename = self.line.text()
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
        #-------------------------------------------------------------------
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
