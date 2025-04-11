import logging
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)

def get_mask_card_number(card_number: str) -> str:
    logger.info(f"Начало маскировки номера карты: {card_number}")
    card_number = str(card_number)

    block_1 = card_number[:4]
    block_2 = card_number[4:6] + "**"
    block_3 = "****"
    block_4 = card_number[-4:]

    masked_card = f"{block_1} {block_2} {block_3} {block_4}"

    logger.info(f"Маскированный номер карты: {masked_card}")
    return masked_card

def get_mask_account(number_acc: str) -> str:
    logger.info(f"Начало маскировки номера счета: {number_acc}")
    if len(number_acc) < 4:
        logger.warning(f"Некорректный номер счета: {number_acc}")
        return "Неверный номер счёта"
    masked_account = f"**{number_acc[-4:]}"
    logger.info(f"Маскированный номер счета: {masked_account}")
    return masked_account


get_mask_account('28831920132347')
get_mask_card_number('4214421122223333')

