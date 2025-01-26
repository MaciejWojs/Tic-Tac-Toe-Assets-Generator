# Tic Tac Toe Board Generator

A simple Python script that generates a tic-tac-toe game board using the Pillow library.

## Requirements

- Python 3.x
- Pillow 11.1.0

## Installation

1. Clone the repository
2. Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Run the main script:

```sh
python main.py
```

The script will generate:
- `board.png` - empty game board
- `X.png` - X symbol (blue)
- `O.png` - O symbol (red)
- `example-board.png` - example board with symbols placed

## Configuration

Main constants in [main.py](main.py):

- `IMAGE_SIZE` - board size in pixels (default 1000)
- `FIELDS_IN_ROW_COUNT` - number of fields per row (default 3)
- `LINE_WIDTH` - line width (default 10)
- `BLUE` - X color (#00adff)
- `RED` - O color (#ff0000)

## License

MIT
