from bokeh.plotting import figure
from bokeh.io import output_file, show, output_notebook, push_notebook
from bokeh.models import ColumnDataSource, HoverTool, CategoricalColorMapper
from bokeh.layouts import row, column, gridplot
from bokeh.models.layouts import Tabs, TabPanel

import numpy as np
f = figure()