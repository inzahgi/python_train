import numpy as np
import matplotlib.pyplot as plt


def simple_line_plot(x, y, figure_no):
    plt.figure(figure_no)
    plt.plot(x, y)
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Simple Line')

def simple_dots(x, y, figure_no):
    plt.figure(figure_no)
    plt.plot(x, y, 'or')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Simple Dots')

def simple_scatter(x, y, figure_no):
    plt.figure(figure_no)
    plt.scatter(x,y)
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Simple scatter')

def scatter_with_color(x, y, labels, figure_no):
    plt.figure(figure_no)
    plt.scatter(x, y, c=labels)
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Scatter with color')

def x_y_axis_labeling(x,y,x_labels, y_labels, figure_no):
    plt.figure(figure_no)
    plt.plot(x, y, '+r')
    plt.margins(0.2)
    plt.xticks(x, x_labels, rotation='vertical')
    plt.yticks(y, y_labels)

def plot_heat_map(x, figure_no):
    plt.figure(figure_no)
    plt.pcolor(x)
    plt.colorbar()

if __name__=="__main__":

    plt.close("all")
    x = np.arange(1, 100, dtype=float)
    y = np.array([np.power(xx, 2) for xx in x])

    figure_no = 1
    simple_line_plot(x, y, figure_no)

    figure_no += 1
    simple_dots(x, y, figure_no)

    x = np.random.uniform(size=100)
    y = np.random.uniform(size=100)

    figure_no += 1
    simple_scatter(x, y, figure_no)
    figure_no += 1
    label = np.random.randint(2, size=100)
    scatter_with_color(x, y, label, figure_no)



    figure_no += 1
    x=np.array(range(1,6))
    y=np.array(range(100, 600, 100))
    x_label = ['element 1', 'element 2', 'element 3', 'element 4', 'element 5']
    y_label = ['weight 1', 'weight 2', 'weight 3', 'weight 4', 'weight 5']
    x_y_axis_labeling(x, y, x_label, y_label, figure_no)

    figure_no += 1
    x = np.random.normal(loc=0.5, scale=0.2, size=(10,10))
    plot_heat_map(x, figure_no)

    plt.show()
