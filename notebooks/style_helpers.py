from cycler import cycler

# The color values are obtained from Colorbrewer (http://colorbrewer2.org/)
# They are from the 'Qualitative' Set1 color scheme using N=5 data classes.

hex_colors = ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00']
color_cycle = cycler('color', hex_colors)
marker_cycle = cycler('marker', ['s', '^', 'o', 'D', 'v'])
markersize_cycle = cycler('markersize', [10, 12, 11, 10, 12])
style_cycle = list(color_cycle + marker_cycle + markersize_cycle)

color_cycle = cycler('color', ['black', '#88CCDD', '#c73027'])
marker_cycle = cycler('marker', [' ', ' ', ' '])
markersize_cycle = cycler('markersize', [8, 8, 8])
fillstyle_cycle = cycler('fillstyle', ['full', 'full', 'full'])
linestyle_cycle = cycler('linestyle', ['dashed', 'solid', 'solid'])
linewidth_cycle = cycler('linewidth', [2, 2.25, 2])
style_cycle_fig7 = list(color_cycle + marker_cycle + markersize_cycle + fillstyle_cycle + linestyle_cycle + linewidth_cycle)
