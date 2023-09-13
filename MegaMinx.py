#Created by Christopher Cahill on 9/8/2023 at 10:00 A.M.
#ChatGPT was used to create the structure for this program and was given the prompt "How would you code a megaminx with a GUI from scratch in Python on VSCode" at 10:10 A.M on 9/8/2023
#ChatGPT was also given these prompts at 10:10-11:00 A.M on 9/8/2023
#"i would like to add the pieces of each face, how would I do that"
#"Can i make each stick clickable"
#"When each sticker is clicked, can you add a list of options including rotate face clockwise"
#"Can you update the GUI such that only 10 stickers are there since the middle sticker never moves and have the first layer just says Face 1 and then below that Face 2 and then below that Face 3"
#"Can you add an if statement for each seperate face number if that face number is roatted clockwise"
#"Can you make it so when Face 1 is rotated, Face 2 Sticker 9 switches locations with Face 3 sticker 1"
#All of these prompts were used to make the basic GUI and function of the MegaMinx but logic was created by hand
#On 9/10/2023 at 10:00-11:00 A.M ChatGPT was given my code and also used for these prompts
#" Can you add a button that says randomize"
#"Can you change the randomize button so it rotates different faces clockwise"
#"Can you modify the randomize button again so it takes in an input of random moves to be made and then randomly rotates that many times"


import tkinter as tk
from tkinter import messagebox
import random

class MegaminxGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Megaminx Solver")

        # Initialize the stickers for each face
        self.stickers = {}
        colors = ["Blue", "Yellow", "Lime", "Pink", "Red", "White","Purple","Green","Orange","Teal","Gold","Silver"]  # Add more colors if needed

        for face in range(12):
            self.stickers[face] = []
            for sticker in range(10):
                label = tk.Label(master, text=f"{colors[face]} {sticker+1}", 
                            cursor="hand2")
                label.grid(row=face, column=sticker, padx=5, pady=5)
                label.bind("<Button-1>", lambda event, f=face, s=sticker: self.handle_sticker_click(f, s))
                self.stickers[face].append(label)

        # Create a solve button
        solve_button = tk.Button(master, text="Solve", command=self.solve)
        solve_button.grid(row=12, column=5, pady=10)

        # Create a randomize button
        randomize_button = tk.Button(master, text="Randomize", command=self.randomize)
        randomize_button.grid(row=12, column=6, pady=10)

        self.random_moves_entry = tk.Entry(master)
        self.random_moves_entry.grid(row=12, column=7, padx=5, pady=5)
        label = tk.Label(master, text="Random Moves")
        label.grid(row=12, column=8, padx=5, pady=5)
    def randomize(self):
        # Get the user input for the number of random moves
        num_moves = int(self.random_moves_entry.get())

        for _ in range(num_moves):
            random_face = random.randint(0, 11)
            self.rotate_face_clockwise(random_face)
    def handle_sticker_click(self, face, sticker):
        # This method is called when a sticker is clicked
        context_menu = tk.Menu(self.master, tearoff=0)
        context_menu.add_command(label="Rotate Face Clockwise", command=lambda f=face: self.rotate_face_clockwise(f))
        context_menu.add_command(label="Rotate Face Counter Clockwise", command=lambda f=face: self.rotate_face_counterclockwise(f))
        context_menu.post(self.master.winfo_pointerx(), self.master.winfo_pointery())

    def rotate_face_clockwise(self, face):
        if face == 0:
            # Rotate the BLUE FACE (0) clockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker < 8:
                    new_stickers[face][(sticker+2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 8:
                    new_stickers[face][0] = self.stickers[face][sticker]["text"]
                elif sticker == 9:
                    new_stickers[face][1] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            temp_text1 = self.stickers[2][0]["text"]
            self.stickers[2][0]["text"] = self.stickers[1][8]["text"]
            self.stickers[1][8]["text"] = self.stickers[5][6]["text"]
            self.stickers[5][6]["text"] = self.stickers[4][4]["text"]
            self.stickers[4][4]["text"] = self.stickers[3][2]["text"]
            self.stickers[3][2]["text"] = temp_text1
            temp_text2 = self.stickers[2][1]["text"]
            self.stickers[2][1]["text"] = self.stickers[1][9]["text"]
            self.stickers[1][9]["text"] = self.stickers[5][7]["text"]
            self.stickers[5][7]["text"] = self.stickers[4][5]["text"]
            self.stickers[4][5]["text"] = self.stickers[3][3]["text"]
            self.stickers[3][3]["text"] = temp_text2
            temp_text3 = self.stickers[2][2]["text"]
            self.stickers[2][2]["text"] = self.stickers[1][0]["text"]
            self.stickers[1][0]["text"] = self.stickers[5][8]["text"]
            self.stickers[5][8]["text"] = self.stickers[4][6]["text"]
            self.stickers[4][6]["text"] = self.stickers[3][4]["text"]
            self.stickers[3][4]["text"] = temp_text3
        elif face == 1:
            # Rotate the YELLOW FACE (1) clockwise
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker < 8:
                    new_stickers[face][(sticker+2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 8:
                    new_stickers[face][0] = self.stickers[face][sticker]["text"]
                elif sticker == 9:
                    new_stickers[face][1] = self.stickers[face][sticker]["text"]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[5][4]["text"]
            self.stickers[5][4]["text"] = self.stickers[0][2]["text"]
            self.stickers[0][2]["text"] = self.stickers[2][2]["text"]
            self.stickers[2][2]["text"] = self.stickers[8][8]["text"]
            self.stickers[8][8]["text"] = self.stickers[6][6]["text"]
            self.stickers[6][6]["text"] = temp_text1
            temp_text2 = self.stickers[5][5]["text"]
            self.stickers[5][5]["text"] = self.stickers[0][3]["text"]
            self.stickers[0][3]["text"] = self.stickers[2][3]["text"]
            self.stickers[2][3]["text"] = self.stickers[8][9]["text"]
            self.stickers[8][9]["text"] = self.stickers[6][7]["text"]
            self.stickers[6][7]["text"] = temp_text2
            temp_text3 = self.stickers[5][6]["text"]
            self.stickers[5][6]["text"] = self.stickers[0][4]["text"]
            self.stickers[0][4]["text"] = self.stickers[2][4]["text"]
            self.stickers[2][4]["text"] = self.stickers[8][0]["text"]
            self.stickers[8][0]["text"] = self.stickers[6][8]["text"]
            self.stickers[6][8]["text"] = temp_text3
        
        elif face == 2:
            # Rotate the LIME FACE (2) clockwise
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker < 8:
                    new_stickers[face][(sticker+2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 8:
                    new_stickers[face][0] = self.stickers[face][sticker]["text"]
                elif sticker == 9:
                    new_stickers[face][1] = self.stickers[face][sticker]["text"]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[3][4]["text"]
            self.stickers[3][4]["text"] = self.stickers[11][6]["text"]
            self.stickers[11][6]["text"] = self.stickers[8][4]["text"]
            self.stickers[8][4]["text"] = self.stickers[1][6]["text"]
            self.stickers[1][6]["text"] = self.stickers[0][4]["text"]
            self.stickers[0][4]["text"] = temp_text1
            temp_text2 = self.stickers[3][5]["text"]
            self.stickers[3][5]["text"] = self.stickers[11][7]["text"]
            self.stickers[11][7]["text"] = self.stickers[8][5]["text"]
            self.stickers[8][5]["text"] = self.stickers[1][7]["text"]
            self.stickers[1][7]["text"] = self.stickers[0][5]["text"]
            self.stickers[0][5]["text"] = temp_text2
            temp_text3 = self.stickers[3][6]["text"]
            self.stickers[3][6]["text"] = self.stickers[11][8]["text"]
            self.stickers[11][8]["text"] = self.stickers[8][6]["text"]
            self.stickers[8][6]["text"] = self.stickers[1][8]["text"]
            self.stickers[1][8]["text"] = self.stickers[0][6]["text"]
            self.stickers[0][6]["text"] = temp_text3    
        
        elif face == 3:
            # Rotate the PINK FACE (3) clockwise
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker < 8:
                    new_stickers[face][(sticker+2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 8:
                    new_stickers[face][0] = self.stickers[face][sticker]["text"]
                elif sticker == 9:
                    new_stickers[face][1] = self.stickers[face][sticker]["text"]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[11][4]["text"]
            self.stickers[11][4]["text"] = self.stickers[10][4]["text"]
            self.stickers[10][4]["text"] = self.stickers[4][6]["text"]
            self.stickers[4][6]["text"] = self.stickers[0][6]["text"]
            self.stickers[0][6]["text"] = self.stickers[2][8]["text"]
            self.stickers[2][8]["text"] = temp_text1
            temp_text2 = self.stickers[11][5]["text"]
            self.stickers[11][5]["text"] = self.stickers[10][5]["text"]
            self.stickers[10][5]["text"] = self.stickers[4][7]["text"]
            self.stickers[4][7]["text"] = self.stickers[0][7]["text"]
            self.stickers[0][7]["text"] = self.stickers[2][9]["text"]
            self.stickers[2][9]["text"] = temp_text2
            temp_text3 = self.stickers[11][6]["text"]
            self.stickers[11][6]["text"] = self.stickers[10][6]["text"]
            self.stickers[10][6]["text"] = self.stickers[4][8]["text"]
            self.stickers[4][8]["text"] = self.stickers[0][8]["text"]
            self.stickers[0][8]["text"] = self.stickers[2][0]["text"]
            self.stickers[2][0]["text"] = temp_text3
        
        elif face == 4:
            # Rotate the RED FACE (4) clockwise
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker < 8:
                    new_stickers[face][(sticker+2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 8:
                    new_stickers[face][0] = self.stickers[face][sticker]["text"]
                elif sticker == 9:
                    new_stickers[face][1] = self.stickers[face][sticker]["text"]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[0][8]["text"]
            self.stickers[0][8]["text"] = self.stickers[3][0]["text"]
            self.stickers[3][0]["text"] = self.stickers[10][2]["text"]
            self.stickers[10][2]["text"] = self.stickers[7][2]["text"]
            self.stickers[7][2]["text"] = self.stickers[5][8]["text"]
            self.stickers[5][8]["text"] = temp_text1
            temp_text1 = self.stickers[0][9]["text"]
            self.stickers[0][9]["text"] = self.stickers[3][1]["text"]
            self.stickers[3][1]["text"] = self.stickers[10][3]["text"]
            self.stickers[10][3]["text"] = self.stickers[7][3]["text"]
            self.stickers[7][3]["text"] = self.stickers[5][9]["text"]
            self.stickers[5][9]["text"] = temp_text1
            temp_text1 = self.stickers[0][0]["text"]
            self.stickers[0][0]["text"] = self.stickers[3][2]["text"]
            self.stickers[3][2]["text"] = self.stickers[10][4]["text"]
            self.stickers[10][4]["text"] = self.stickers[7][4]["text"]
            self.stickers[7][4]["text"] = self.stickers[5][0]["text"]
            self.stickers[5][0]["text"] = temp_text1
        
        elif face == 5:
            # Rotate the WHITE FACE (5) clockwise
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker < 8:
                    new_stickers[face][(sticker+2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 8:
                    new_stickers[face][0] = self.stickers[face][sticker]["text"]
                elif sticker == 9:
                    new_stickers[face][1] = self.stickers[face][sticker]["text"]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[1][0]["text"]
            self.stickers[1][0]["text"] = self.stickers[0][0]["text"]
            self.stickers[0][0]["text"] = self.stickers[4][2]["text"]
            self.stickers[4][2]["text"] = self.stickers[7][0]["text"]
            self.stickers[7][0]["text"] = self.stickers[6][8]["text"]
            self.stickers[6][8]["text"] = temp_text1
            temp_text2 = self.stickers[1][1]["text"]
            self.stickers[1][1]["text"] = self.stickers[0][1]["text"]
            self.stickers[0][1]["text"] = self.stickers[4][3]["text"]
            self.stickers[4][3]["text"] = self.stickers[7][1]["text"]
            self.stickers[7][1]["text"] = self.stickers[6][9]["text"]
            self.stickers[6][9]["text"] = temp_text2
            temp_text3 = self.stickers[1][2]["text"]
            self.stickers[1][2]["text"] = self.stickers[0][2]["text"]
            self.stickers[0][2]["text"] = self.stickers[4][4]["text"]
            self.stickers[4][4]["text"] = self.stickers[7][2]["text"]
            self.stickers[7][2]["text"] = self.stickers[6][0]["text"]
            self.stickers[6][0]["text"] = temp_text3
        
        elif face == 6:
            # Rotate the PURPLE FACE (6) clockwise
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker < 8:
                    new_stickers[face][(sticker+2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 8:
                    new_stickers[face][0] = self.stickers[face][sticker]["text"]
                elif sticker == 9:
                    new_stickers[face][1] = self.stickers[face][sticker]["text"]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[8][0]["text"]
            self.stickers[8][0]["text"] = self.stickers[1][2]["text"]
            self.stickers[1][2]["text"] = self.stickers[5][2]["text"]
            self.stickers[5][2]["text"] = self.stickers[7][8]["text"]
            self.stickers[7][8]["text"] = self.stickers[9][0]["text"]
            self.stickers[9][0]["text"] = temp_text1
            temp_text2 = self.stickers[8][1]["text"]
            self.stickers[8][1]["text"] = self.stickers[1][3]["text"]
            self.stickers[1][3]["text"] = self.stickers[5][3]["text"]
            self.stickers[5][3]["text"] = self.stickers[7][9]["text"]
            self.stickers[7][9]["text"] = self.stickers[9][1]["text"]
            self.stickers[9][1]["text"] = temp_text2
            temp_text3 = self.stickers[8][2]["text"]
            self.stickers[8][2]["text"] = self.stickers[1][4]["text"]
            self.stickers[1][4]["text"] = self.stickers[5][4]["text"]
            self.stickers[5][4]["text"] = self.stickers[7][0]["text"]
            self.stickers[7][0]["text"] = self.stickers[9][2]["text"]
            self.stickers[9][2]["text"] = temp_text3
        
        elif face == 7:
            # Rotate the GREEN FACE (7) counterclockwise
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker < 8:
                    new_stickers[face][(sticker+2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 8:
                    new_stickers[face][0] = self.stickers[face][sticker]["text"]
                elif sticker == 9:
                    new_stickers[face][1] = self.stickers[face][sticker]["text"]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[6][0]["text"]
            self.stickers[6][0]["text"] = self.stickers[5][0]["text"]
            self.stickers[5][0]["text"] = self.stickers[4][0]["text"]
            self.stickers[4][0]["text"] = self.stickers[10][0]["text"]
            self.stickers[10][0]["text"] = self.stickers[9][2]["text"]
            self.stickers[9][2]["text"] = temp_text1
            temp_text1 = self.stickers[6][1]["text"]
            self.stickers[6][1]["text"] = self.stickers[5][1]["text"]
            self.stickers[5][1]["text"] = self.stickers[4][1]["text"]
            self.stickers[4][1]["text"] = self.stickers[10][1]["text"]
            self.stickers[10][1]["text"] = self.stickers[9][3]["text"]
            self.stickers[9][3]["text"] = temp_text1
            temp_text1 = self.stickers[6][2]["text"]
            self.stickers[6][2]["text"] = self.stickers[5][2]["text"]
            self.stickers[5][2]["text"] = self.stickers[4][2]["text"]
            self.stickers[4][2]["text"] = self.stickers[10][2]["text"]
            self.stickers[10][2]["text"] = self.stickers[9][4]["text"]
            self.stickers[9][4]["text"] = temp_text1
        
        elif face == 8:
            # Rotate the ORANGE FACE (8) counterclockwise
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker < 8:
                    new_stickers[face][(sticker+2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 8:
                    new_stickers[face][0] = self.stickers[face][sticker]["text"]
                elif sticker == 9:
                    new_stickers[face][1] = self.stickers[face][sticker]["text"]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[11][8]["text"]
            self.stickers[11][8]["text"] = self.stickers[2][4]["text"]
            self.stickers[2][4]["text"] = self.stickers[1][4]["text"]
            self.stickers[1][4]["text"] = self.stickers[6][4]["text"]
            self.stickers[6][4]["text"] = self.stickers[9][8]["text"]
            self.stickers[9][8]["text"] = temp_text1
            temp_text2 = self.stickers[11][9]["text"]
            self.stickers[11][9]["text"] = self.stickers[2][5]["text"]
            self.stickers[2][5]["text"] = self.stickers[1][5]["text"]
            self.stickers[1][5]["text"] = self.stickers[6][5]["text"]
            self.stickers[6][5]["text"] = self.stickers[9][9]["text"]
            self.stickers[9][9]["text"] = temp_text2
            temp_text3 = self.stickers[11][0]["text"]
            self.stickers[11][0]["text"] = self.stickers[2][6]["text"]
            self.stickers[2][6]["text"] = self.stickers[1][6]["text"]
            self.stickers[1][6]["text"] = self.stickers[6][6]["text"]
            self.stickers[6][6]["text"] = self.stickers[9][0]["text"]
            self.stickers[9][0]["text"] = temp_text3
        
        elif face == 9:
            # Rotate the TEAL FACE (9) counterclockwise
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker < 8:
                    new_stickers[face][(sticker+2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 8:
                    new_stickers[face][0] = self.stickers[face][sticker]["text"]
                elif sticker == 9:
                    new_stickers[face][1] = self.stickers[face][sticker]["text"]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[11][0]["text"]
            self.stickers[11][0]["text"] = self.stickers[8][2]["text"]
            self.stickers[8][2]["text"] = self.stickers[6][2]["text"]
            self.stickers[6][2]["text"] = self.stickers[7][8]["text"]
            self.stickers[7][8]["text"] = self.stickers[10][8]["text"]
            self.stickers[10][8]["text"] = temp_text1
            temp_text2 = self.stickers[11][1]["text"]
            self.stickers[11][1]["text"] = self.stickers[8][3]["text"]
            self.stickers[8][3]["text"] = self.stickers[6][3]["text"]
            self.stickers[6][3]["text"] = self.stickers[7][9]["text"]
            self.stickers[7][9]["text"] = self.stickers[10][9]["text"]
            self.stickers[10][9]["text"] = temp_text2
            temp_text3 = self.stickers[11][2]["text"]
            self.stickers[11][2]["text"] = self.stickers[8][4]["text"]
            self.stickers[8][4]["text"] = self.stickers[6][4]["text"]
            self.stickers[6][4]["text"] = self.stickers[7][0]["text"]
            self.stickers[7][0]["text"] = self.stickers[10][0]["text"]
            self.stickers[10][0]["text"] = temp_text3
        
        elif face == 10:
            # Rotate the GOLD FACE (10) counterclockwise
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker < 8:
                    new_stickers[face][(sticker+2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 8:
                    new_stickers[face][0] = self.stickers[face][sticker]["text"]
                elif sticker == 9:
                    new_stickers[face][1] = self.stickers[face][sticker]["text"]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[3][6]["text"]
            self.stickers[3][6]["text"] = self.stickers[11][2]["text"]
            self.stickers[11][2]["text"] = self.stickers[9][4]["text"]
            self.stickers[9][4]["text"] = self.stickers[7][4]["text"]
            self.stickers[7][4]["text"] = self.stickers[4][8]["text"]
            self.stickers[4][8]["text"] = temp_text1
            temp_text2 = self.stickers[3][7]["text"]
            self.stickers[3][7]["text"] = self.stickers[11][3]["text"]
            self.stickers[11][3]["text"] = self.stickers[9][5]["text"]
            self.stickers[9][5]["text"] = self.stickers[7][5]["text"]
            self.stickers[7][5]["text"] = self.stickers[4][9]["text"]
            self.stickers[4][9]["text"] = temp_text2
            temp_text3 = self.stickers[3][8]["text"]
            self.stickers[3][8]["text"] = self.stickers[11][4]["text"]
            self.stickers[11][4]["text"] = self.stickers[9][6]["text"]
            self.stickers[9][6]["text"] = self.stickers[7][6]["text"]
            self.stickers[7][6]["text"] = self.stickers[4][0]["text"]
            self.stickers[4][0]["text"] = temp_text3
        
        elif face == 11:
            # Rotate the SILVER FACE (11) counterclockwise
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker < 8:
                    new_stickers[face][(sticker+2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 8:
                    new_stickers[face][0] = self.stickers[face][sticker]["text"]
                elif sticker == 9:
                    new_stickers[face][1] = self.stickers[face][sticker]["text"]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[2][6]["text"]
            self.stickers[2][6]["text"] = self.stickers[8][4]["text"]
            self.stickers[8][4]["text"] = self.stickers[9][6]["text"]
            self.stickers[9][6]["text"] = self.stickers[10][6]["text"]
            self.stickers[10][6]["text"] = self.stickers[3][6]["text"]
            self.stickers[3][6]["text"] = temp_text1
            temp_text2 = self.stickers[2][7]["text"]
            self.stickers[2][7]["text"] = self.stickers[8][5]["text"]
            self.stickers[8][5]["text"] = self.stickers[9][7]["text"]
            self.stickers[9][7]["text"] = self.stickers[10][7]["text"]
            self.stickers[10][7]["text"] = self.stickers[3][7]["text"]
            self.stickers[3][7]["text"] = temp_text2
            temp_text3 = self.stickers[2][8]["text"]
            self.stickers[2][8]["text"] = self.stickers[8][6]["text"]
            self.stickers[8][6]["text"] = self.stickers[9][8]["text"]
            self.stickers[9][8]["text"] = self.stickers[10][8]["text"]
            self.stickers[10][8]["text"] = self.stickers[3][8]["text"]
            self.stickers[3][8]["text"] = temp_text3
    
    
    def rotate_face_counterclockwise(self, face):
        if face == 0:
            # Rotate the BLUE FACE (0) counterclockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker > 1:
                    new_stickers[face][(sticker-2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 0:
                    new_stickers[face][8] = self.stickers[face][sticker]["text"]
                elif sticker == 1:
                    new_stickers[face][9] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            temp_text1 = self.stickers[2][0]["text"]
            self.stickers[2][0]["text"] = self.stickers[3][2]["text"]
            self.stickers[3][2]["text"] = self.stickers[4][4]["text"]
            self.stickers[4][4]["text"] = self.stickers[5][6]["text"]
            self.stickers[5][6]["text"] = self.stickers[1][8]["text"]
            self.stickers[1][8]["text"] = temp_text1
            temp_text2 = self.stickers[2][1]["text"]
            self.stickers[2][1]["text"] = self.stickers[3][3]["text"]
            self.stickers[3][3]["text"] = self.stickers[4][5]["text"]
            self.stickers[4][5]["text"] = self.stickers[5][7]["text"]
            self.stickers[5][7]["text"] = self.stickers[1][9]["text"]
            self.stickers[1][9]["text"] = temp_text2
            temp_text3 = self.stickers[2][2]["text"]
            self.stickers[2][2]["text"] = self.stickers[3][4]["text"]
            self.stickers[3][4]["text"] = self.stickers[4][6]["text"]
            self.stickers[4][6]["text"] = self.stickers[5][8]["text"]
            self.stickers[5][8]["text"] = self.stickers[1][0]["text"]
            self.stickers[1][0]["text"] = temp_text3
        elif face == 1:
            # Rotate the Yellow FACE (1) counterclockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker > 1:
                    new_stickers[face][(sticker-2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 0:
                    new_stickers[face][8] = self.stickers[face][sticker]["text"]
                elif sticker == 1:
                    new_stickers[face][9] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[5][4]["text"]
            self.stickers[5][4]["text"] = self.stickers[6][6]["text"]
            self.stickers[6][6]["text"] = self.stickers[8][8]["text"]
            self.stickers[8][8]["text"] = self.stickers[2][2]["text"]
            self.stickers[2][2]["text"] = self.stickers[0][2]["text"]
            self.stickers[0][2]["text"] = temp_text1
            temp_text2 = self.stickers[5][5]["text"]
            self.stickers[5][5]["text"] = self.stickers[6][7]["text"]
            self.stickers[6][7]["text"] = self.stickers[8][9]["text"]
            self.stickers[8][9]["text"] = self.stickers[2][3]["text"]
            self.stickers[2][3]["text"] = self.stickers[0][3]["text"]
            self.stickers[0][3]["text"] = temp_text2
            temp_text3 = self.stickers[5][6]["text"]
            self.stickers[5][6]["text"] = self.stickers[6][8]["text"]
            self.stickers[6][8]["text"] = self.stickers[8][0]["text"]
            self.stickers[8][0]["text"] = self.stickers[2][4]["text"]
            self.stickers[2][4]["text"] = self.stickers[0][4]["text"]
            self.stickers[0][4]["text"] = temp_text3
        
        elif face == 2:
            # Rotate the Lime FACE (2) counterclockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker > 1:
                    new_stickers[face][(sticker-2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 0:
                    new_stickers[face][8] = self.stickers[face][sticker]["text"]
                elif sticker == 1:
                    new_stickers[face][9] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[3][4]["text"]
            self.stickers[3][4]["text"] = self.stickers[0][4]["text"]
            self.stickers[0][4]["text"] = self.stickers[1][6]["text"]
            self.stickers[1][6]["text"] = self.stickers[8][4]["text"]
            self.stickers[8][4]["text"] = self.stickers[11][6]["text"]
            self.stickers[11][6]["text"] = temp_text1
            temp_text2 = self.stickers[3][5]["text"]
            self.stickers[3][5]["text"] = self.stickers[0][5]["text"]
            self.stickers[0][5]["text"] = self.stickers[1][7]["text"]
            self.stickers[1][7]["text"] = self.stickers[8][5]["text"]
            self.stickers[8][5]["text"] = self.stickers[11][7]["text"]
            self.stickers[11][7]["text"] = temp_text2
            temp_text3 = self.stickers[3][6]["text"]
            self.stickers[3][6]["text"] = self.stickers[0][6]["text"]
            self.stickers[0][6]["text"] = self.stickers[1][8]["text"]
            self.stickers[1][8]["text"] = self.stickers[8][6]["text"]
            self.stickers[8][6]["text"] = self.stickers[11][8]["text"]
            self.stickers[11][8]["text"] = temp_text3   
        
        elif face == 3:
           # Rotate the Pink FACE (3) counterclockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker > 1:
                    new_stickers[face][(sticker-2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 0:
                    new_stickers[face][8] = self.stickers[face][sticker]["text"]
                elif sticker == 1:
                    new_stickers[face][9] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[11][4]["text"]
            self.stickers[11][4]["text"] = self.stickers[2][8]["text"]
            self.stickers[2][8]["text"] = self.stickers[0][6]["text"]
            self.stickers[0][6]["text"] = self.stickers[4][6]["text"]
            self.stickers[4][6]["text"] = self.stickers[10][4]["text"]
            self.stickers[10][4]["text"] = temp_text1
            temp_text2 = self.stickers[11][5]["text"]
            self.stickers[11][5]["text"] = self.stickers[2][9]["text"]
            self.stickers[2][9]["text"] = self.stickers[0][7]["text"]
            self.stickers[0][7]["text"] = self.stickers[4][7]["text"]
            self.stickers[4][7]["text"] = self.stickers[10][5]["text"]
            self.stickers[10][5]["text"] = temp_text2
            temp_text3 = self.stickers[11][6]["text"]
            self.stickers[11][6]["text"] = self.stickers[2][0]["text"]
            self.stickers[2][0]["text"] = self.stickers[0][8]["text"]
            self.stickers[0][8]["text"] = self.stickers[4][8]["text"]
            self.stickers[4][8]["text"] = self.stickers[10][6]["text"]
            self.stickers[10][6]["text"] = temp_text3
        
        elif face == 4:
            # Rotate the Red FACE (4) counterclockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker > 1:
                    new_stickers[face][(sticker-2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 0:
                    new_stickers[face][8] = self.stickers[face][sticker]["text"]
                elif sticker == 1:
                    new_stickers[face][9] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[0][8]["text"]
            self.stickers[0][8]["text"] = self.stickers[5][8]["text"]
            self.stickers[5][8]["text"] = self.stickers[7][2]["text"]
            self.stickers[7][2]["text"] = self.stickers[10][2]["text"]
            self.stickers[10][2]["text"] = self.stickers[3][0]["text"]
            self.stickers[3][0]["text"] = temp_text1
            temp_text2 = self.stickers[0][9]["text"]
            self.stickers[0][9]["text"] = self.stickers[5][9]["text"]
            self.stickers[5][9]["text"] = self.stickers[7][3]["text"]
            self.stickers[7][3]["text"] = self.stickers[10][3]["text"]
            self.stickers[10][3]["text"] = self.stickers[3][1]["text"]
            self.stickers[3][1]["text"] = temp_text2
            temp_text3 = self.stickers[0][0]["text"]
            self.stickers[0][0]["text"] = self.stickers[5][0]["text"]
            self.stickers[5][0]["text"] = self.stickers[7][4]["text"]
            self.stickers[7][4]["text"] = self.stickers[10][4]["text"]
            self.stickers[10][4]["text"] = self.stickers[3][2]["text"]
            self.stickers[3][2]["text"] = temp_text3
        
        elif face == 5:
            # Rotate the White FACE (5) counterclockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker > 1:
                    new_stickers[face][(sticker-2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 0:
                    new_stickers[face][8] = self.stickers[face][sticker]["text"]
                elif sticker == 1:
                    new_stickers[face][9] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[1][0]["text"]
            self.stickers[1][0]["text"] = self.stickers[6][8]["text"]
            self.stickers[6][8]["text"] = self.stickers[7][0]["text"]
            self.stickers[7][0]["text"] = self.stickers[4][2]["text"]
            self.stickers[4][2]["text"] = self.stickers[0][0]["text"]
            self.stickers[0][0]["text"] = temp_text1
            temp_text2 = self.stickers[1][1]["text"]
            self.stickers[1][1]["text"] = self.stickers[6][9]["text"]
            self.stickers[6][9]["text"] = self.stickers[7][1]["text"]
            self.stickers[7][1]["text"] = self.stickers[4][3]["text"]
            self.stickers[4][3]["text"] = self.stickers[0][1]["text"]
            self.stickers[0][1]["text"] = temp_text2
            temp_text3 = self.stickers[1][2]["text"]
            self.stickers[1][2]["text"] = self.stickers[6][0]["text"]
            self.stickers[6][0]["text"] = self.stickers[7][2]["text"]
            self.stickers[7][2]["text"] = self.stickers[4][4]["text"]
            self.stickers[4][4]["text"] = self.stickers[0][2]["text"]
            self.stickers[0][2]["text"] = temp_text3
        
        elif face == 6:
            # Rotate the Purple FACE (6) counterclockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker > 1:
                    new_stickers[face][(sticker-2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 0:
                    new_stickers[face][8] = self.stickers[face][sticker]["text"]
                elif sticker == 1:
                    new_stickers[face][9] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[8][0]["text"]
            self.stickers[8][0]["text"] = self.stickers[9][0]["text"]
            self.stickers[9][0]["text"] = self.stickers[7][8]["text"]
            self.stickers[7][8]["text"] = self.stickers[5][2]["text"]
            self.stickers[5][2]["text"] = self.stickers[1][2]["text"]
            self.stickers[1][2]["text"] = temp_text1
            temp_text2 = self.stickers[8][1]["text"]
            self.stickers[8][1]["text"] = self.stickers[9][1]["text"]
            self.stickers[9][1]["text"] = self.stickers[7][9]["text"]
            self.stickers[7][9]["text"] = self.stickers[5][3]["text"]
            self.stickers[5][3]["text"] = self.stickers[1][3]["text"]
            self.stickers[1][3]["text"] = temp_text2
            temp_text3 = self.stickers[8][2]["text"]
            self.stickers[8][2]["text"] = self.stickers[9][2]["text"]
            self.stickers[9][2]["text"] = self.stickers[7][0]["text"]
            self.stickers[7][0]["text"] = self.stickers[5][4]["text"]
            self.stickers[5][4]["text"] = self.stickers[1][4]["text"]
            self.stickers[1][4]["text"] = temp_text3
        
        elif face == 7:
            # Rotate the Green FACE (7) counterclockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker > 1:
                    new_stickers[face][(sticker-2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 0:
                    new_stickers[face][8] = self.stickers[face][sticker]["text"]
                elif sticker == 1:
                    new_stickers[face][9] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[6][0]["text"]
            self.stickers[6][0]["text"] = self.stickers[9][2]["text"]
            self.stickers[9][2]["text"] = self.stickers[10][0]["text"]
            self.stickers[10][0]["text"] = self.stickers[4][0]["text"]
            self.stickers[4][0]["text"] = self.stickers[5][0]["text"]
            self.stickers[5][0]["text"] = temp_text1
            temp_text2 = self.stickers[6][1]["text"]
            self.stickers[6][1]["text"] = self.stickers[9][3]["text"]
            self.stickers[9][3]["text"] = self.stickers[10][1]["text"]
            self.stickers[10][1]["text"] = self.stickers[4][1]["text"]
            self.stickers[4][1]["text"] = self.stickers[5][1]["text"]
            self.stickers[5][1]["text"] = temp_text2
            temp_text3 = self.stickers[6][2]["text"]
            self.stickers[6][2]["text"] = self.stickers[9][4]["text"]
            self.stickers[9][4]["text"] = self.stickers[10][2]["text"]
            self.stickers[10][2]["text"] = self.stickers[4][2]["text"]
            self.stickers[4][2]["text"] = self.stickers[5][2]["text"]
            self.stickers[5][2]["text"] = temp_text3
        
        elif face == 8:
            # Rotate the Orange FACE (8) counterclockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker > 1:
                    new_stickers[face][(sticker-2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 0:
                    new_stickers[face][8] = self.stickers[face][sticker]["text"]
                elif sticker == 1:
                    new_stickers[face][9] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[11][8]["text"]
            self.stickers[11][8]["text"] = self.stickers[9][8]["text"]
            self.stickers[9][8]["text"] = self.stickers[6][4]["text"]
            self.stickers[6][4]["text"] = self.stickers[1][4]["text"]
            self.stickers[1][4]["text"] = self.stickers[2][4]["text"]
            self.stickers[2][4]["text"] = temp_text1
            temp_text2 = self.stickers[11][9]["text"]
            self.stickers[11][9]["text"] = self.stickers[9][9]["text"]
            self.stickers[9][9]["text"] = self.stickers[6][5]["text"]
            self.stickers[6][5]["text"] = self.stickers[1][5]["text"]
            self.stickers[1][5]["text"] = self.stickers[2][5]["text"]
            self.stickers[2][5]["text"] = temp_text2
            temp_text3 = self.stickers[11][0]["text"]
            self.stickers[11][0]["text"] = self.stickers[9][0]["text"]
            self.stickers[9][0]["text"] = self.stickers[6][6]["text"]
            self.stickers[6][6]["text"] = self.stickers[1][6]["text"]
            self.stickers[1][6]["text"] = self.stickers[2][6]["text"]
            self.stickers[2][6]["text"] = temp_text3
        
        elif face == 9:
            # Rotate the Teal FACE (9) counterclockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker > 1:
                    new_stickers[face][(sticker-2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 0:
                    new_stickers[face][8] = self.stickers[face][sticker]["text"]
                elif sticker == 1:
                    new_stickers[face][9] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[11][0]["text"]
            self.stickers[11][0]["text"] = self.stickers[10][8]["text"]
            self.stickers[10][8]["text"] = self.stickers[7][8]["text"]
            self.stickers[7][8]["text"] = self.stickers[6][2]["text"]
            self.stickers[6][2]["text"] = self.stickers[8][2]["text"]
            self.stickers[8][2]["text"] = temp_text1
            temp_text2 = self.stickers[11][1]["text"]
            self.stickers[11][1]["text"] = self.stickers[10][9]["text"]
            self.stickers[10][9]["text"] = self.stickers[7][9]["text"]
            self.stickers[7][9]["text"] = self.stickers[6][3]["text"]
            self.stickers[6][3]["text"] = self.stickers[8][3]["text"]
            self.stickers[8][3]["text"] = temp_text2
            temp_text3 = self.stickers[11][4]["text"]
            self.stickers[11][2]["text"] = self.stickers[10][0]["text"]
            self.stickers[10][0]["text"] = self.stickers[7][0]["text"]
            self.stickers[7][0]["text"] = self.stickers[6][4]["text"]
            self.stickers[6][4]["text"] = self.stickers[8][4]["text"]
            self.stickers[8][4]["text"] = temp_text3
        
        elif face == 10:
            # Rotate the Gold FACE (10) counterclockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker > 1:
                    new_stickers[face][(sticker-2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 0:
                    new_stickers[face][8] = self.stickers[face][sticker]["text"]
                elif sticker == 1:
                    new_stickers[face][9] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[3][6]["text"]
            self.stickers[3][6]["text"] = self.stickers[4][8]["text"]
            self.stickers[4][8]["text"] = self.stickers[7][4]["text"]
            self.stickers[7][4]["text"] = self.stickers[9][4]["text"]
            self.stickers[9][4]["text"] = self.stickers[11][2]["text"]
            self.stickers[11][2]["text"] = temp_text1
            temp_text2 = self.stickers[3][7]["text"]
            self.stickers[3][7]["text"] = self.stickers[4][9]["text"]
            self.stickers[4][9]["text"] = self.stickers[7][5]["text"]
            self.stickers[7][5]["text"] = self.stickers[9][5]["text"]
            self.stickers[9][5]["text"] = self.stickers[11][3]["text"]
            self.stickers[11][3]["text"] = temp_text2
            temp_text3 = self.stickers[3][8]["text"]
            self.stickers[3][8]["text"] = self.stickers[4][0]["text"]
            self.stickers[4][0]["text"] = self.stickers[7][6]["text"]
            self.stickers[7][6]["text"] = self.stickers[9][6]["text"]
            self.stickers[9][6]["text"] = self.stickers[11][4]["text"]
            self.stickers[11][4]["text"] = temp_text3
        
        elif face == 11:
            # Rotate the Silver FACE (11) counterclockwise 
            new_stickers = [[0]*10 for _ in range(12)]
            for sticker in range(10):
                if sticker > 1:
                    new_stickers[face][(sticker-2)%10] = self.stickers[face][sticker]["text"]
                elif sticker == 0:
                    new_stickers[face][8] = self.stickers[face][sticker]["text"]
                elif sticker == 1:
                    new_stickers[face][9] = self.stickers[face][sticker]["text"]

            # Update labels with new positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker]

            # Swap Faces with corresponding sticker positions
            for sticker in range(10):
                self.stickers[face][sticker]["text"] = new_stickers[face][sticker] 
            temp_text1 = self.stickers[2][6]["text"]
            self.stickers[2][6]["text"] = self.stickers[3][6]["text"]
            self.stickers[3][6]["text"] = self.stickers[10][6]["text"]
            self.stickers[10][6]["text"] = self.stickers[9][6]["text"]
            self.stickers[9][6]["text"] = self.stickers[8][4]["text"]
            self.stickers[8][4]["text"] = temp_text1
            temp_text2 = self.stickers[2][7]["text"]
            self.stickers[2][7]["text"] = self.stickers[3][7]["text"]
            self.stickers[3][7]["text"] = self.stickers[10][7]["text"]
            self.stickers[10][7]["text"] = self.stickers[9][7]["text"]
            self.stickers[9][7]["text"] = self.stickers[8][5]["text"]
            self.stickers[8][5]["text"] = temp_text2
            temp_text3 = self.stickers[2][8]["text"]
            self.stickers[2][8]["text"] = self.stickers[3][8]["text"]
            self.stickers[3][8]["text"] = self.stickers[10][8]["text"]
            self.stickers[10][8]["text"] = self.stickers[9][8]["text"]
            self.stickers[9][8]["text"] = self.stickers[8][6]["text"]
            self.stickers[8][6]["text"] = temp_text3
    def solve(self):
        # Implement the solving logic here
        messagebox.showinfo("Solved", "Megaminx solved!")

# Create a Tkinter window
root = tk.Tk()

# Create an instance of MegaminxGUI
megaminx_gui = MegaminxGUI(root)

# Start the Tkinter event loop
root.mainloop()
