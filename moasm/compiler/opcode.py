from .opcode_type import OpCodeType


class OpCode:
    def __init__(self, opcode_type: OpCodeType, opcode_value: str = None, opcode_dtype: str = None):
        self.__opcode_type = opcode_type
        self.__opcode_value = opcode_value
        self.__opcode_dtype = opcode_dtype

    @property
    def opcode_type(self):
        return self.__opcode_type

    @property
    def opcode_value(self):
        return self.__opcode_value

    @opcode_type.setter
    def opcode_type(self, opcode_type: OpCodeType):
        self.__opcode_type = opcode_type

    def __str__(self) -> str:
        optype = str(self.__opcode_type).split(".")[1]
        value = f" {self.__opcode_value} ({self.__opcode_dtype})"

        return optype + " " + value \
            if self.__opcode_value is not None and self.__opcode_dtype is not None \
            else optype
