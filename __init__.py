import stat
import re
from typing import Self

"""https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f"""

square = int

color = int

piece = int


RANKS_NAME = ["a", "b", "c", "d", "e", "f", "g", "h"]

FILES_NAME = ["1", "2", "3", "4", "5", "6", "7", "8"]

SQUARES_NAME = [f + r for r in RANKS_NAME for f in FILES_NAME]

COLORS_NAME = ["white", "black", "yellow", "none"] #upper, lower, @, .

PIECES_TYPE_NAME = ["k" ,"q" ,"r", "n", "b", "p", "@", "."]

PIECES_NAME = ["K", "Q", "R", "N", "B", "P", "k", "q", "r", "n", "b" , "p", "d", "."]

PIECES_UNICODE= ["♔", "♕", "♖", "♘", "♗", "♙", "♚", "♛", "♜", "♞", "♝", "♟︎", "🦆", "."]

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

COLORS = [white, black ,yellow, none] = range(4)

PIECETYPES = [t_k, t_q, t_r, t_n, t_b, t_p, t_d, t_space] = range (8)

PIECES = [K, Q, R, N, B, P, k, q, r, n, b, p, d, space] = range(14)


DISPLAY = [
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ]

EMPTY = [
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    ]

aaaa = [
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,6,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,0,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    ]


class Board :
    
    B_BOARD = [
            B_A1, B_B1, B_C1, B_D1, B_E1, B_F1, B_G1, B_H1,
            B_A2, B_B2, B_C2, B_D2, B_E2, B_F2, B_G2, B_H2,
            B_A3, B_B3, B_C3, B_D3, B_E3, B_F3, B_G3, B_H3,
            B_A4, B_B4, B_C4, B_D4, B_E4, B_F4, B_G4, B_H4,
            B_A5, B_B5, B_C5, B_D5, B_E5, B_F5, B_G5, B_H5,
            B_A6, B_B6, B_C6, B_D6, B_E6, B_F6, B_G6, B_H6,
            B_A7, B_B7, B_C7, B_D7, B_E7, B_F7, B_G7, B_H7,
            B_A8, B_B8, B_C8, B_D8, B_E8, B_F8, B_G8, B_H8,
    ] = list(aaaa)

    B_Passent = int

    B_Castle = [bool, bool, bool, bool]

    B_HalfClock = int

    B_FullClock = int

    B_Side = bool



class Decode :

    #convert The name of a square to its coordinate
    @staticmethod
    def SquareN(Square) :
        for i, rank in enumerate(RANKS_NAME) :
            if rank == Square[0].lower() :
                return (int(Square[1]) - 1) * 8 + i
        return None

    #return the square's rank
    def File(Square: square) :
        Square = Square % 8
        return Square

    def Rank(Square: square) :
        Square = Square // 8
        return Square
    
    @staticmethod
    def OnEdge(Square: square) :
        return Decode.Rank(Square) in [0, 7] or Decode.File(Square) in [0, 7]

    @staticmethod
    def FEN_to_BOARD(fen, part) :
        fen_parts = fen.split()
        match part :
            case 0 :
                fen_board = fen_parts[0]
                board = []

                for char in fen_board :
                    if char.isdigit() :
                        board.extend([13] * int(char))
                    elif char in PIECES_NAME :
                        board.append(PIECES_NAME.index(char))
                return board
            case 1 :
                if fen_parts[1] == "w" :
                    return 0
                else :
                    return 1
            case 2 :
                fen_castle = fen_parts[2]
                all_castle = ["K", "Q", "k", "q"]
                castle = [False, False, False, False]
                for i, char in enumerate(castle) :
                    if char == fen_castle[i] :
                        castle[i] = True
                return castle
            case 3 :
                if fen_parts[3] == "-" :
                    return None
                else :
                    return Decode.SquareN(fen_parts[3])
            case _ :
                return fen_parts[part]
            
    @staticmethod
    def BOARD_to_FEN() :
        return



