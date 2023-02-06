import pathlib

from wradlib_data import DATASETS, locate


def test_registry():
    files = DATASETS.registry_files
    assert len(files) > 0


def test_locate():
    p = locate()
    assert 'wradlib-data' in p
    assert pathlib.Path(p)
