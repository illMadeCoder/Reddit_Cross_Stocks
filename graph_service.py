import matplotlib.pyplot as plt
import numpy as np

# def produce_graph(data):
#     N = len(data)
#     ind = np.arange(3)
#     width = .4
#     fig = plt.figure()
#     ax = fig.add_subplot()
#     rects = ax.bar(ind, data.keys(), width, align='center')
#     # ax.set_xticks(np.arange(N) + width/2)
#     # ax.set_xticklabels(tuple(map(lambda a : a[0], data)))
#     plt.show()


#def my_plotter(ax, data1, data2, param_dict):
#     """
#     A helper function to make a graph

#     Parameters
#     ----------
#     ax : Axes
#         The axes to draw to

#     data1 : array
#        The x data

#     data2 : array
#        The y data

#     param_dict : dict
#        Dictionary of kwargs to pass to ax.plot

#     Returns
#     -------
#     out : list
#         list of artists added
#     """
#      out = ax.plot(data1, data2, **param_dict)
#      return out

def bar(data):
    data_items = data.items()
    data_items_sorted = sorted(data_items, key=lambda x : x[1], reverse=True)
    bar_limit = 10
    plt.bar(list(map(lambda x : x[0], data_items_sorted))[:bar_limit],
            list(map(lambda x : x[1], data_items_sorted))[:bar_limit])
    plt.ion()
    plt.show()
    return None
    
