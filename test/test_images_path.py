import os
import tempfile
import pytest
from testfixtures import TempDirectory, tempdir, compare
from pathlib import Path

from src.images_path import get_all_directories_recursive, get_all_image_path


SKIP_TEST = False


@pytest.fixture
def directories():
    with TempDirectory() as root:
        root.makedir(("folder_1", "sub_folder_1"))
        root.makedir(("folder_1", "sub_folder_2"))
        root.makedir(("folder_2", "a"))
        root.makedir(("folder_2", "b"))
        yield root


@pytest.mark.skipif(SKIP_TEST, reason="Trying new method")
def test_get_all_directories_recursive(directories: pytest.fixture):
    full_paths = get_all_image_path(directories.as_string())
    cleared_paths = []
    for item in full_paths:
        ls = item.split("\\")
        for pos, val in enumerate(ls):
            if val == "Temp":
                cleared_paths.append("\\".join([i for i in ls[pos + 2 :]]))
                break
    assert [
        "folder_1",
        "folder_2",
        "folder_1\\sub_folder_1",
        "folder_1\\sub_folder_2",
        "folder_2\\a",
        "folder_2\\b",
    ] == cleared_paths


@pytest.mark.skipif(True, reason="Trying new method")
def test_get_all_directories_recursive_with_empty_directory():
    # Test when the directory is empty
    with tempfile.TemporaryDirectory() as temp_dir:
        result = get_all_directories_recursive(temp_dir)
        assert result == [temp_dir]


def test_get_all_image_path():
    path = os.getcwd()
    assert "" == get_all_image_path(path)
