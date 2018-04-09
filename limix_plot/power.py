from __future__ import division

import matplotlib.pyplot as plt
from numpy import asarray, linspace


def power(pv, label=None, pts_kws=None, ax=None):
    r"""Plot number of hits across significance levels.

    Parameters
    ----------
    pv : array_like
        P-values.
    label : string, optional
        Legend label for the relevent component of the plot.
    pts_kws : dict, optional
        Keyword arguments forwarded to the matplotlib function used for
        plotting the points.
    ax : matplotlib Axes, optional
        The target handle for this figure. If ``None``, the current axes is
        set.

    Returns
    -------
    ax : matplotlib Axes
        Axes object with the plot for further tweaking.
    """

    pv = asarray(pv).ravel()

    ax = plt.gca() if ax is None else ax

    if pts_kws is None:
        pts_kws = dict()
    if 'label' not in pts_kws:
        pts_kws['label'] = label

    alphas, nhits = _collect_nhits(pv)
    ax.plot(alphas, asarray(nhits, int), **pts_kws)

    ax.set_xlabel('significance level')
    ax.set_ylabel('number of hits')

    return ax


def _collect_nhits(pv):
    alphas = linspace(0.01, 0.5, 500)
    nhits = []

    for alpha in alphas:
        n = (pv < alpha).sum()
        nhits += [n]

    nhits = asarray(nhits, int)

    return (alphas, nhits)