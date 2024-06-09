# Chess Game Implementation Documentation

This document provides an overview of the classes and methods used in the Chess game implementation. Examples are provided for each method to demonstrate their usage.

## Import

```python
import DuckChess
```

## Data Types and Constants

### Aliases

- `square = int`
- `color = int`
- `piece = int`
- `board = list`

### Names and Mappings

- `RANKS_NAME`: List of rank names (`["1", "2", "3", "4", "5", "6", "7", "8"]`).
- `FILES_NAME`: List of file names (`["a", "b", "c", "d", "e", "f", "g", "h"]`).
- `SQUARES_NAME`: List of square names (`["a1", "b1", ..., "h8"]`).
- `COLORS_NAME`: List of color names (`["white", "black", "yellow", "none"]`).
- `PIECES_TYPE_NAME`: List of piece type names (`["k", "q", "r", "n", "b", "p", "@", "."]`).
- `PIECES_NAME`: List of piece names (`["K", "Q", "R", "N", "B", "P", "k", "q", "r", "n", "b", "p", "d", "."]`).
- `PIECES_UNICODE`: List of piece Unicode symbols (`["♔", "♕", ..., "🦆", "."]`).

### Enumerations

- `SQUARES`: List of square indices (`A1, B1, ..., H8`) assigned to `range(64)`.
- `COLORS`: List of color indices (`WHITE, BLACK, YELLOW, NONE`) assigned to `range(4)`.
- `PIECETYPES`: List of piece type indices (`T_K, T_Q, ..., T_SPACE`) assigned to `range(8)`.
- `PIECES`: List of piece indices (`W_K, W_Q, ..., SPACE`) assigned to `range(14)`.

### Constants

- `EMPTY`: Representation of an empty board.

## Game Class

The `Game` class is used to store the game state.

### `__init__`

Initialize the game state.

**Parameters:**

- `G_Board`: The board state as a list.
- `G_Side`: The side to play.
- `G_Castle`: The castle rights.
- `G_Passent`: The en passant square.
- `G_HalfClock`: The half-move clock.
- `G_FullClock`: The full-move clock.

**Example:**

```python
game = Game(EMPTY, 0, [True, True, True, True], None, 0, 1)
```

### `flipSide`

Flip the board and return the flipped board state.

**Example:**

```python
flipped_game = game.flipSide()
```

## `Convertion` Class

The `Convertion` class provides static methods for various conversions.

### `SquareNum`

Convert the name of a square to its coordinate.

**Parameters:**

- `Square`: The square name as a string.

**Returns:**

- The square number as an integer.

**Example:**

```python
square_num = Convertion.SquareNum("e2")
```

### `SquareName`

Convert the coordinate of a square to its name.

**Parameters:**

- `Square`: The square number as an integer.

**Returns:**

- The square name as a string.

**Example:**

```python
square_name = Convertion.SquareName(12)
```

### `File`

Return the file of a square.

**Parameters:**

- `Square`: The square number as an integer.

**Returns:**

- The file number as an integer.

**Example:**

```python
file = Convertion.File(12)
```

### `Rank`

Return the rank of a square.

**Parameters:**

- `Square`: The square number as an integer.

**Returns:**

- The rank number as an integer.

**Example:**

```python
rank = Convertion.Rank(12)
```

### `OnEdge`

Check if a square is on the edge of the board.

**Parameters:**

- `Square`: The square number as an integer.

**Returns:**

- `True` if the square is on the edge, `False` otherwise.

**Example:**

```python
on_edge = Convertion.OnEdge(0)
```

### `Piece_to_Type`

Convert a piece number to its piece type number.

**Parameters:**

- `Piece`: The piece number as an integer.

**Returns:**

- The piece type number as an integer.

**Example:**

```python
piece_type = Convertion.Piece_to_Type(1)
```

### `FEN_to_BOARD`

Convert FEN to the board part of the `Game` class.

**Parameters:**

- `fen`: The FEN string.
- `part`: The part of the FEN to convert.

**Returns:**

- The converted part of the FEN.

**Example:**

```python
board = Convertion.FEN_to_BOARD("8/8/8/8/8/8/8/8 w - - 0 1", 0)
```

### `Game_to_FEN`

Convert a `Game` object to a FEN string.

**Parameters:**

- `Game`: The `Game` object.

**Returns:**

- The FEN string.

**Example:**

```python
fen = Convertion.Game_to_FEN(game)
```

### `PGN_to_Move`

Convert a PGN move to detailed move information.

**Parameters:**

- `pgn_move`: The PGN move string.
- `currentGame`: The current `Game` object.

**Returns:**

- The detailed move information.

**Example:**

```python
move_info = Convertion.PGN_to_Move("e4", game)
```

### `FEN_to_Game`

Convert a FEN string to a `Game` object.

**Parameters:**

- `fen`: The FEN string.

**Returns:**

- The `Game` object.

**Example:**

```python
game_from_fen = Convertion.FEN_to_Game("8/8/8/8/8/8/8/8 w - - 0 1")
```

### `Num_to_DC`

Convert a square number to diagonal coordinate.

**Parameters:**

- `Square`: The square number as an integer.

**Returns:**

- The diagonal coordinate as a list.

**Example:**

```python
dc = Convertion.Num_to_DC(12)
```

### `DC_to_Num`

