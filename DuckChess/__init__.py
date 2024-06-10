import re
from copy import deepcopy

square = int

color = int

piece = int

board = list

RANKS_NAME = ["1", "2", "3", "4", "5", "6", "7", "8"] # rank name

FILES_NAME = ["a", "b", "c", "d", "e", "f", "g", "h"] # file name

SQUARES_NAME = [f + r for r in RANKS_NAME for f in FILES_NAME] # square name

COLORS_NAME = ["white", "black", "yellow", "none"] # upper, lower, @, .

PIECES_TYPE_NAME = ["k" ,"q" ,"r", "n", "b", "p", "@", "."] # piece type name

PIECES_NAME = ["K", "Q", "R", "N", "B", "P", "k", "q", "r", "n", "b" , "p", "d", "."] # piece name

PIECES_UNICODE= ["♔", "♕", "♖", "♘", "♗", "♙", "♚", "♛", "♜", "♞", "♝", "♟︎", "🦆", "."] # piece unicode

SQUARES = [
    A1, B1, C1, D1, E1, F1, G1, H1,
    A2, B2, C2, D2, E2, F2, G2, H2,
    A3, B3, C3, D3, E3, F3, G3, H3,
    A4, B4, C4, D4, E4, F4, G4, H4,
    A5, B5, C5, D5, E5, F5, G5, H5,
    A6, B6, C6, D6, E6, F6, G6, H6,
    A7, B7, C7, D7, E7, F7, G7, H7,
    A8, B8, C8, D8, E8, F8, G8, H8,
    ] = range(64) # asign square number

COLORS = [WHITE, BLACK, YELLOW, NONE] = range(4) # asign color number

PIECETYPES = [T_K, T_Q, T_R, T_N, T_B, T_P, T_D, T_SPACE] = range (8) # asign piece type number

PIECES = [W_K, W_Q, W_R, W_N, W_B, W_P, B_K, B_Q, B_R, B_N, B_B, B_P, D, SPACE] = range(14) # asign pice number

EMPTY = [
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    13,13,13,13,13,13,13,13,
    ] # empty board

#storing the gmae state
class Game:
    def __init__(self, G_Board: board, G_Side: bool, G_Castle: list, G_Passent = int, G_HalfClock = int, G_FullClock = int):
    
        self.G_Board = G_Board # piece on each square

        self.G_Side = G_Side # side Playing

        self.G_Castle = G_Castle # castle rights
    
        self.G_Passent = G_Passent # en passentcsquare

        self.G_HalfClock = G_HalfClock # half clock

        self.G_FullClock = G_FullClock # full clock

    def flipSide(self): # flip th board
        G_Board = []
        
        for i in range(7, -1, -1):
            G_Board.append(self.G_Board[i * 8:(i + 1) * 8])

        for Square in G_Board:
            if(Square < 6):
                Square += 6
            elif(Square < 12):
                Square += -6

        FlipedBoard = Game(G_Board, not self.G_Side, [self.G_Castle[2], self.G_Castle[3], self.G_Castle[0], self.G_Castle[1]], self.G_Passent, self.G_HalfClock, self.G_FullClock)
        return FlipedBoard

