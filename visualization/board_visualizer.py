from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d


class DrawBoard:
    def __init__(self, params):
        self.p = figure()
        self._connect4_config(params['width'], params['height'])

        # add a circle renderer with a size, color, and alpha
        self.p.circle([1.5, 2.5, 3.5, 4.5], [1.5, 2.5, 3.5, 4.5], size=100, color="yellow", alpha=0.75)
        self.p.circle([1.5, 2.5, 3.5, 4.5], [4.5, 3.5, 2.5, 1.5], size=100, color="red", alpha=0.75)

        # show the results
        show(self.p)

        ## write function to visualize circles 1 by 1 while recursing through graph


    def _connect4_config(self, width, height):
        # output to static HTML file
        output_file("output/test_connect4_viz.html")

        # set up empty spaces
        self.p.circle([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]*6, [0.5]*7+[1.5]*7+[2.5]*7+[3.5]*7+[4.5]*7+[5.5]*7, size=100, color="white")

        self.p.background_fill_color = 'blue'
        self.p.background_fill_alpha = 0.75
        self.p.xgrid.grid_line_color = None
        self.p.ygrid.grid_line_color = None

        self.p.line([0,width],[0,0], color='navy', line_width=10)

        self.p.x_range = Range1d(0, width)
        self.p.y_range = Range1d(0, height)
        self.p.plot_height = 125*height
        self.p.plot_width= 125*width

        self.p.xaxis.major_tick_line_color = None  # turn off x-axis major ticks
        self.p.xaxis.minor_tick_line_color = None  # turn off x-axis minor ticks

        self.p.yaxis.major_tick_line_color = None  # turn off y-axis major ticks
        self.p.yaxis.minor_tick_line_color = None  # turn off y-axis minor ticks

        self.p.xaxis.major_label_text_font_size = '0pt'  # turn off x-axis tick labels
        self.p.yaxis.major_label_text_font_size = '0pt'  # turn off y-axis tick labels

        self.p.yaxis.visible = False

        self.p.toolbar.logo = None
        self.p.toolbar_location = None


Connect4_params = {'width':7, 'height':6, 'root':None}
DrawBoard(params=Connect4_params)
