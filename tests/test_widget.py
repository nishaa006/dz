import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "acc, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(acc: str, expected: str) -> None:
    assert mask_account_card(acc) == expected


@pytest.mark.parametrize("acc", ["", None, "abcd efgh", "1234", "111122223333"])
def test_mask_account_card_invalid(acc: str) -> None:
    """Проверяет, что некорректные данные вызывают ValueError."""
    if acc is None:
        with pytest.raises(TypeError):
            mask_account_card(acc)


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2023-08-15", "15.08.23"),
        ("2000-01-01", "01.01.00"),
        ("2024-03-11T02:26:18.671407", "11.03.24"),
    ],
)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected
