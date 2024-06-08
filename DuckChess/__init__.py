import re

square = int

color = int

piece = int

board = list

RANKS_NAME = ["1", "2", "3", "4", "5", "6", "7", "8"]

FILES_NAME = ["a", "b", "c", "d", "e", "f", "g", "h"]

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

class Game:
    def __init__(self, B_Board: board, B_Side: bool, B_Castle: list, B_Passent = int, B_HalfClock = int, B_FullClock = int):
    
        self.B_Board = B_Board

        self.B_Side = B_Side

        self.B_Castle = B_Castle
    
        self.B_Passent = B_Passent

        self.B_HalfClock = B_HalfClock

        self.B_FullClock = B_FullClock

    def flipSide(self):
        B_Board = []
        
        for i in range(7, -1, -1):
            B_Board.append(self.B_Board[i * 8:(i + 1) * 8])

        for Square in B_Board:
            if(Square < 6):
                Square += 6
            elif(Square < 12):
                Square += -6

        FlipedBoard = Game(B_Board, not self.B_Side, [self.B_Castle[2], self.B_Castle[3], self.B_Castle[0], self.B_Castle[1]], self.B_Passent, self.B_HalfClock, self.B_FullClock)
        return FlipedBoard

class Convertion:

    #convert The name of a square to its coordinate
    @staticmethod
    def SquareNum(Square: str):
        return SQUARES_NAME.index(Square)
    
    #convert The number of a square to its name        
    @staticmethod
    def SquareName(Square: square):
        return SQUARES_NAME[Square]

    #return the square's file
    @staticmethod
    def File(Square: square):
        return Square % 8
	
    #return the square's rank
    @staticmethod
    def Rank(Square: square):
        return Square // 8
    
    @staticmethod
    def OnEdge(Square: square):
        return Convertion.Rank(Square) in [0, 7] or Convertion.File(Square) in [0, 7]
    
    @staticmethod
    def Piece_to_Type(Piece: piece):
        if Piece >= 12:
            return Piece - 6
        else:
            return Piece % 6

    @staticmethod
    def FEN_to_BOARD(fen: str, part: int):
        fen_parts = fen.split()
        match part:
            case 0:
                fen_parts[0] = fen_parts[0].split("/")
                fen_board = "".join(fen_parts[0][::-1])
                Board = []

                for char in fen_board:
                    if char.isdigit():
                        Board.extend([13] * int(char))
                    elif char in PIECES_NAME:
                        Board.append(PIECES_NAME.index(char))
                return Board
            case 1:
                if fen_parts[1] == "w":
                    return 0
                else:
                    return 1
            case 2:
                castle = ["K" in fen_parts[2], "Q" in fen_parts[2], "k" in fen_parts[2], "q" in fen_parts[2]]
                return castle
            case 3:
                if fen_parts[3] == "-":
                    return None
                else:
                    return Convertion.SquareNum(fen_parts[3])
            case _:
                return fen_parts[part]
            
    @staticmethod
    def BOARD_to_FEN(Game: Game):

        fen = []
        space_count = None
        
        for i in range(64):
            if (i + 1) % 8 == 0:
                fen.append("/")
            if Game.B_Board[i] == 13:
                space_count += 1
            else:
                if space_count:
                    fen.append(space_count)
                    space_count = None    
            fen.appaend(PIECES_NAME[i])
        fen.reverse()
        
        fen.append(" " + "b" if Game.B_Side else "w")
        
        fen.append(" ")
        fen.append("K" if Game.B_Castle[0] else "")
        fen.append("Q" if Game.B_Castle[1] else"")
        fen.append("k" if Game.B_Castle[2] else"")
        fen.append("q" if Game.B_Castle[3] else"")
        
        fen.append(" " + "-" if not Game.B_Passent else Convertion.SquareName(Game.B_Passent))
        
        fen.append(" " + Game.B_HalfClock)
        
        fen.append(" " + Game.B_FullClock)
        
        return fen
    
    #return PieceType, PieceColor, Taking a piece or not, where it's going, and duck destination 
    @staticmethod
    def PGN_to_Move(pgn_move: str, currentGame: Game):
        Side = currentGame.B_Side

        if pgn_move[0] == "O":
            if pgn_move.count("O") == 2:
                return 0
            else:
                return 1
            
        elif pgn_move[0] == "o":    
            if pgn_move.count("o") == 2:
                return 2
            else:
                return 3
            
        else:
            move = pgn_move.split("@")
            if move[0][-1] == "#":
                move = move[0][:-1] 
            End = Convertion.SquareNum(move[0][-2::])
            move[0] = move[0][:-2]
            pattern = r"([NBRQKnbrqk]?)([a-h]?[1-8]?)(x?)"
            match = re.match(pattern, move[0])

            if match:
                Piece, Pos, attack = match.groups()
                Piece = "P" if Piece else "p"
                attack = True if attack == "x" else False 
                Piece = PIECES[eval(Piece)]

            PieceMap = Map(currentGame.B_Board).PieceMap
            ColorMap = Map(currentGame.B_Board).ColorMap

            Start = []

            for Square, i in enumerate(PieceMap):

                if i == Convertion.Piece_to_Type(Piece) and bool(ColorMap[Square]) == Side:
                    currentMove = Moves(Square, currentGame.B_Board)
                    match i:                   
                        case 0:
                            if End in currentMove.king(attack):
                                Start.append(Square)
                        case 1:    
                            if End in currentMove.straight(attack) or End in currentMove.diagnal(attack):
                                Start.append(Square)
                        case 2:
                            if End in currentMove.straight(attack):
                                Start.append(Square)
                        case 3:
                            if End in currentMove.knight(attack):
                                Start.append(Square)
                        case 4:
                            if End in currentMove.diagnal(attack):
                                Start.append(Square)
                        case 5:
                            if End in currentMove.pawn(attack):
                                Start.append(Square)
            if len(Start) > 1:
                if Pos.isdigit():
                    Pos = RANKS_NAME.index(Pos)
                    for Square in Start:
                        if Convertion.Rank(Square) == Pos:
                            Start = Square
                else:
                    Pos = FILES_NAME.index(Pos)
                    for Square in Start:
                        if Convertion.File(Square) == Pos:
                            Start = Square
            else:
                Start = Start[0]                

            return [Start, attack, Side, move[1]]
        
    @staticmethod
    def FEN_to_GAME(fen: str) -> Game:
    # Parse the FEN string to get the board state
        B_Board = Convertion.FEN_to_BOARD(fen, 0)
        B_Side = Convertion.FEN_to_BOARD(fen, 1)
        B_Castle = Convertion.FEN_to_BOARD(fen, 2)
        B_Passent = Convertion.FEN_to_BOARD(fen, 3) if Convertion.FEN_to_BOARD(fen, 3) is not None else -1
        B_HalfClock = int(Convertion.FEN_to_BOARD(fen, 4))
        B_FullClock = int(Convertion.FEN_to_BOARD(fen, 5))
    
    # Create and return a Game object
        return Game(B_Board, B_Side, B_Castle, B_Passent, B_HalfClock, B_FullClock)    
        
    @staticmethod
    def Num_to_DC(Square: square):
        Color = Square % 2 != 0
        Coords = [0, 0, 1, 2, 4, 6, 9, 12,
                  1, 2, 3, 5, 7, 10, 13, 16,
                  3, 4, 6, 8, 11, 14, 17, 20,
                  5, 7, 9, 12, 15, 18, 21, 23,
                  8, 10, 13, 16, 19, 22, 24, 26,
                  11, 14, 17, 20, 23, 25, 27, 28,
                  15, 18, 21, 24, 26, 28, 29, 30,
                  19, 22, 25, 27, 29, 30, 31, 31,]
        return [Color, Coords[Square]]
        
    @staticmethod    
    def DC_to_Num(Color: bool, DC: int):
        if Color:
            Coords = [0, 64, 1, 64, 4, 64, 9, 64,
                      64, 2, 64, 5, 64, 10, 64, 16,
                      3, 64, 6, 64, 11, 64, 17, 64,
                      64, 7, 64, 12, 64, 18, 64, 23,
                      8, 64, 13, 64, 19, 64, 24, 64,
                      64, 14, 64, 20, 64, 25, 64, 28,
                      15, 64, 21, 64, 26, 64, 29, 64,
                      64, 22, 64, 27, 64, 30, 64, 31,]
        else:
            Coords = [64, 0, 64, 2, 64, 6, 64, 12,
                      1, 64, 3, 64, 7, 64, 13, 64,
                      64, 4, 64, 8, 64, 14, 64, 20,
                      5, 64, 9, 64, 15, 64, 21, 64,
                      64, 10, 64, 16, 64, 22, 64, 26,
                      11, 64, 17, 64, 23, 64, 27, 64,
                      64, 18, 64, 24, 64, 28, 64, 30,
                      19, 64, 25, 64, 29, 64, 31, 64,]
        return Coords.index(DC)
    
    @staticmethod
    def DCx(Color: bool, DC: int):
        if Color:
            Size = [1, 4, 9, 16, 23, 28, 31, 32]
        else:
            Size = [2, 6, 12, 20, 26, 30, 32]

        for i, size in enumerate(Size):
            if size > DC:
                return i

    @staticmethod
    def DCy(Color: bool, DC: int):
        x = Convertion.DCx(Color, DC)

        if Color:
            Size = [3, 0, -5, -20, -12, -19, -24, -27]
        else:
            Size = [3, -1, -3, -9, -16, -22, -26, -28]

        return DC + Size[x]

