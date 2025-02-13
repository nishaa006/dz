import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567891011234", "1234 56** **** 1234"),
        ("123456789", "1234 56** **** 6789"),
        ("123456789101123459012", "1234 56** **** 9012"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "number_acc, expected1",
    [("73654108430135874305", "**4305"), ("73654430135874305", "**4305"), ("73654108430135879024305", "**4305")],
)
def test_get_mask_account(number_acc: str, expected1: str) -> None:
    assert get_mask_account(number_acc) == expected1
