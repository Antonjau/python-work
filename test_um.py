from um import count

def test_count_no_um():
    assert count("This sentence has no ums in it.") == 0

def test_count_single_um():
    assert count("There's only one um in this sentence.") == 1

def test_count_multiple_um():
    assert count("Um, let me think...um, um, um...") == 3

def test_count_case_insensitive():
    assert count("um, UM, uM, Um") == 4

def test_count_only_um_as_word():
    assert count("This should not count as an umlaut: üm") == 0

def test_count_empty_string():
    assert count("") == 0
