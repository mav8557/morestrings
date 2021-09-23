import morestrings

def test_sum_n():
    assert 0 == morestrings.sum_n(0)
    assert 15 == morestrings.sum_n(5)
    assert 0 == morestrings.sum_n(-1)
    # sum 0 - 10 and compare to sum_n(10)
    assert sum(range(11)) == morestrings.sum_n(10)

def test_first_two():
    assert "Da" == morestrings.first_two("Dale Cooper")
    assert "Di" == morestrings.first_two("Diane")
    assert "" == morestrings.first_two("")
    assert "A" == morestrings.first_two("A")

def test_real_len():
    assert 5 == morestrings.real_len("clean")
    assert 5 == morestrings.real_len("           clean")
    assert 5 == morestrings.real_len("           slice             ")

def test_last_index():
    assert 4 == morestrings.last_index("Annie")
    assert 3 == morestrings.last_index("Eric")
    assert 10 == morestrings.last_index("AAAABBBBCCC")

def test_comma_sum():
    assert 6 == morestrings.comma_sum("aa,bb,cc")
    assert 12 == morestrings.comma_sum("dale,diane,ben")