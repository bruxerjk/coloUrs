import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import ListedColormap
from matplotlib import cm

def my_combined_cmap(cmap1, cmap2, name="my_cmap"):
    '''
    Combines two colour maps, cmap1 and cmap2, to form one 
    single colour map with name attribute = name
    '''
    top = cm.get_cmap(cmap1, 128)
    bottom = cm.get_cmap(cmap2, 128)
    newcolors = np.vstack((top(np.linspace(0,1,128)),
                           bottom(np.linspace(0,1,128))))
    my_cmap = ListedColormap(newcolors, name=name)
    
    return my_cmap


def my_diverging_cmap(bottom_colour, top_colour, name="my_colour_map"):
    '''
    Creates a diverging colour map from two colours (bottom_colour, top_colour)
    '''
    N = 256
    
    r,g,b = mcolors.to_rgb(bottom_colour)

    c1 = np.ones((N, 4))
    c1[:, 0] = np.linspace(r, 1, N) 
    c1[:, 1] = np.linspace(g, 1, N) 
    c1[:, 2] = np.linspace(b, 1, N)  
    c1_cmp = ListedColormap(c1)
    
    r,g,b = mcolors.to_rgb(top_colour)

    c2 = np.ones((N, 4))
    c2[:, 0] = np.linspace(r, 1, N)
    c2[:, 1] = np.linspace(g, 1, N)
    c2[:, 2] = np.linspace(b, 1, N)
    c2_cmp = ListedColormap(c2)

    newcolors = np.vstack((c1_cmp(np.linspace(0, 1, 128)),
                           c2_cmp(np.linspace(1, 0, 128))))

    my_cmap = ListedColormap(newcolors, name=name)
    
    return my_cmap


def plot_color_gradients(category, cmap_list):
    '''
    Plots swaths of colour maps
    
    '''
    
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
                        left=0.2, right=0.99)
    axs[0].set_title(f'{category} colormaps', fontsize=14)

    for ax, name in zip(axs, cmap_list):
        
        # adapted this to work with custom cmaps, which can't 
        # be searched by name
        if isinstance(name, str) is False:
            cmap = plt.get_cmap(name)
            name = name.name
        else:
            cmap = plt.get_cmap(name)
            
        ax.imshow(gradient, aspect='auto', cmap=cmap)
        ax.text(-0.01, 0.5, name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

BlOr = my_diverging_cmap("mediumblue", "#d17a00", "Blue_Orange")
DryWet = my_combined_cmap("YlOrBr_r", "PuBu", "Dry_Wet")
Habs = my_diverging_cmap("#AB0722", "#001363", "Go Habs!!!")
GoPu = my_diverging_cmap("gold", "darkviolet", "Gold_Purple")

LAGear = GoPu
LAGear.name = "LA Gear"

mine = [BlOr, DryWet, Habs, LAGear]

# tests...


# # built-in colour maps
# plot_color_gradients('Diverging',
#                      ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu',
#                       'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic'])

# # mine
# plot_color_gradients('My Colour Maps',
#                      [BlOr, drywet, badgood])