Convert a diagonal coordinate to a square number.

**Parameters:**

- `Color`: The color as a boolean.
- `DC`: The diagonal coordinate as an integer.

**Returns:**

- The square number as an integer.

**Example:**

```python
square_num = Convertion.DC_to_Num(True, 5)
```

### `DCx`

Get the x-coordinate from a diagonal coordinate.

**Parameters:**

- `Color`: The color as a boolean.
- `DC`: The diagonal coordinate as an integer.

**Returns:**

- The x-coordinate as an integer.

**Example:**

```python
dcx = Convertion.DCx(True, 5)
```

### `DCy`

Get the y-coordinate from a diagonal coordinate.

**Parameters:**

- `Color`: The color as a boolean.
- `DC`: The diagonal coordinate as an integer.

**Returns:**

- The y-coordinate as an integer.

**Example:**

```python
dcy = Convertion.DCy(True, 5)
```

## `Map` Class

The `Map` class creates lists of colors and piece types on the board.

### `__init__`

Initialize the map.

**Parameters:**

- `Board`: The board state as a list.

**Example:**

```python
map = Map(EMPTY)
```

### `ColorType`

Create a list of all squares' colors.

**Returns:**

- A list of colors.

**Example:**

```python
color_map = map.ColorType()
```

### `PieceType`

Create a list of all squares' piece types.

**Returns:**

- A list of piece types.

**Example:**

```python
piece_map = map.PieceType()
```

## `Moves` Class

The `Moves` class generates possible moves for a piece.

### `__init__`

Initialize the moves.

**Parameters:**

- `Start`: The start square as an integer.
- `Game`: The current `Game` object.

**Example:**

```python
moves = Moves(12, game)
```

### `diagnal`

Generate diagonal moves.

**Parameters:**

- `attack`: The attack mode as a boolean, set to `true` to return capture moves.

**Returns:**

- A list of diagonal move's destination square.

**Example:**

```python
diagonal_moves = moves.diagnal(True)
```

### `straight`

Generate straight moves.

**Parameters:**

- `attack`: The attack mode as a boolean, set to `true` to return capture moves.

**Returns:**

- A list of straight move's destination square.

**Example:**

```python
straight_moves = moves.straight(True)
```

### `knight`

Generate knight moves.

**Parameters:**

- `attack`: The attack mode as a boolean, set to `true` to return capture moves.

**Returns:**

- A list of knight move's destination square.

**Example:**

```python
knight_moves = moves.knight(True)
```

### `pawn`

Generate pawn moves.

**Parameters:**

- `attack`: The attack mode as a boolean, set to `true` to return capture moves.

**Returns:**

- A list of pawn move's destination square.

**Example:**

```python
pawn_moves = moves.pawn(True)
```

### `king`

Generate king moves.

**Parameters:**

- `attack`: The attack mode as a boolean, set to `true` to return capture moves.

**Returns:**

- A list of king move's destination square.

**Example:**

```python
king_moves = moves.king(True)
```

### `duck_leagal`

Check if a duck can move to a square.

**Parameters:**

- `Square`: The square number as an integer.

**Returns:**

- `True` if the duck move is legal, `False` otherwise.

**Example:**

```python
duck_legal = moves.duck_leagal(12)
```

### `leagal`

Check if a move is legal.

**Parameters:**

- `End`: The end square as an integer.
- `attack`: The attack mode as a boolean.

**Returns:**

- `True` if the move is legal, `False` otherwise.

**Example:**

```python
legal_move = moves.leagal(24, True)
```

## `Castle` Class

The `Castle` class handles castling moves.

### `__init__`

Initialize the castling class.

**Parameters:**

- `Game`: The current `Game` object.

**Example:**

```python
castle = Castle(game)
```

### `castling`

Get castling squares.

**Parameters:**

- `castle_type`: The type of castling as an integer.

**Returns:**

- A list of the king's destination, the rook's destination, the king's starting position, the rook's startion position.

**Example:**

```python
castling_squares = castle.castling(0)
```

### `leagal`

Check if castling is legal.

**Parameters:**

- `castle_type`: The type of castling as an integer.

**Returns:**

- `True` if the castling is legal, `False` otherwise.

**Example:**

```python
castling_legal = castle.leagal(0)
```

## `Termination` Class

### `__init__`

Initialize the castling class.

**Parameters:**

- `Game`: The current `Game` object.
- `n_move_rule`: The amount of moves to trigger the 50-move rule.(deaflt = 50)

**Example:**

```python
termination = Termination(game)
```

### `terminationType`

**Returns:**

-`0` if game ends in 50 move rule -`1` if game ends in king captured -`2` if stalmated

**Example:**

```python
termination_type = termination.terminationType()
```

### `terminationSide`

**Returns:**

-`0` if white wins -`1` if black wins -`3` if draw

**Example:**

```python
Winning_Side = termination.terminationSide()
```

### `isTermination`

**Returns:**

-`True` if the game has ended

**Example:**

```python
GameIsStillGoing = not termination.isTermination()
```

## Functions

### `generate_all_moves`

Generate all possible moves for the current game state.

**Parameters:**

- `current_game`: The current `Game` object.

**Returns:**

- A list of all posible `Game` class after one move.

**Example:**

```python
all_moves = generate_all_moves(game)
```
