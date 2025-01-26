#! /usr/bin/env python3
from PIL import Image, ImageDraw


if __name__ == "__main__":

    #CONSTANTS
    IMAGE_SIZE = 1000
    FIELDS_IN_ROW_COUNT = 3
    LINE_WIDTH = 10
    FILE_FORMAT = "png"
    BOARD_BASE_NAME = "board"
    BOARD_NAME = f"{BOARD_BASE_NAME}.{FILE_FORMAT}"
    
    #CALCULATED CONSTANTS
    FIGURE_SIZE = (IMAGE_SIZE - (LINE_WIDTH * 2)) // FIELDS_IN_ROW_COUNT
    FIRST_LINE = FIGURE_SIZE + LINE_WIDTH // 2
    SECOND_LINE = FIRST_LINE * 2 + (LINE_WIDTH // 2)

    #COLORS
    BLUE = "#00adff"
    RED = "#ff0000"
    TRANSPARENT_COLOR = "#00000000"


    print(f"{FIGURE_SIZE = }")

    board = Image.new(mode="RGBA", size=(IMAGE_SIZE, IMAGE_SIZE))
    board_draw = ImageDraw.Draw(board)
    board_draw.line([(0, FIRST_LINE), (IMAGE_SIZE, FIRST_LINE)], width=LINE_WIDTH)
    board_draw.line([(FIRST_LINE, 0), (FIRST_LINE, IMAGE_SIZE)], width=LINE_WIDTH)
    board_draw.line([(0, SECOND_LINE), (IMAGE_SIZE, SECOND_LINE)], width=LINE_WIDTH)
    board_draw.line([(SECOND_LINE, 0), (SECOND_LINE, IMAGE_SIZE)], width=LINE_WIDTH)
    board.show()
    board.save(BOARD_NAME, format=FILE_FORMAT)

    x = Image.new(mode="RGBA", size=(FIGURE_SIZE, FIGURE_SIZE))
    x_draw = ImageDraw.Draw(x)
    TEMP_XY = FIGURE_SIZE * 1 / 10
    x_draw.line(
        [(TEMP_XY, TEMP_XY), (FIGURE_SIZE - TEMP_XY, FIGURE_SIZE - TEMP_XY)],
        width=7,
        fill=BLUE,
    )
    x_draw.line(
        [(TEMP_XY, FIGURE_SIZE - TEMP_XY), (FIGURE_SIZE - TEMP_XY, TEMP_XY)],
        width=7,
        fill=BLUE,
    )
    x.save("X.png", format=FILE_FORMAT)

    o = Image.new(mode="RGBA", size=(FIGURE_SIZE, FIGURE_SIZE))
    o_draw = ImageDraw.Draw(o)
    o_draw.ellipse(
        [(TEMP_XY, TEMP_XY), (FIGURE_SIZE - TEMP_XY, FIGURE_SIZE - TEMP_XY)],
        fill=RED,
        width=7,
    )
    o_draw.ellipse(
        [
            (TEMP_XY + 10, TEMP_XY + 10),
            (FIGURE_SIZE - TEMP_XY - 10, FIGURE_SIZE - TEMP_XY - 10),
        ],
        fill="#00000000",
        width=LINE_WIDTH,
    )
    o.save("O.png", format=FILE_FORMAT)

    # Board edit
    board.paste(x, (0, 0))
    board.paste(o, (FIGURE_SIZE + LINE_WIDTH, 0))
    board.paste(o, ((FIGURE_SIZE + LINE_WIDTH) * 2, 0))
    board.paste(o, (FIGURE_SIZE + LINE_WIDTH, FIGURE_SIZE + LINE_WIDTH))
    board.paste(x, ((FIGURE_SIZE + LINE_WIDTH) * 2, FIGURE_SIZE + LINE_WIDTH))
    board.paste(x, ((FIGURE_SIZE + LINE_WIDTH) * 2, (FIGURE_SIZE + LINE_WIDTH) * 2))
    board.save(f"example-{BOARD_NAME}", format=FILE_FORMAT)
