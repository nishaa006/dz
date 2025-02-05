def get_mask_card_number(card_number: str) -> str:
    card_number = str(card_number)

    # Формируем замаскированные блоки
    block_1 = card_number[:4]
    block_2 = card_number[4:6] + "**"
    block_3 = "****"
    block_4 = card_number[-4:]

    # Объединяем блоки с пробелами
    masked_card = f"{block_1} {block_2} {block_3} {block_4}"

    return masked_card


def get_mask_account(number_acc: str) -> str:
    str_number = str(number_acc)
    if len(number_acc) < 4:
        return "Неверный номер счёта"
    return f"**{number_acc[-4:]}"
