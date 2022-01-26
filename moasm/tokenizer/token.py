from .tokentype import TokenType


class Token:
    def __init__(self, ttype: TokenType, val: str = "", dtype: str = "") -> None:
        self.__ttype: TokenType = ttype
        self.__val: str = val
        self.__dtype: str = dtype

    def __str__(self) -> str:
        type = f"{self.__ttype}"
        val_dtype = f"{self.__val} ({self.__dtype})"

        return type + " " + val_dtype if self.__val and self.__dtype else type