#tensor.py
import random
import matplotlib.pyplot as plt
import numpy as np

class Tensor:

    def __init__(self,r,c,h,initial_array = None):
        '''
        Where
        r = row
        c = column
        h = height
        initial_array   = if there is already an array, insert to this variable
        '''
        # Instantiate
        self.r = r
        self.c = c
        self.h = h
        self.shape = (r,c,h)
        n = max(r,c,h)
        self.MC = ((n * ( (n ** 3)+1))/2)

        
        # Auto make tensor  r x c x h   with heigth h
        self.array = []
        

        # Inialize the tensor with value 0
        if initial_array is not None:
            self.array = np.array(initial_array)
        else:
            for _ in range(h):
                h_array = []
                for _ in range(r):
                    j_array = [0] * c
                    h_array.append(j_array)
                self.array.append(h_array)
            self.array = np.array(self.array)


    def print_tensor(self):
        level = self.h
        for height in self.array:
            print(f"Level {len(height)-level+1}: \n")
            level = level - 1
            for row in height:
                print(row)
            print()

    def plot_cube(self,title="Tensor Cube"):
        fig = plt.figure(figsize=(15,15))
        ax = fig.add_subplot(111,projection="3d")
        ax.set_box_aspect([self.r, self.c, self.h])

        for h in range(self.h):
            for r in range(self.r):
                for c in range(self.c):
                    ax.text(r,c,h,f"{self.array[h][r][c]}",ha="center",va="center",fontsize=14,color="blue")
                    ax.scatter(r,c,h,c="orange",s=500,edgecolors="k",alpha=0.4)
            
        ax.set_xlabel("column-axis")
        ax.set_ylabel("row-axis")
        ax.set_zlabel("level")
        plt.title(title)
        return plt.show()
    
    def plot_per_level(self,title="Tensor Cube"):
         for h in range(self.h):
            fig = plt.figure(figsize=(8, 8))
            ax = fig.add_subplot(111, projection="3d")
            ax.set_box_aspect([self.r, self.c, 1])

            # Plot cells within the current level
            for r in range(self.r):
                for c in range(self.c):
                    ax.text(r, c, 0, f"{self.array[h][r][c]}", ha="center", va="center", fontsize=14, color="blue")
                    ax.scatter(r, c, 0, c="orange", s=500, edgecolors="k", alpha=0.4)

            # Labels and title
            ax.set_xlabel("Column-axis")
            ax.set_ylabel("Row-axis")
            ax.set_zlabel("Level")
            plt.title(f"{title} - Level {h + 1}")
            plt.show()

    def same_tensor(self,tensor):
        '''
        Function to check whether the tensor is same or not
        
        '''
        if self.array.shape != tensor.array.shape:
            return False
        
        for heigth in range(self.h):
            for row in range(self.r):
                for col in range(self.c):
                    if self.array[heigth,row,col] != tensor.array[heigth,row,col]:
                        return False
        return True
                            
    
    def is_in_tensor(self, v):
        '''
        Function to check whether the value in the tensor or not
        
        '''
        for height in self.array:
            for row in height:
                if v in row:
                    return True
        return False
    
    def max_len(self):
        return max(self.r,self.c,self.h)

    def initial_state(self):
        '''
        Function to make initial state the tensor

        Requirements:
        Values in range 1 to  n^3 
        where:
        n^3 is max(r,c,h)

        and there are no same value in it

        '''
        n = self.max_len()
        n = n ** 3

        for height in self.array:
            for row in height:
                for col in range(len(row)):
                    v = random.randint(1, n)
                    while self.is_in_tensor(v):
                        v = random.randint(1, n)
                    row[col] = v
        return self
    
    def randomize_value(self):
        n = self.max_len() ** 3
        shape = self.array.shape
        num_swaps = n // 2
        for _ in range(num_swaps):
            first = (np.random.randint(0, shape[0]), 
                    np.random.randint(0, shape[1]), 
                    np.random.randint(0, shape[2]))
            second = first
            while second == first:
                second = (np.random.randint(0, shape[0]), 
                        np.random.randint(0, shape[1]), 
                        np.random.randint(0, shape[2])) 
            self.array[first], self.array[second] = self.array[second], self.array[first]
        return self
                    
                    

    '''
    Magic Cube Functions
    '''
    
    def straight_line(self):
        n = self.max_len()
        return  3 * n ** 2 + 6* n + 4
    
    def objective_function(self,square_error=True):
        '''
        - Summation of all rows in each level = MC V
        - Summation of all columns in each level = MC V
        - Sumation of the main diagonal in each level = MC V
        - Summation all pillars through levels = MC V
        - Summation diagonal spaces from upper right to down left = MC V
        - Summation diagonal spaces from upper left to down right = MC V
        - Summation of all cols in each row = MC V
        - Summation of all row in each col = MC V
        Reference:
        https://www.magischvierkant.com/three-dimensional-eng/magic-features
        '''
        Z = 0
        n = self.max_len()
        if square_error == True:
            # Row, Column, and Level
            for i in range(n):
                for j in range(n):
                    row_sum = np.sum(self.array[i,j,:])

                    Z += (row_sum - self.MC) ** 2
                    col_sum = np.sum(self.array[i,:,j])

                    Z += (col_sum - self.MC) ** 2 

                    pillar_sum = np.sum(self.array[:,i,j])
                    Z += (pillar_sum - self.MC) ** 2
            # Main Diagonal
            for level in range(self.h):
                main_diagonal_left = 0
                main_diagonal_right = 0
                for i in range(self.r):
                    main_diagonal_left += self.array[level, i, i]
                    main_diagonal_right += self.array[level, i, self.h-1-i]
                Z += (main_diagonal_left - self.MC) ** 2
                Z += (main_diagonal_right - self.MC) ** 2

            # Diagonal Spaces
            space_diagonal_left = 0
            space_diagonal_right = 0
            for i in range(self.max_len()):
                space_diagonal_left += self.array[self.h - (self.h - i),i,i]
                space_diagonal_right += self.array[i,i, self.h - 1 - i]
            Z += (space_diagonal_left - self.MC) ** 2
            Z += (space_diagonal_right - self.MC) ** 2

            # Space Summation 
            for i in range(self.max_len()):
                space_row = 0
                space_col = 0
                for j in range(self.max_len()):
                    space_row += self.array[self.h - (self.h - j),i,self.c - (self.c - j)]
                    space_col += self.array[self.h - (self.h - j),self.r - (self.r - j),i]
                Z += (space_row - self.MC) ** 2
                Z += (space_col - self.MC) ** 2
        else:
            # Row, Column, and Level
            for i in range(n):
                for j in range(n):
                    row_sum = np.sum(self.array[i,j,:])

                    Z += np.abs((row_sum - self.MC))
                    col_sum = np.sum(self.array[i,:,j])

                    Z += np.abs((col_sum - self.MC)  )

                    pillar_sum = np.sum(self.array[:,i,j])
                    Z += np.abs((pillar_sum - self.MC) )



            # Main Diagonal
            for level in range(self.h):
                main_diagonal_left = 0
                main_diagonal_right = 0
                for i in range(self.r):
                    main_diagonal_left += self.array[level, i, i]
                    main_diagonal_right += self.array[level, i, self.h-1-i]
                Z += np.abs((main_diagonal_left - self.MC)) 
                Z += np.abs((main_diagonal_right - self.MC) )

            # Diagonal Spaces
            space_diagonal_left = 0
            space_diagonal_right = 0
            for i in range(self.max_len()):
                space_diagonal_left += self.array[self.h - (self.h - i),i,i]
                space_diagonal_right += self.array[i,i, self.h - 1 - i]
            Z += np.abs((space_diagonal_left - self.MC) )
            Z += np.abs((space_diagonal_right - self.MC) )

            # Space Summation 
            for i in range(self.max_len()):
                space_row = 0
                space_col = 0
                for j in range(self.max_len()):
                    space_row += self.array[self.h - (self.h - j),i,self.c - (self.c - j)]
                    space_col += self.array[self.h - (self.h - j),self.r - (self.r - j),i]
                Z += np.abs((space_row - self.MC) )
                Z += np.abs((space_col - self.MC) )
        return Z