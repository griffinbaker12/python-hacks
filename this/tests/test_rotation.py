from src import rotate_char, encode, decode


def test_rotation():
    """Test basic rotation functionality"""
    # lower
    assert rotate_char("a") == "n"
    assert rotate_char("n") == "a"
    assert rotate_char("z") == "m"

    # upper
    assert rotate_char("A") == "N"
    assert rotate_char("N") == "A"
    assert rotate_char("Z") == "M"


def test_non_letters():
    """Test that non-letters stay unchanged"""
    assert encode(" ") == " "
    assert encode("!") == "!"
    assert encode("123") == "123"


def test_encode_decode_symmetry():
    """Test that encode->decode gets original"""
    message = "the zen of python"
    assert "".join(decode(c) for c in "".join(encode(c) for c in message)) == message
