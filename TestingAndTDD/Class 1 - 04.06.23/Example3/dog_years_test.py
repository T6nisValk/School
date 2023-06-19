import pytest

import dog_years


@pytest.mark.parametrize("human_year, dog_year",
                         [(4, 29),
                          (31, 137),
                          (9, 49),
                          (0, 0),
                          (-34, 0)])
def test_human_to_dog_years(human_year, dog_year):
    assert dog_years.human_to_dog_years(human_year) == dog_year