class Convertion:
    #convert name of a square to coordinate
    @staticmethod
    def SquareNum(Square: str):
        return SQUARES_NAME.index(Square)
    
    #convert coordinate to name        
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
    
    #return if piece is on edge of board
    @staticmethod
    def OnEdge(Square: square):
        return Convertion.Rank(Square) in [0, 7] or Convertion.File(Square) in [0, 7]
    
    #piece number to piece type number
    @staticmethod
    def Piece_to_Type(Piece: piece):
        if Piece >= 12:
            return Piece - 6
        else:
            return Piece % 6

    #FEN to each part of the Game class
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

    #Game class to FEN
    @staticmethod
    def Game_to_FEN(Game: Game):

        fen = []
        space_count = None
        
        for i in range(64):
            if (i + 1) % 8 == 0:
                fen.append("/")
            if Game.G_Board[i] == 13:
                space_count += 1
            else:
                if space_count:
                    fen.append(space_count)
                    space_count = None    
            fen.appaend(PIECES_NAME[i])
        fen.reverse()
        
        fen.append(" " + "b" if Game.G_Side else "w")
        
        fen.append(" ")
        fen.append("K" if Game.G_Castle[0] else "")
        fen.append("Q" if Game.G_Castle[1] else"")
        fen.append("k" if Game.G_Castle[2] else"")
        fen.append("q" if Game.G_Castle[3] else"")
        
        fen.append(" " + "-" if not Game.G_Passent else Convertion.SquareName(Game.G_Passent))
        
        fen.append(" " + Game.G_HalfClock)
        
        fen.append(" " + Game.G_FullClock)
        
        return fen
    
    #return PieceType, PieceColor, Taking a piece or not, where it's going, and duck destination 
    @staticmethod
    def PGN_to_Move(pgn_move: str, currentGame: Game):
        Side = currentGame.G_Side

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

            PieceMap = Map(currentGame.G_Board).PieceMap
            ColorMap = Map(currentGame.G_Board).ColorMap

            Start = []

            for Square, i in enumerate(PieceMap):

                if i == Convertion.Piece_to_Type(Piece) and bool(ColorMap[Square]) == Side:
                    currentMove = Moves(Square, currentGame.G_Board)
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

    #FEN to Game class
    @staticmethod
    def FEN_to_Game(fen: str) -> Game:
        G_Board = Convertion.FEN_to_BOARD(fen, 0)
        G_Side = Convertion.FEN_to_BOARD(fen, 1)
        G_Castle = Convertion.FEN_to_BOARD(fen, 2)
        G_Passent = Convertion.FEN_to_BOARD(fen, 3) if Convertion.FEN_to_BOARD(fen, 3) is not None else -1
        G_HalfClock = int(Convertion.FEN_to_BOARD(fen, 4))
        G_FullClock = int(Convertion.FEN_to_BOARD(fen, 5))
    
    # Create and return a Game object
        return Game(G_Board, G_Side, G_Castle, G_Passent, G_HalfClock, G_FullClock)    
    
    #coordinate to diagnal coordinate
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

    #diagnal coordinate to coordinate  
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
    
    #diagnal coordinate x
    @staticmethod
    def DCx(Color: bool, DC: int):
        Coords = [0, 0, 1, 1, 2, 2, 3, 3,
                  0, 1, 1, 2, 2, 3, 3, 4,
                  1, 1, 2, 2, 3, 3, 4, 4,
                  1, 2, 2, 3, 3, 4, 4, 5,
                  2, 2, 3, 3, 4, 4, 5, 5,
                  2, 3, 3, 4, 4, 5, 5, 6,
                  3, 3, 4, 4, 5, 5, 6, 6,
                  3, 4, 4, 5, 5, 6, 6, 7,]
        return Coords[DC]

    #diagnal coordinate y
    @staticmethod
    def DCy(Color: bool, DC: int):
        Coords = [3, 3, 2, 2, 1, 1, 0, 0,
                  4, 3, 3, 2, 2, 1, 1, 0,
                  4, 4, 3, 3, 2, 2, 1, 1,
                  5, 4, 4, 3, 3, 2, 2, 1,
                  5, 5, 4, 4, 3, 3, 2, 2,
                  6, 5, 5, 4, 4, 3, 3, 2,
                  6, 6, 5, 5, 4, 4, 3, 3,
                  7, 6, 6, 5, 5, 4, 4, 3,]
        return Coords[DC]
#create list of color and piece type
class Map:
    def __init__(self, Board: board):

        self.Board = Board

        self.ColorMap = self.ColorType()
        self.PieceMap = self.PieceType()
    
    #list of all square's color
    def ColorType(self): 
        colorMap = list(EMPTY)
        for i, Square in enumerate(self.Board):
            if Square >= 12:
                colorMap[i] += -10
            else:
                colorMap[i] = Square // 6
        return colorMap

    #list of all square's piecetype
    def PieceType(self):
        pieceMap = []
        for i in self.Board:
            pieceMap.append(Convertion.Piece_to_Type(i))
        return pieceMap    