class Map:

    def __init__(self, Board: board):

        self.Board = Board

        self.ColorMap = self.ColorType()
        self.PieceMap = self.PieceType()
    
    def ColorType(self): 
        colorMap = list(EMPTY)
        for i, Square in enumerate(self.Board):
            if Square >= 12:
                colorMap[i] += -10
            else:
                colorMap[i] = Square // 6
        return colorMap

    def PieceType(self):
        pieceMap = []
        for i in self.Board:
            pieceMap.append(Convertion.Piece_to_Type(i))
        return pieceMap    

class Moves:
    
    def __init__(self, Start: square, Game: Game):
        
        self.Board = Game.B_Board
        self.Start = Start

        self.Map = Map(self.Board)

        self.Piece = self.Map.PieceMap
        self.Color = self.Map.ColorMap
        self.passent = Game.B_Passent
        
    def diagnal(self, attack: bool):
        moves = []
        attacks = [] 
        offsets = [7, -7, 9, -9]

        for offset in offsets:
            move = self.Start + offset
            while move in range(64) and abs(move % 8 - self.Start % 8) == abs(move // 8 - self.Start // 8):
                if self.Color[move] == 3:
                    moves.append(move)
                    move += offset
                elif self.Color[move] == int(not bool(self.Color[self.Start])):
                    attacks.append(move)
                    break
                elif self.Color[move] == self.Color[self.Start]:
                    break

        if attack:
            return attacks
        else:
            return moves

    def straight(self, attack: bool):
        moves = []
        attacks = [] 
        offsets = [1,-1,8,-8]

        for offset in offsets:
            move = self.Start + offset
            while move in range(64) and (self.Start // 8 == move // 8 or self.Start % 8 == move % 8):
                if self.Color[move] == 3:
                    moves.append(move)
                    move += offset
                elif self.Color[move] == int(not bool(self.Color[self.Start])):
                    attacks.append(move)
                    break
                elif self.Color[move] == self.Color[self.Start]:
                    break

        if attack:
            return attacks
        else:
            return moves

    def knight(self, attack: bool):
        moves = []
        attacks = [] 
        offsets = [6, 10, 15, 17, -6, -10, -15, -17]

        for offset in offsets:
            move = self.Start + offset
            if move in range(64) and abs(move % 8 - self.Start % 8) <= 2 and abs(move // 8 - self.Start // 8) <= 2:
                if self.Color[move] == 3:
                    moves.append(move)
                elif self.Color[move] == int(not bool(self.Color[self.Start])):
                    attacks.append(move)

        if attack:
            return attacks
        else:
            return moves
    
    def pawn(self, attack: bool):
        moves = []
        attacks = []
        offsets = []
        atteck_offsets = [1, -1]
        foward = 0

        if bool(self.Color[self.Start]):
               foward = -8
        else:
               foward = 8

        if attack:
            for offset in atteck_offsets:
                offsets.append(foward + offset)
        else:
            if (self.Start <= 15 or self.Start >= 48) and self.Color[self.Start + foward] == 3:
               offsets.append(foward * 2)
            offsets.append(foward)
            
        for offset in offsets:
            move = self.Start + offset
            if move in range(64) and abs(self.Start % 8 - move % 8) <= 1:
                if self.Color[move] == 3 and not attack:
                    moves.append(move)
                if self.Color[move] == int(not bool(self.Color[self.Start])) or self.passent == move:
                    attacks.append(move)
        
        if attack:
            return attacks
        else:
            return moves

    def king(self, attack: bool):
        moves = []
        attacks = []
        offsets = [-9, -8, -7, -1 , 1, 7, 8, 9]
        
        for offset in offsets:
            move = self.Start + offset
            if move in range(64) and (abs(move // 8 - self.Start // 8) <= 1 or abs(move % 8 - self.Start % 8) <= 1):
                if self.Color[move] == 3:
                    moves.append(move)
                elif self.Color[move] == int(not bool(self.Color[self.Start])):
                    attacks.append(move)

        if attack:
            return attacks
        else:
            return moves
        
    def duck_leagal(self, Square: square):
        return self.Piece(Square) == 7
    
    def leagal(self, End: square, attack: bool):
        match self.Piece[self.Start]:                   
            case 0:
                if End in self.king(attack):
                    return True
            case 1:    
                if End in self.straight(attack) or End in self.diagnal(attack):
                    return True
            case 2:
                if End in self.straight(attack):
                    return True
            case 3:
                if End in self.knight(attack):
                    return True
            case 4:
                if End in self.diagnal(attack):
                    return True
            case 5:
                if End in self.pawn(attack):
                    return True
        
    
class Castle:
    def __init__(self, Game: Game):
        self.Game = Game
        map = Map(Game.B_Board)
        self.ColorMap = map.ColorMap
    
    def castling(self, castle_type):
        match castle_type:
            case 0:
                if all(Color == 3 for Color in self.ColorMap[5:6]) and self.Game.B_Castle[castle_type]:
                    return [6, 5, 4, 7]
            case 1:
                if all(Color == 3 for Color in self.ColorMap[1:3]) and self.Game.B_Castle[castle_type]:    
                    return [2, 3, 4, 0]
            case 2:
                if all(Color == 3 for Color in self.ColorMap[61:62]) and self.Game.B_Castle[castle_type]:
                    return [62, 61, 60, 63]
            case 3:
                if all(Color == 3 for Color in self.ColorMap[57:59]) and self.Game.B_Castle[castle_type]:
                    return [58, 59, 60, 56]
                
    def leagal(self, castle_type):
        return self.castling(castle_type) != None