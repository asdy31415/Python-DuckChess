from __future__ import annotations

__author__ = "Just A Pi"

__email__ = ""

__version__ = "0.1.0"

import collections
import copy
import dataclasses
import enum
import math
import re
import itertools
import typing

from typing import ClassVar, Callable, Counter, Dict, Generic, Hashable, Iterable, Iterator, List, Mapping, Optional, SupportsInt, Tuple, Type, TypeVar, Union

try:
    from typing import Literal
    _EnPassantSpec = Literal["legal", "fen", "xfen"]
except ImportError:
    # Before Python 3.8.
    _EnPassantSpec = str


Color = int
COLORS = [WHITE, BLACK, YELLOW] = [1, 0, 2]
COLOR_NAMES = ["black", "white", "yellow"]

PieceType = int
PIECE_TYPES = [PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING, DUCK] = range(1, 8)
PIECE_SYMBOLS = [None, "p", "n", "b", "r", "q", "k", "@"]
PIECE_NAMES = [None, "pawn", "knight", "bishop", "rook", "queen", "king", "duck"]

def piece_symbol(piece_type: PieceType) -> str:
    return typing.cast(str, PIECE_SYMBOLS[piece_type])

def piece_name(piece_type: PieceType) -> str:
    return typing.cast(str, PIECE_NAMES[piece_type])

UNICODE_PIECE_SYMBOLS = {
    "R": "♖", "r": "♜",
    "N": "♘", "n": "♞",
    "B": "♗", "b": "♝",
    "Q": "♕", "q": "♛",
    "K": "♔", "k": "♚",
    "P": "♙", "p": "♟",
}

FILE_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h"]

RANK_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8"]

STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
"""The FEN for the standard chess starting position."""

STARTING_BOARD_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
"""The board part of the FEN for the standard chess starting position."""
