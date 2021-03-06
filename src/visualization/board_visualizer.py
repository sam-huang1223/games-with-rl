from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d


class DrawBoard:
    def __init__(self, params):
        self.p = figure()
        self.CIRCLE_SIZE = size=800/1.1/params['width']
        self._connect4_config(params['width'], params['height'], params['output_path'])

        # add a circle renderer with a size, color, and alpha
        for l in params['board']:
            for node in l:
                if node.player == 1:
                    color='red'  # player piece
                elif node.player == -1:
                    color='black'  # AI piece
                elif not node.player:
                    color='white'  # empty
                else:
                    raise EnvironmentError
                self.p.circle(node.x+0.5, node.y+0.5, size=self.CIRCLE_SIZE, color=color)

        # show the results
        show(self.p)

    def _connect4_config(self, width, height, output_path):
        # output to static HTML file
        output_file(output_path)

        self.p.background_fill_color = 'blue'
        self.p.background_fill_alpha = 0.75
        self.p.xgrid.grid_line_color = None
        self.p.ygrid.grid_line_color = None

        self.p.x_range = Range1d(0, width)
        self.p.y_range = Range1d(0, height)
        self.p.plot_height = 800
        self.p.plot_width= 800

        self.p.xaxis.major_tick_line_color = None  # turn off x-axis major ticks
        self.p.xaxis.minor_tick_line_color = None  # turn off x-axis minor ticks

        self.p.yaxis.major_tick_line_color = None  # turn off y-axis major ticks
        self.p.yaxis.minor_tick_line_color = None  # turn off y-axis minor ticks

        self.p.xaxis.major_label_text_font_size = '0pt'  # turn off x-axis tick labels
        self.p.yaxis.major_label_text_font_size = '0pt'  # turn off y-axis tick labels

        self.p.yaxis.visible = False

        self.p.toolbar.logo = None
        self.p.toolbar_location = None
