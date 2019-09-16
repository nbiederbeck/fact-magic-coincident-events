from sortedcontainers import SortedList
import numpy as np


def coincident_indices(list0, list1, delta):
    """Get indices of coincident times in both lists as dictionary.

    Parameters
    ----------
    list0 : list
        List of times
    list1 : list
        List of times (preferably longer than ``list0``)
    delta : float
        Time-delta slice

    Returns
    -------
    coincidents : dict
        {index_list0: index_list1}

    """
    slist0 = SortedList(list0)
    slist1 = SortedList(list1)

    coincidents = {}

    for t0 in iter(slist0):
        times = list(slist1.irange(t0 - delta, t0 + delta))
        diffs = []
        for t1 in iter(times):
            diffs.append(abs(t0 - t1))
        if len(diffs) > 0:
            coincidents[slist0.index(t0)] = slist1.index(times[np.argmin(diffs)])

    return coincidents


def coincidents(list0, list1, indices):
    """Get coincident values from lists based on indices calculated.

    Parameters
    ----------
    list0 : list
        List of values
    list1 : list
        List of values
    indices : dict
        Dictionary containing index mapping

    Returns
    -------
    items : dict
        {value0: value1}

    """
    items = {}
    for index0, index1 in indices.items():
        items[list0[index0]] = list1[index1]

    return items
