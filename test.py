"""Doing tests, very cool."""
from main import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(1, True) is False


def test__students_study__night_without_coffee__no_studying():
    """During night without coffee students do not study."""
    assert students_study(4, False) is False


def test__students_study__evening_without_coffee__no_studying():
    """Doing Testing, Testing Test."""
    assert students_study(24, False) is True


def test__students_study__evening_with_coffee__no_studying():
    """Doing Testing, Testing ."""
    assert students_study(24, True) is True


def test__students_study__day_without_coffee__no_studying():
    """During day without coffee students do not study."""
    assert students_study(17, False) is False


def test__students_study__day_with_coffee__no_studying():
    """During day with coffee students do study."""
    assert students_study(5, True) is True


def test__students_study__evening_edge_case():
    """Doing Testing, Testing ."""
    assert students_study(24, True) == students_study(18, True) is True


def test__students_study__evening_edge_case_no_coffee():
    """Doing Testing, Testing Test."""
    assert students_study(24, False) == students_study(18, False) is True


def test__students_study__night_edge_case():
    """Doing Testing, Testing Test."""
    assert students_study(1, True) == students_study(4, True) is False


def test__students_study__night_edge_case_no_coffee():
    """Doing Testing, Testing Test."""
    assert students_study(1, False) == students_study(4, False) is False


def test__students_study__day_edge_case():
    """Doing Testing, Testing Test."""
    assert students_study(17, True) == students_study(5, True) is True


def test__students_study__day_edge_case_no_coffee():
    """Doing Testing, Testing Test."""
    assert students_study(17, False) == students_study(5, False) is False


def test__lottery_using_all_fives():
    """Doing Testing, Testing Test."""
    assert lottery(5, 5, 5) == 10


def test__lottery__using_all_same_positive():
    """Doing Testing, Testing Test."""
    assert lottery(3, 3, 3) == 5


def test__lottery__using_all_same_negative():
    """Doing Testing, Testing Test."""
    assert lottery(-3, -3, -3) == 5


def test__lottery__all_same_zero():
    """Doing Testing, Testing Test."""
    assert lottery(0, 0, 0) == 5


def test__lottery__a_b_same_c_diff():
    """Doing Testing, Testing Test."""
    assert lottery(4, 4, 2) == 0


def test__lottery__a_c_same_b_diff():
    """Doing Testing, Testing Test."""
    assert lottery(4, 2, 4) == 0


def test__lottery__b_c_same_a_diff():
    """Doing Testing, Testing Test."""
    assert lottery(2, 4, 4) == 1


def test__lottery__all_diff():
    """Doing Testing, Testing Test."""
    assert lottery(2, 3, 1) == 1


def test__fruit_order__all_zero():
    """Doing Testing, Testing Test."""
    assert fruit_order(0, 0, 0) == 0


def test__fruit_order__zero_amount_zero_big():
    """Doing Testing, Testing Test."""
    assert fruit_order(5, 0, 0) == 0


def test__fruit_order__zero_amount_zero_s():
    """Doing Testing, Testing Test."""
    assert fruit_order(0, 2, 0) == 0


def test__fruit_order__zero_amount_others_not_zero():
    """Doing Testing, Testing Test."""
    assert fruit_order(7, 2, 0) == 0


def test__fruit_order__only_big_exact_match():
    """Doing Testing, Testing Test."""
    assert fruit_order(0, 2, 10) == 0


def test__fruit_order__only_big_not_enough_but_multiple_of_5():
    """Doing Testing, Testing Test."""
    assert fruit_order(0, 10, 50) == 0


def test__fruit_order__only_big_not_enough():
    """Doing Testing, Testing Test."""
    assert fruit_order(0, 2, 20) == -1


def test__fruit_order__only_big_more_than_required_match():
    """Doing Testing, Testing Test."""
    assert fruit_order(0, 10, 20) == 0


def test__fruit_order__only_big_more_than_required_no_match():
    """Doing Testing, Testing Test."""
    assert fruit_order(0, 10, 24) == -1


def test__fruit_order__only_s_match_more_than_5_ss():
    """Doing Testing, Testing Test."""
    assert fruit_order(7, 0, 7) == 7


def test__fruit_order__only_s_not_enough_more_than_5_ss():
    """Doing Testing, Testing Test."""
    assert fruit_order(6, 0, 7) == -1


def test__fruit_order__only_s_exact_match():
    """Doing Testing, Testing Test."""
    assert fruit_order(1, 0, 1) == 1


def test__fruit_order__only_s_not_enough():
    """Doing Testing, Testing Test."""
    assert fruit_order(1, 0, 3) == -1


def test__fruit_order__only_s_more_than_required():
    """Doing Testing, Testing Test."""
    assert fruit_order(5, 0, 3) == 3


def test__fruit_order__match_with_more_than_5_ss():
    """Doing Testing, Testing Test."""
    assert fruit_order(50, 15, 100) == 25


def test__fruit_order__all_positive_exact_match():
    """Doing Testing, Testing Test."""
    assert fruit_order(50, 10, 100) == 50


def test__fruit_order__use_all_ss_some_bigs():
    """Doing Testing, Testing Test."""
    assert fruit_order(1, 1, 1) == 1


def test__fruit_order__use_all_bigs_some_ss():
    """Doing Testing, Testing Test."""
    assert fruit_order(5, 20, 100) == 0


def test__fruit_order__use_some_ss_some_bigs():
    """Doing Testing, Testing Test."""
    assert fruit_order(120, 120, 124) == 4


def test__fruit_order__not_enough():
    """Doing Testing, Testing Test."""
    assert fruit_order(1, 1, 50) == -1


def test__fruit_order__enough_bigs_not_enough_ss():
    """Doing Testing, Testing Test."""
    assert fruit_order(4, 11, 55) == 0


def test__fruit_order__enough_ss_not_enough_bigs():
    """Doing Testing, Testing Test."""
    assert fruit_order(11, 1, 15) == 10


def test__fruit_order__not_enough_with_more_than_5_ss():
    """Doing Testing, Testing Test."""
    assert fruit_order(20, 1, 50) == -1


def test__fruit_order__enough_bigs_not_enough_s_l_numbers():
    """Doing Testing, Testing Test."""
    assert fruit_order(2, 600, 1158) == -1


def test__fruit_order__match_l_numbers():
    """Doing Testing, Testing Test."""
    assert fruit_order(200, 200, 1200) == 200
