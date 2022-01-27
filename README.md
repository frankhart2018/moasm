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
|   .-   |    A   |
|  -...  |    B   |
|  -.-.  |    C   |
|   -..  |    D   |
|    .   |    E   |
|  ..-.  |    F   |
|   --.  |    G   |
|  ....  |    H   |
|   ..   |    I   |
|  .---  |    J   |
|   -.-  |    K   |
|  .-..  |    L   |
|   --   |    M   |
|   -.   |    N   |
|   ---  |    O   |
|  .--.  |    P   |
|  --.-  |    Q   |
|   .-.  |    R   |
|   ...  |    S   |
|    -   |    T   |
|   ..-  |    U   |
|  ...-  |    V   |
|   .--  |    W   |
|  -..-  |    X   |
|  -.--  |    Y   |
|  --..  |    Z   |
|  .---- |    1   |
|  ..--- |    2   |
|  ...-- |    3   |
|  ....- |    4   |
|  ..... |    5   |
|  -.... |    6   |
|  --... |    7   |
|  ---.. |    8   |
|  ----. |    9   |
|  ----- |    0   |


## Keywords

These are the keywords in MoASM:

1. `SHOW`: Prints the value to STDOUT.

## Don't know how to get started?

Here is a sample hello world program in MoASM:

```
... .... --- .-- ~ .... . .-.. .-.. --- ~ .-- --- .-. .-.. -..
```

This translates to:

```
SHOW HELLO WORLD
```