class Map :

    def __init__(self, Board, Color: color) :

        self.Board = Board
        self.Color = Color

        self.ColorMap = self.ColorType()
        self.PieceMap = self.PieceType()
        self.AttackedMap = self.Attacked()
        #self.DeffededMap = self.Deffended()
    
    def ColorType(self) : 
        colorMap = list(EMPTY)
        for i, Square in enumerate(self.Board) :
            if Square <= 5 :
                colorMap[i] = 0
            elif Square <= 11 :
                colorMap[i] = 1
            elif Square == 12 :
                colorMap[i] = 2
            else :
                colorMap[i] = 3
        return colorMap

    def PieceType(self) :
        typeMap = list(EMPTY)
        for i, Square in enumerate(self.Board) :
            if Square == 12 :
                typeMap[i] = 6
            elif Square == 13 :
                typeMap[i] = 7
            else :
                typeMap[i] = Square % 8
        return typeMap
    
    @staticmethod
    def Attacked(self) :
        if self.Side != None :
            attacked = []
            for i in range(64) :
                if bool(self.ColorMap[i]) == self.Side and self.ColorMap[i] <= 1 :
                    current_moves = Moves(i, None, None, None)
                    match self.PieceMap[i] :                   
                        case 0 :
                            attacked += current_moves.king()
                        case 1 :    
                            attacked += current_moves.straight()
                            attacked += current_moves.diagnal()
                        case 2 :
                            attacked += current_moves.straight()
                        case 3 :
                            attacked += current_moves.knight()
                        case 4 :
                            attacked += current_moves.diagnal()
                        case 5 :
                            attacked += current_moves.pawn()

                    current_moves = Moves(i, None, True, None)
                    match self.PieceMap[i] :                   
                        case 0 :
                            attacked += current_moves.king()
                        case 1 :    
                            attacked += current_moves.straight()
                            attacked += current_moves.diagnal()
                        case 2 :
                            attacked += current_moves.straight()
                        case 3 :
                            attacked += current_moves.knight()
                        case 4 :
                            attacked += current_moves.diagnal()
                        case 5 :
                            attacked += current_moves.pawn()
            attacked = list(set(attacked))
            return attacked
        else :
            return
                
                               

