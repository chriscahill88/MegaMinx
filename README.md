# MegaMinx
CS463 MegaMinx
10 pts - Description of data structure:
The data structures that our group used were homogeneous data structures. We used lists of lists and dictionaries. We used dictionaries to store the information about the faces on each cube. We then started using lists of lists to hold the current positions when the cubes are rearranged/rotated.  

15 pts - Code for data structure and how to run:
 https://github.com/chriscahill88/MegaMinx A link to the code for the megaminx and randomizer can be found here to test the code.
In order to run this you need to install the latest version of python. Tkinter is the standard GUI library for python, which means it should already be included. On VScode there should be a play button to run the code. Once it does a window will show up as shown below:Dee


15 pts - Example of GUI output:

In the File

10 pts - Description of randomizer:
How our randomizer works starts with generating a default or you could say already solved Megamix. This is important because if we generated a Megamix with randomized sides and edges, the Megamix would not be reflective of a real Megamix, and thus not even solvable. Next, you type into the GUI the number of moves you'd like to make, why this is random is because the code picks a random face and turns each randomly selected face one time. It is also important to note that each face only turns clockwise when this is done. The importance of this feature is understood when realizing that if a face moved both clockwise and or counter clockwise, the code for this feature becomes more complicated/bulky to write, potentially takes up more memory, and removes the possibility for contradiction by moving a face clockwise and then moving it counterclockwise in succession, or vise versa. After each move, each array is updated to reflect the changes made after each move. 

15 pts - Code for randomizer and how to run:
Run the code given and in the GUI a section is allocated to allow for input of the amount of random moves desired. After that amount of moves is inputed, click the randomize button and that amount of random moves will happen

10 pts - Heuristic (clearly described and justified, including argument that is admissible):
Our heuristic, which is both an approximation of the number of steps to the solved state and admissible, will meet this criteria by seeing how many misplaced cubes there are compared to a solved Megaminx. Our heuristic will be measured by evaluating the number of misplaced cubes on the megaminx with the intent of minimizing this number which would signal that the puzzle is closer to being solved.
This heuristic is also admissible because it is guaranteed to not be greater than the actual number of steps to solve a megaminx. This is true because it cannot overestimate the actual number of moves required to solve the megaminx since it approximates the minimum number of moves to correct the misplaced cubes. 

8 pts - Statement of what was learned from this assignment:
Throughout this project we went in depth of trying to understand data structures before attempting to do anything. The use of homogenous data structures creates a pathway for us to develop a plan for constructing the megaminx. With first understanding how homogenous data structures worked as a process of using arrays to develop positions for each tile we would then be able to develop a randomizer to manipulate the megaminx in a randomized fashion that wouldn't create any complications. We learned that in order to make the randomization work we would need to understand the limitation of the megaminx and how a moved tile had to match two adjacent tiles. We also learned how to improve this before and during the process of solving it. Since there was an increased understanding of how to implement homogenous data structures, there would be a way of efficiently creating a Class or object to reduce the bulk of the code. Each face required 30 lines of code, with a class we could reduce it so that we could limit it to one set of lines of code. There’s also the need to improve our GUI representation. As of now, the representation could get quite confusing to understand. As a starter, the representation gives us an understanding of the positions of megaminx pieces. With it we could create a 2d representation of the megaminx with the positions aligned in a way to be able to solve it. 
