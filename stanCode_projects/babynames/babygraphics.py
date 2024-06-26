"""
File: babygraphics.py
Name:
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    equal_spacing = (width-(GRAPH_MARGIN_SIZE*2))/len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE+(equal_spacing*year_index)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # two horizontal lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # vertical lines for years
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    count = 0
    for name in lookup_names:
        target_d = name_data[name]
        for i in range(len(YEARS)-1):
            year1 = str(YEARS[i])     # change into string for comparison
            if year1 not in target_d:
                rank1 = 1000
            else:
                rank1 = int(target_d[year1])
            year2 = str(YEARS[i+1])
            if year2 not in target_d:
                rank2 = 1000
            else:
                rank2 = int(target_d[year2])
            x1 = get_x_coordinate(CANVAS_WIDTH, i)
            x2 = get_x_coordinate(CANVAS_WIDTH, i+1)
            y_equal_spacing = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE-GRAPH_MARGIN_SIZE) / 1000
            y1 = GRAPH_MARGIN_SIZE + rank1*y_equal_spacing
            y2 = GRAPH_MARGIN_SIZE + rank2*y_equal_spacing
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[count])
            if rank1 != 1000:
                canvas.create_text(x1, y1, text=name + ' ' + str(rank1), anchor=tkinter.SW, fill=COLORS[count])
            else:
                canvas.create_text(x1, y1, text=name + ' *', anchor=tkinter.SW, fill=COLORS[count])

        last_x = get_x_coordinate(CANVAS_WIDTH, len(YEARS)-1)
        last_year = str(YEARS[len(YEARS)-1])
        if last_year not in target_d:
            rank = 1000
        else:
            rank = int(target_d[last_year])
        y_equal_spacing = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000
        last_y = GRAPH_MARGIN_SIZE + rank*y_equal_spacing
        if rank == 1000:
            canvas.create_text(last_x, last_y, text=name + ' *', anchor=tkinter.SW, fill=COLORS[count])
        else:
            canvas.create_text(last_x, last_y, text=name + ' ' + str(rank), anchor=tkinter.SW, fill=COLORS[count])
        count += 1
        count = count % len(COLORS)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
