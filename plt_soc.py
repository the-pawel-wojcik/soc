"""
Script that help to visualize what's going on with SOC
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

CARTESIAN = ["x", "y", "z"]


def show_Hamiltonian(hamiltonian, title: str = ""):

    absH = np.zeros_like(hamiltonian, dtype=float)
    for rowID, row in enumerate(hamiltonian):
        for colID, value in enumerate(row):
            absH[rowID, colID] = np.log(1 + abs(value))

    max_value = absH.max()

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


def show_tdms(tdms_matrix):

    tdms_max = []
    for cart in CARTESIAN:
        row_with_max = max(tdms_matrix[cart], key=lambda x: abs(
            max(x, key=lambda y: abs(y))))
        max_element = max(row_with_max, key=lambda x: abs(x))
        tdms_max += [max_element]

    max_tdm = max(tdms_max)

    for cart in CARTESIAN:
        # TODO: print the thing
        # fig, ax = plt.subplots(figsize=(2, 4))
        fig, ax = plt.subplots(figsize=(3, 3))

        # annotations = [['A'], ['F'], ['Z']]
        # labels = [1]

        parameters = {
            "vmin": -max_tdm,
            "vmax": max_tdm,
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

        ax = sns.heatmap(tdms_matrix[cart], **parameters)
        plt.title(f"TDMs matrix the {cart} component")
        plt.show()
