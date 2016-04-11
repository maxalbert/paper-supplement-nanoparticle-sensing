import brewer2mpl
from cycler import cycler

N = 5

cmap = brewer2mpl.get_map('Set1', 'Qualitative', N, reverse=False)
color_cycle = cycler('color', cmap.hex_colors)
marker_cycle = cycler('marker', ['s', '^', 'o', 'D', 'v'])
markersize_cycle = cycler('markersize', [10, 12, 11, 10, 12])
style_cycle = list(color_cycle + marker_cycle + markersize_cycle)[:N]

cmap = brewer2mpl.get_map('Set1', 'Qualitative', 3, reverse=False)
color_cycle = cycler('color', ['black', '#88CCDD', '#c73027'])
marker_cycle = cycler('marker', [' ', ' ', ' '])
markersize_cycle = cycler('markersize', [8, 8, 8])
fillstyle_cycle = cycler('fillstyle', ['full', 'full', 'full'])
linestyle_cycle = cycler('linestyle', ['dashed', 'solid', 'solid'])
linewidth_cycle = cycler('linewidth', [2, 2.25, 2])
style_cycle_fig7 = list(color_cycle + marker_cycle + markersize_cycle + fillstyle_cycle + linestyle_cycle + linewidth_cycle)[:N]
