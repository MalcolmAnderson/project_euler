import pytest
import pe26_reciprocal_cycles as pe26


def test_md_one_seventeenth_works():
    expected = "0.058823529411764705882352941176470588235294117647058823"
    actual, junk = pe26.manual_division(1, 17, 50)
    print(actual)
    assert expected == actual


def test_frp_one_seventeenth_works():
    expected = "0588235294117647"
    # known_value, junk = pe26.manual_division(1, 17, 50)
    # print(known_value)
    known_value = "0.058823529411764705882352941176470588235294117647058823"
    # actual = pe26.find_repeating_portion(known_value)
    actual = pe26.find_repeating_portion(known_value)
    # print(f"1/9 expected = .(52631578947368421) - actual = {find_repeating_portion("0.52631578947368421526315789473684215263157894736842")}")
    assert expected == actual


def test_frp_one_ninth_works():
    # expected = ".(52631578947368421)"
    expected = "52631578947368421"
    actual = pe26.find_repeating_portion("0.52631578947368421526315789473684215263157894736842")
    # print(f"1/9 expected = .(52631578947368421) - actual = {find_repeating_portion("0.52631578947368421526315789473684215263157894736842")}")
    assert expected == actual


def test_drc_one_eleventh_works():
    expected = "1/11 = 0.(09)"
    actual, junk = pe26.display_rc(11)
    assert expected == actual


def test_drc_one_seventeenth_works():
    expected = "1/17 = 0.(0588235294117647)"
    actual, junk = pe26.display_rc(17)
    assert expected == actual


def test_fdl_should_find_duplicate():
    r = "57862"  # r for "repeat"
    test = r * 3
    actual = pe26.find_repeating_portion(test)
    expected = r
    assert expected == actual


def test_fdl_one_seventeenth_works():
    expected = "0588235294117647"
    # known_value, junk = pe26.manual_division(1, 17, 50)
    # print(known_value)
    known_value = "0.058823529411764705882352941176470588235294117647058823"
    actual = pe26.find_repeating_portion(known_value)
    # print(f"1/9 expected = .(52631578947368421) - actual = {find_repeating_portion("0.52631578947368421526315789473684215263157894736842")}")
    assert expected == actual


def test_fdl_one_ninth_works():
    # expected = ".(52631578947368421)"
    expected = "52631578947368421"
    actual = pe26.find_repeating_portion("0.52631578947368421526315789473684215263157894736842")
    # print(f"1/9 expected = .(52631578947368421) - actual = {find_repeating_portion("0.52631578947368421526315789473684215263157894736842")}")
    assert expected == actual


def test_fdl_short_one_sixth_works():
    expected = "6"
    actual = pe26.find_repeating_portion("16666")
    # print(f"1/9 expected = .(52631578947368421) - actual = {find_repeating_portion("0.52631578947368421526315789473684215263157894736842")}")
    assert expected == actual


def test_fdl_short_one_thirty_fourth_works():
    expected = "2941176470588235"
    test_val = "0.0294117647058823529411764705882352941176470588235294117647058823529411764705882352941"
    test_val = pe26.manual_division(1, 34)[0]
    actual = pe26.find_repeating_portion(test_val)
    # print(f"1/34 expected = .0(2941176470588235) - actual = {find_repeating_portion("0.52631578947368421526315789473684215263157894736842")}")
    assert expected == actual


def test_fdl_one_716th_works():
    expected = "1396648044692737430167597765363128491620111731843575418994413407821229050279329608938547486033519553072625698324022346368715083798882681564245810055865921787709497206703910614525"
    # test_val = "0.0294117647058823529411764705882352941176470588235294117647058823529411764705882352941"
    print(f"{len(expected) = }")
    test_val = pe26.manual_division(1, 716)[0]
    actual = pe26.find_repeating_portion(test_val)
    print(f"{len(actual) = }")
    # print(f"1/34 expected = .0(2941176470588235) - actual = {find_repeating_portion("0.52631578947368421526315789473684215263157894736842")}")
    assert expected == actual


@pytest.mark.skip(reason="is_valid_repeating_sequence assumes that rounded char has been stripped")
def test_6_repeating_with_rounding_works():
    rest = "66667"
    candidate = "6"
    expected = True
    actual = pe26.is_valid_repeating_sequence(candidate, rest)
    assert expected == actual


def test_6_repeating_without_rounding_works():
    rest = "6666"
    candidate = "6"
    expected = True
    actual = pe26.is_valid_repeating_sequence(candidate, rest)
    assert expected == actual


@pytest.mark.skip(reason="currently not economical to handle edge case")
def test_6_with_fake_repeating_fails_correctly():
    rest = "66668"
    candidate = "6"
    expected = False
    actual = pe26.is_valid_repeating_sequence(candidate, rest)
    assert expected == actual
