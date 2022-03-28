import imp
from prg_tetelek import count_accented, sum_numbers         # Ezzel importáljuk be a file-okat
from prg_tetelek import hun_counter
from prg_tetelek import count_accented


def test_sum():
    # given
    numbers = [1, 2, 3, 4]
    # when
    result = sum_numbers(numbers)
    # then
    # összehasonlítjuk az elvárt értéket a kapott értékkel
    assert result == 10 # Output

def test_sum_short():
    assert sum_numbers([1, 2, 3, 5]) == 11

def hun_counter_test():
    assert hun_counter("tűzőgép") == 3

def test_count_accented():
    assert count_accented("juhúnaonjó") == 2