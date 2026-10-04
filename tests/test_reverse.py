from pathlib import Path

from reverse import reverse


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

def read_file(filename):
    return get_test_data_path(filename).read_text()

def test_reverse():
    before_txt = read_file("before.txt")
    expected = read_file("after.txt")
    actual = reverse(before_txt)

    assert actual == expected