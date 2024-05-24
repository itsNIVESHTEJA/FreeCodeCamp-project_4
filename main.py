from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Test and visualize the functions
if __name__ == "__main__":
    # Draw line plot and display
    line_fig = draw_line_plot()
    line_fig.show()

    # Draw bar plot and display
    bar_fig = draw_bar_plot()
    bar_fig.show()

    # Draw box plot and display
    box_fig = draw_box_plot()
    box_fig.show()
