#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 21:18:42 2025

@author: hgtllys
"""
import numpy as np

def two_rocks_game(n, m):
    n, m = n + 1, m + 1
    game = np.zeros((n, m))
    
    for i in range(n):
        game[i, 0] = i % 2
    for j in range(m):
        game[0, j] = j % 2
    
    for i in range(1, n):
        for j in range(1, m):
            game[i, j] = not (game[i-1,j] and game[i,j-1] and game[i-1,j-1])
    
    return game


def another_two_rocks_game(n, m):
    n, m = n + 1, m + 1
    game = np.zeros((n, m))
    
    for i in range(0, n):
        for j in range(0, m):
            if i != 0 or j != 0:
                for l in range(4):
                    for r in range(4):
                        if l != 0 or r != 0:
                            di = i - l
                            dj = j - r
                            if di >= 0 and dj >= 0:
                                if game[di, dj] == 0:
                                    game[i, j] = 1
    
    return game


if __name__ == "__main__":
    
    n, m = 10, 10
    game = two_rocks_game(n, m)
    