class Moves :
    
    def __init__(self, Start: square, End: square, attack = None, Side = None) :
        
        self.Start = Start
        self.End = End
        self.attack = attack
        self.Side = Side 

        self.Map = Map(Board.B_BOARD, )
        
        self.Piece = self.Map.PieceMap()[self.Start]
        self.Color = self.Map.ColorMap()[self.Start]
        
    def diagnal(self) :
        moves = []
        attacks = [] 
        offsets = [7, -7, 9, -9]

        for offset in offsets :
            move = self.Start + offset
            while move in range(64) and abs(move % 8 - self.Start % 8) == abs(move // 8 - self.Start // 8):
                if Map.ColorType()[move] == 3 :
                    moves.append(move)
                    move += offset
                elif Map.ColorType()[move] == int(not bool(self.Color)) :
                    attacks.append(move)
                    break

        if self.attack :
            return attacks
        else :
            return moves

    def straight(self) :
        moves = []
        attacks = [] 
        offsets = [1,-1,8,-8]

        for offset in offsets :
            move = self.Start + offset
            while move in range(64) and (self.Start // 8 == move // 8 or self.Start % 8 == move % 8):
                if Map.ColorType()[move] == 3 :
                    moves.append(move)
                    move += offset
                elif Map.ColorType()[move] == int(not bool(self.Color)) :
                    attacks.append(move)
                    break

        if self.attack :
            return attacks
        else :
            return moves

    def knight(self) :
        moves = []
        attacks = [] 
        offsets = [6, 10, 15, 17, -6, -10, -15, -17]

        for offset in offsets :
            move = self.Start + offset
            if move in range(64) and abs(move % 8 - self.Start % 8) <= 2 and abs(move // 8 - self.Start // 8) <= 2 :
                if Map.ColorType()[move] == 3 :
                    moves.append(move)
                elif Map.ColorType()[move] == int(not bool(self.Color)) :
                    attacks.append(move)

        if self.attack :
            return attacks
        else :
            return moves
    
    def pawn(self) :
        moves = []
        attacks = []
        offsets = []
        atteckoffsets = [1, -1]
        foward = 0

        if bool(self.Color) :
               foward = -8
        else :
               foward = 8

        if self.attack :
            for offset in atteckoffsets :
                offsets.append(foward + offset)
        else :
            if self.Start < 15 or self.Start > 48 :
               offsets.append(foward * 2)
            offsets.append(foward)

            
        for offset in offsets :
            move = self.Start + offset
            if move in range(64) and abs(self.Start % 8 - move % 8) <= 1 :
                if Map.ColorType()[move] == 3 :
                    moves.append(move)
                elif Map.ColorType()[move] == int(not bool(self.Color)) :
                    attacks.append(move)
        
        if self.attack :
            return attacks
        else :
            return moves

    def king(self) :
        moves = []
        attacks = []
        offsets = [-9, -8, -7, -1 , 1, 7, 8, 9]
        
        for offset in offsets :
            move = self.Start + offset
            if move in range(64) and (abs(move // 8 - self.Start // 8) <= 1 or abs(move % 8 - self.Start % 8) <= 1) :
                if Map.ColorType()[move] == 3 :
                    moves.append(move)
                elif Map.ColorType()[move] == int(not bool(self.Color)) or Map.passentable :
                    attacks.append(move)

        if self.attack :
            return attacks
        else :
            return moves

    def castle(self):
        move = None
        if bool(self.Color) :
            #black king side castle
            if self.Side :
                if Board.B_Castle[0] == False :
                    return move
                for i in range (61,63) :
                    if Map.PieceType()[i] != 7 :
                        return move
                if self.Piece :
                    move = 62
                else :
                    move = 61
            #black queen side castle
            else :
                if Board.B_Castle[1] == False :
                    return move
                for i in range (57,60) :
                    if Map.PieceType()[i] != 7 :
                        return move
                if self.Piece :
                    move = 58
                else :
                    move = 59
        else :
            #white king side castle
            if self.Side :
                if Board.B_Castle[2] == False :
                    return move
                for i in range (5,7) :
                    if Map.PieceType()[i] != 7 :
                        return move
                if self.Piece :
                    move = 6
                else :
                    move = 5
            #white queen side castle        
            else :
                if Board.B_Castle[3] == False :
                    return move
                for i in range (1,4) :
                    if Map.PieceType()[i] != 7 :
                        return move
                if self.Piece :
                    move = 2
                else :
                    move = 3
        return move
    
    def move(self) :

        AttackMap = Map(Board.B_BOARD, self.Color)

        if self.Side :
            moves = []
            for Square, i in enumerate(self.Map.PieceMap) :
                if i == self.Piece and self.Map.ColorMap[Square] == self.Color :
                    match self.Piece :                   
                        case 0 :
                            moves += self.king()
                            moves = [i for i in moves if i not in AttackMap.Attacked()]            
                        case 1 :    
                            moves += self.straight()
                            moves += self.diagnal()
                        case 2 :
                            moves += self.straight()
                        case 3 :
                            moves += self.knight()
                        case 4 :
                            moves += self.diagnal()
                        case 5 :
                            moves += self.pawn()
            return moves                                

class Game :

    def clear() :
        Board = list(EMPTY)

    def fen_import(fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1") :
        Board.B_BOARD = Decode.FEN_to_BOARD(fen)

    def start() :
        Input = input('.')
        
        return

    def move(pgn_move) :

        move = pgn_move.split("@")
        
        pattern = r"([NBRQKnbrqk]?)([1-8]?)(x?)([a-h]?[1-8]?)"
        match = re.match(pattern, move[0])

        if match :
            Piece, File, attack, destination = match.groups()

            if not Piece :
                Piece = "P"
            Piece = PIECES[Piece]

        Color = Board.B_Side

        destination = Decode.SquareN(destination)

        return Piece, Color, attack, destination, move[1]

    
