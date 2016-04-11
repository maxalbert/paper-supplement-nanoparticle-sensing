import brewer2mpl
import itertools
from cycler import cycler


cmap = brewer2mpl.get_map('Set1', 'Qualitative', 5, reverse=False)
color_cycle = cycler('color', cmap.hex_colors)
marker_cycle = cycler('marker', ['s', '^', 'o', 'D', 'v'])
markersize_cycle = cycler('markersize', [10, 12, 11, 10, 12])

style_cycle = itertools.cycle(color_cycle + marker_cycle + markersize_cycle)
