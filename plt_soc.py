"""
Script that help to visualize what's going on with SOC
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def show_Hamiltonian(hamiltonian, title: str = ""):

    absH = np.log(1 + np.abs(hamiltonian))
    max_value = np.max(absH)

    fig, ax = plt.subplots(figsize=(3, 3))

    parameters = {
        "vmin": -max_value,
        "vmax": max_value,
        "center": 0.0,
        "cmap": "vlag",
        # "cmap": "vlag",  # diverging
        # "annot": annotations,  # bool or matrix
        # "fmt": '',  # string formatting options for displaying annot
        "linewidth": 0.5,  # width of the lines that divide cells.
        "square": True,
        "cbar": True,  # draw color bar
        "ax": ax,  # Axes where the figure will be drawn
        # "cbar_ax": None,  # Axis for the color bar, i.e., the legend
        # "xticklabels": labels,
        # 'yticklabels': [r'$\alpha$', r'$\beta$', r'$\gamma$'],
    }

    ax = sns.heatmap(absH, **parameters)
    plt.title("Log(1+Abs) values of\n" + title)
    plt.show()


def show_real_matrix(matrix: np.ndarray, title: str = ""):

    max_element = np.abs(matrix).max()
    if max_element < 1e-3:
        return 0

    # TODO: print the thing
    # fig, ax = plt.subplots(figsize=(2, 4))
    fig, ax = plt.subplots(figsize=(3, 3))

    # annotations = [['A'], ['F'], ['Z']]
    # labels = [1]

    parameters = {
        "vmin": -max_element,
        "vmax": max_element,
        "center": 0.0,
        "cmap": "vlag",
        # "cmap": "vlag",  # diverging
        # "annot": annotations,  # bool or matrix
        # "fmt": '',  # string formatting options for displaying annot
        "linewidth": 0.5,  # width of the lines that divide cells.
        "square": True,
        "cbar": True,  # draw color bar
        "ax": ax,  # Axes where the figure will be drawn
        # "cbar_ax": None,  # Axis for the color bar, i.e., the legend
        # "xticklabels": labels,
        # 'yticklabels': [r'$\alpha$', r'$\beta$', r'$\gamma$'],
    }

    ax = sns.heatmap(matrix, **parameters)
    plt.title(title)
    plt.show()
