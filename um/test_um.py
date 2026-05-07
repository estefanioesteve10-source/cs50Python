from um import count

def test_isolated_um():
    assert count("um") == 1
    assert count("um um um") == 3
    assert count("Um, thanks for the album.") == 1

def test_punctuation():
    assert count("um?") == 1
    assert count("Hello, um...") == 1
    assert count("um, hello, um") == 2

def test_inside_words():
    # Estas palavras contêm 'um', mas não devem ser contadas
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("instrument") == 0

def test_case_insensitivity():
    assert count("UM") == 1
    assert count("uM") == 1
    assert count("Um") == 1
