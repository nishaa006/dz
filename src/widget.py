from src import masks


def mask_account_card(account: str) -> str:
    num = ""
    card_num = ""
    for i in account:
        if i.isdigit():
            num += i
        else:
            card_num += i

    if card_num == "Счет":
        card_num += masks.get_mask_account(num)
    else:
        card_num += masks.get_mask_card_number(num)

    return card_num


def get_date(date: str) -> str:
    date_form = f"{date[8:10]+'.'+date[5:7]+'.'+date[2:4]}"
    if "T" in date:
        date = date.split("T")[0]
    return date_form




print(get_date('2024-03-11T02:26:18.671407'))