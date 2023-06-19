import task2


def test_odd_indexes():
    assert task2.odd_indexes("hello") == "el"
    assert task2.odd_indexes("cupcakes") == "ucks"
    assert task2.odd_indexes("what is happening?") == "hti apnn?"
    assert task2.odd_indexes(4342) == "32"
