# MoASM

MoASM is an esoteric low-level assembly like language in which the instructions are written in morse code.

## Installation and usage

Before installing MoASM, make sure you have python3 (>= 3.6) and pip3 installed.

1. Install MoASM:

```bash
user@programmer~:$ pip install git+https://github.com/frankhart2018/moasm.git
```

2. Run MoASM script:

Once you have written your instructions in a .moasm file, you can run it by running the following command:

```bash
user@programmer~:$ moasm -i <.moasm file>
```

## Symbols

The entire language consists of only three symbols:

1. `.`: The dot symbol.
2. `-`: The dash symbol.
3. `~`: The space symbol.

Here is the list of morse code symbols:

| Symbol | Letter |
|:------:|:------:|
|   .-   |   A    |
|  -...  |   B    |
|  -.-.  |   C    |
|  -..   |   D    |
|   .    |   E    |
|  ..-.  |   F    |
|  --.   |   G    |
|  ....  |   H    |
|   ..   |   I    |
|  .---  |   J    |
|  -.-   |   K    |
|  .-..  |   L    |
|   --   |   M    |
|   -.   |   N    |
|  ---   |   O    |
|  .--.  |   P    |
|  --.-  |   Q    |
|  .-.   |   R    |
|  ...   |   S    |
|   -    |   T    |
|  ..-   |   U    |
|  ...-  |   V    |
|  .--   |   W    |
|  -..-  |   X    |
|  -.--  |   Y    |
|  --..  |   Z    |
| .----  |   1    |
| ..---  |   2    |
| ...--  |   3    |
| ....-  |   4    |
| .....  |   5    |
| -....  |   6    |
| --...  |   7    |
| ---..  |   8    |
| ----.  |   9    |
| -----  |   0    |
| ..-..  |   %    |
| -.-..  |   $    |


## Keywords

These are the keywords in MoASM:

1. `SHOW`: Prints the value (string, number, or identifier) to STDOUT. If used without any parameters, it prints the last value in constant stack. (`SHOW HELLO WORLD`)
2. `ADD`: Adds the values and prints it out. (`ADD 1 2`)
3. `SUB`: Subtracts the values and prints it out. (`SUB 1 2`)
4. `MUL`: Multiplies the values and prints it out. (`MUL 1 2`)
5. `DIV`: Divides the values and prints it out. (`DIV 1 2`)
6. `MOD`: Computes modulo of values and prints it out. (`MOD 1 2`)
7. `PUSH`: Pushes the value to the constant stack. (`PUSH 2`)
8. `POP`: Pops the value from the constant stack and pushes into a variable. (`POP %ABC`, all variables in MoASM have to start with `%`)
9. `JZ`: Jumps to the specified label if and only if the value on top of stack is zero. (`JZ $END`, all labels in MoASM have to start with `$`)
10. `JMP`: Jumps to the specified label. (`JMP $END`)

## Don't know how to get started?

Here is a sample hello world program in MoASM:

```
... .... --- .-- ~ .... . .-.. .-.. --- ~ .-- --- .-. .-.. -..
```

This translates to:

```
SHOW HELLO WORLD
```