#generatae the destination of a move
#`attack = true` for captures, `attack = false` for non-capture move
class Moves:
    def __init__(self, Start: square, Game: Game):
        
        self.Board = Game.G_Board
        self.Start = Start

        self.Map = Map(self.Board)

        self.Piece = self.Map.PieceMap
        self.Color = self.Map.ColorMap
        self.passent = Game.G_Passent

    #diagnal(bishop) moves    
    def diagnal(self, attack: bool):
        moves = []
        attacks = [] 
        offsets = [7, -7, 9, -9]

        for offset in offsets:
            move = self.Start + offset
            while move in range(64) and abs(move % 8 - self.Start % 8) == abs(move // 8 - self.Start // 8):
                if self.Color[move] == NONE:
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

    #straight(rook) moves
    def straight(self, attack: bool):
        moves = []
        attacks = [] 
        offsets = [1,-1,8,-8]

        for offset in offsets:
            move = self.Start + offset
            while move in range(64) and (self.Start // 8 == move // 8 or self.Start % 8 == move % 8):
                if self.Color[move] == NONE:
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

    #knight moves
    def knight(self, attack: bool):
        moves = []
        attacks = [] 
        offsets = [6, 10, 15, 17, -6, -10, -15, -17]

        for offset in offsets:
            move = self.Start + offset
            if move in range(64) and abs(move % 8 - self.Start % 8) <= 2 and abs(move // 8 - self.Start // 8) <= 2:
                if self.Color[move] == NONE:
                    moves.append(move)
                elif self.Color[move] == int(not bool(self.Color[self.Start])):
                    attacks.append(move)

        if attack:
            return attacks
        else:
            return moves
    
    #pawn moves
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
                if self.Color[move] == NONE and not attack:
                    moves.append(move)
                if self.Color[move] == int(not bool(self.Color[self.Start])) or self.passent == move:
                    attacks.append(move)
        
        if attack:
            return attacks
        else:
            return moves

    #king moves
    def king(self, attack: bool):
        moves = []
        attacks = []
        offsets = [-9, -8, -7, -1 , 1, 7, 8, 9]
        
        for offset in offsets:
            move = self.Start + offset
            if move in range(64) and (abs(move // 8 - self.Start // 8) <= 1 or abs(move % 8 - self.Start % 8) <= 1):
                if self.Color[move] == NONE:
                    moves.append(move)
                elif self.Color[move] == int(not bool(self.Color[self.Start])):
                    attacks.append(move)

        if attack:
            return attacks
        else:
            return moves
    
    #return `true` if duck can go to the square
    def duck_leagal(self, Square: square):
        return self.Piece(Square) == T_SPACE
    
    #detect wheather move is leagal
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
        
#handling castles
class Castle:
    def __init__(self, Game: Game):
        self.Game = Game
        map = Map(Game.G_Board)
        self.ColorMap = map.ColorMap
    
    #return [king end square, rook end square, king start square, rook start square]
    def castling(self, castle_type):
        match castle_type:
            case 0:
                if all(Color == NONE for Color in self.ColorMap[5:6]) and self.Game.G_Castle[castle_type]:
                    return [6, 5, 4, 7]
            case 1:
                if all(Color == NONE for Color in self.ColorMap[1:3]) and self.Game.G_Castle[castle_type]:    
                    return [2, 3, 4, 0]
            case 2:
                if all(Color == NONE for Color in self.ColorMap[61:62]) and self.Game.G_Castle[castle_type]:
                    return [62, 61, 60, 63]
            case 3:
                if all(Color == NONE for Color in self.ColorMap[57:59]) and self.Game.G_Castle[castle_type]:
                    return [58, 59, 60, 56]
                
    #detect wheather castle is leagal           
    def leagal(self, castle_type):
        return self.castling(castle_type) != None

#class for game end
class Termination:
    #change n_move_rule value for the 50 move rule moves
    def __init__(self, current_Game: Game, n_move_rule = 50):
        self.current_Game = current_Game
        self.T_Type = None
        self.T_Side = None

        if current_Game.G_HalfClock > n_move_rule:
            self.T_Type = 0
            self.T_Side = 3
        if B_K not in current_Game.G_Board:
            self.T_Type = 1
            self.T_Side = 0
        if W_K not in current_Game.G_Board:
            self.T_Type = 1
            self.T_Side = 1
        if not generate_all_moves(current_Game):
            self.T_Type = 2
            if current_Game.G_Side:
                self.T_Side = 1
            else:
                self.T_Side = 0

    #wheather game is terminated
    def isTermination(self):
        return self.T_Type != None
    
    #termination type: 0 -> 50 move rule, 1 -> king capture, 2 -> no move
    def terminationType(self):
        return self.T_Type
    
    #the wining side
    def terminationSide(self):
        return self. T_Side

#generate all posible board state after one move    
def generate_all_moves(current_game: Game):
    all_moves = []

    piece_map = Map(current_game.G_Board).PieceMap
    color_map = Map(current_game.G_Board).ColorMap

    current_side = current_game.G_Side

    for start_square, piece_type in enumerate(piece_map):
        if color_map[start_square] == current_side:
            current_moves = Moves(start_square, current_game)

            match piece_type:
                case 0:
                    possible_moves = current_moves.king(False)
                    possible_attacks = current_moves.king(True)
                case 1:
                    possible_moves = current_moves.straight(False) + current_moves.diagnal(False)
                    possible_attacks = current_moves.straight(True) + current_moves.diagnal(True)
                case 2:
                    possible_moves = current_moves.straight(False)
                    possible_attacks = current_moves.straight(True)
                case 3:
                    possible_moves = current_moves.knight(False)
                    possible_attacks = current_moves.knight(True)
                case 4:
                    possible_moves = current_moves.diagnal(False)
                    possible_attacks = current_moves.diagnal(True)
                case 5:
                    possible_moves = current_moves.pawn(False)
                    possible_attacks = current_moves.pawn(True)
                case _:
                    continue

            all_possible_moves = possible_moves + possible_attacks
            if all_possible_moves:
                for i, end_square in enumerate(all_possible_moves):
                    new_game_state = deepcopy(current_game)
                    if piece_type == T_P:
                        new_game_state.G_HalfClock == 0
                        if current_game.G_Passent == end_square:
                            new_game_state.G_Board[current_game.G_Passent + (((int(current_side) << 1) - 1) << 3)] = SPACE
                        if abs(end_square - start_square) == 16:
                            new_game_state.G_Passent == end_square
                        else:
                            new_game_state.G_Passent = None
                    elif i > len(possible_moves):
                        new_game_state.G_HalfClock == 0
                    else:
                        new_game_state.G_HalfClock += 1
                    new_game_state.G_Board[end_square] = new_game_state.G_Board[start_square]
                    new_game_state.G_Board[start_square] = SPACE
                    new_game_state.G_Side = not current_side
                    if piece_type == T_K or piece_type == T_R:
                        for j in range(2):
                            j += int(current_side) << 1
                            new_game_state.G_Castle[j] == False
                    if current_side == 0:
                        new_game_state.G_FullClock += 1
                    all_moves.append(new_game_state)

    # Handle castling separately
    castle = Castle(current_game)
    for i in range(2):
        i += int(current_side) << 1
        if castle.leagal(i):
            new_game_state = deepcopy(current_game)
            castle_moves = castle.castling(i)
            for j in range(2) + int(current_side) << 1:
                new_game_state.G_Castle[j] == False
            if castle_moves:
                new_game_state.G_Board[castle_moves[0]] = new_game_state.G_Board[castle_moves[2]]
                new_game_state.G_Board[castle_moves[1]] = new_game_state.G_Board[castle_moves[3]]
                new_game_state.G_Board[castle_moves[2]] = SPACE
                new_game_state.G_Board[castle_moves[3]] = SPACE
                new_game_state.G_Side = not current_side
                if current_side == 0:
                    new_game_state.G_FullClock += 1
                    new_game_state.G_HalfClock += 1
                all_moves.append(new_game_state)

    return all_moves