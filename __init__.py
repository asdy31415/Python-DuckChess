from ast import If
import collections
import copy
import dataclasses
import enum
import math
from msilib.schema import Class
import re
import itertools
from string import octdigits
import typing

from typing import ClassVar, Callable, Counter, Dict, Generic, Hashable, Iterable, Iterator, List, Mapping, Optional, SupportsInt, Tuple, Type, TypeVar, Union

square = int

RANKS_NAME = ["a", "b", "c", "d", "e", "f", "g", "h"]

FILES_NAME = ["1", "2", "3", "4", "5", "6", "7", "8"]

SQUARES = [
    A1, B1, C1, D1, E1, F1, G1, H1,
    A2, B2, C2, D2, E2, F2, G2, H2,
    A3, B3, C3, D3, E3, F3, G3, H3,
    A4, B4, C4, D4, E4, F4, G4, H4,
    A5, B5, C5, D5, E5, F5, G5, H5,
    A6, B6, C6, D6, E6, F6, G6, H6,
    A7, B7, C7, D7, E7, F7, G7, H7,
    A8, B8, C8, D8, E8, F8, G8, H8,
    ] = range(64)

SQUARES_NAME = [f + r for r in RANKS_NAME for f in FILES_NAME]

EMPTY = [".", ".", ".", ".", ".", ".", ".", ".",
         ".", ".", ".", ".", ".", ".", ".", ".",
         ".", ".", ".", ".", ".", ".", ".", ".",
         ".", ".", ".", ".", ".", ".", ".", ".",
         ".", ".", ".", ".", ".", ".", ".", ".",
         ".", ".", ".", ".", ".", ".", ".", ".",
         ".", ".", ".", ".", ".", ".", ".", ".",
         ".", ".", ".", ".", ".", ".", ".", ".",
         ]

BOARD = [
    B_A1, B_B1, B_C1, B_D1, B_E1, B_F1, B_G1, B_H1,
    B_A2, B_B2, B_C2, B_D2, B_E2, B_F2, B_G2, B_H2,
    B_A3, B_B3, B_C3, B_D3, B_E3, B_F3, B_G3, B_H3,
    B_A4, B_B4, B_C4, B_D4, B_E4, B_F4, B_G4, B_H4,
    B_A5, B_B5, B_C5, B_D5, B_E5, B_F5, B_G5, B_H5,
    B_A6, B_B6, B_C6, B_D6, B_E6, B_F6, B_G6, B_H6,
    B_A7, B_B7, B_C7, B_D7, B_E7, B_F7, B_G7, B_H7,
    B_A8, B_B8, B_C8, B_D8, B_E8, B_F8, B_G8, B_H8,
    ] = EMPTY

class Decode :

    #convert The name of a square to its coordinate
    def SquareN(Square) :
        for i, rank in enumerate(RANKS_NAME) :
            if rank == Square[0].lower() :
                return (int(Square[1]) - 1) * 8 + i
        return None

    #return the square's rank
    def Rank(Square: square) :
        Square = Square % 8 + 1
        return Square

    def File(Square: square) :
        Square = Square // 8
        return Square

class Board:
    def occupied(Square: square, Color) :
        oc = []
        for i, square in enumerate(BOARD) :
            match Color :
                case None :
                    
                case 0 :
                    
                case 1 :
               
                
        for j in oc :
            if Square == oc :
                return True
            break
        return False


class Moves :

    def diagnal(Square: square, attack) :
        moves = []
        attacks = [] 
        offsets = [7, -7, 9, -9]

        for offset in offsets :
            move = Square + offset
            while move in range(64) and not (offset == -7 and move % 8 == 7) or (offset == -9 and move % 8 == 0) or  not (offset == 7 and move % 8 == 0) or (offset == 9 and move % 8 == 7) :
                if not Board.occupied(Square) :
                    moves.append(move)
                    move += offset
                else :
                    attacks.append(move)
                    break

        if attack :
            return attacks
        else :
            return moves

    def straight(Square: square, attack) :
        moves = []
        attacks = [] 
        offsets = [1,-1,8,-8]

        for offset in offsets :
            move = Square + offset
            while move in range(64) and (move // 8 == Square // 8 or offset == 8 or offset == -8) :
                    if not Board.occupied(Square) :
                        moves.append(move)
                        move += offset
                    else :
                        attacks.append(move)
                        break

        if attack :
            return attacks
        else :
            return moves

    def knight(Square: square, attack) :
        moves = []
        attacks = [] 
        offsets = [6, 10, 15, 17, -6, -10, -15, -17]

        for offset in offsets :
            move = Square + offset
            if move in range(64) and abs(move % 8 - Square % 8) <= 2 and abs(move // 8 - Square // 8) <= 2 :
                if not Board.occupied(Square) :
                    moves.append(move)
                else :
                    attacks.append(move)

        if attack :
            return attacks
        else :
            return moves
    
    def pawn() :

        return

    def king(Square: square, attack) :
        moves = []
        attacks = []
        offsets = [-9, -8, -7, -1 , 1, 7, 8, 9]
        
        for offset in offsets :
            move = Square + offset
            if move in range(64) and abs(move % 8 - Square % 8) <= 1 and abs(move // 8 - Square // 8) <= 1 :
                if not Board.occupied(Square) :
                    move.append(move)
                else :
                    attacks.append(move)

        return

class Map :

    def attack() :

        return

    def defend() :

        return

    def passentable() :

        return

    def occupied() :
    
class PieceMap :

