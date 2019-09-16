import pandas as pd
from pandas.util.testing import assert_frame_equal
from timing_neighbors.eventmerge import merge_events


def test_merge_events_0():
    items0 = [1, 2, 4]
    items1 = [2, 3, 5]

    data0 = pd.DataFrame(
        data={"A": [1, 1, 2, 3, 5], "items": [1, 2, 4, 8, 16], "B": [1, 4, 16, 64, 256]}
    )

    data1 = pd.DataFrame(
        data={"C": [6, 4, 3, 2, 2], "items": [17, 9, 5, 3, 2], "D": [257, 65, 17, 5, 2]}
    )

    data0 = data0.set_index("items")
    data1 = data1.set_index("items")

    merged = merge_events(items0, items1, data0, data1)

    solution = pd.DataFrame(
        data={
            "A": [1, 1, 2],
            "B": [1, 4, 16],
            "index0": items0,
            "C": [2, 2, 3],
            "D": [2, 5, 17],
            "index1": items1,
        }
    )

    assert_frame_equal(merged, solution)
