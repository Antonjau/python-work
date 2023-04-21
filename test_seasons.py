from datetime import date
from seasons import calculate_age_in_minutes


def test_calculate_age_in_minutes():
    dob = date(2000, 1, 1)
    assert calculate_age_in_minutes(dob) == 5256000

    dob = date(2001, 1, 1)
    assert calculate_age_in_minutes(dob) == 5184000

    dob = date(2010, 6, 15)
    assert calculate_age_in_minutes(dob) == 2534400

    dob = date(2015, 12, 31)
    assert calculate_age_in_minutes(dob) == 357840

    dob = date(2023, 4, 20)
    assert calculate_age_in_minutes(dob) == 0

    dob = date(1900, 1, 1)
    assert calculate_age_in_minutes(dob) == 15033120


if __name__ == "__main__":
    test_calculate_age_in_minutes()
    print("All tests pass")
