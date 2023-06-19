import text_functions

text = "wed WErt eey an"


def test_swap_case():
    assert text_functions.swap_case(text) == "WED weRT EEY AN"


def test_shortest_word():
    assert text_functions.shortest_word(text) == "an"
