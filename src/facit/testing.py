import deepdiff
from xarray.testing import assert_equal


def assert_ds_equal(a, b):
    def _all_attrs(x):
        return {name: var.attrs for name, var in x.variables.items()}

    assert_equal(a, b)
    assert not deepdiff.DeepDiff(a.attrs, b.attrs)
    assert not deepdiff.DeepDiff(
        _all_attrs(a),
        _all_attrs(b),
    )
    assert a.variables.keys() == b.variables.keys()
