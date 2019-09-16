def merge_events(items0, items1, data0, data1):
    """Merge events.

    Merge two dataframes based on given items.
    The ``items`` should be a subset of the ``data``s index.

    Parameters
    ----------
    items0 : list
    items1 : list
    data0 : pandas.DataFrame
    data1 : pandas.DataFrame

    Returns
    -------
    merged : pandas.DataFrame

    """
    data0["index0"] = data0.index
    data0 = data0.loc[data0.index.intersection(items0)]
    data0 = data0.reindex(items0)
    data0.index = range(len(data0))

    data1["index1"] = data1.index
    data1 = data1.loc[data1.index.intersection(items1)]
    data1 = data1.reindex(items1)
    data1.index = range(len(data1))

    merged = data0.join(data1)

    return merged
