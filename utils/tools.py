import re


def remove_dot_prefix(text: str) -> str:
    """ Списки вида: 1."""
    exclusion_list = []
    for exclusion in exclusion_list:
        if text.startswith(exclusion):
            return text
    return re.sub(r'^\d+\.', '', text)


def remove_space_prefix(text: str) -> str:
    """ Списки вида: 1"""
    exclusion_list = ()
    for exclusion in exclusion_list:
        if text.startswith(exclusion):
            return text
    return re.sub(r'^\d+ ', '', text)


def remove_bracket_prefix(text: str) -> str:
    """ Списки вида: 1)"""
    exclusion_list = []
    for exclusion in exclusion_list:
        if text.startswith(exclusion):
            return text
    return re.sub(r'^\d+\)', '', text)


def remove_dash_prefix(text: str) -> str:
    """ Списки вида: 1-"""
    exclusion_list = []
    for exclusion in exclusion_list:
        if text.startswith(exclusion):
            return text
    return re.sub(r'^\d+-', '', text)


def clean_symbols(text: str) -> str:
    for symbol in ('"', ":", "»", "«", ",", ".", "!", "-"):
        text = text.replace(symbol, "")
    return text


def clean_quotes(text: str) -> str:
    for symbol in ('"', "»", "«"):
        text = text.replace(symbol, "")
    return text


def remove_year(text: str) -> str:
    # если в строке есть год в скобках, убирает его
    return re.sub(r'\(\d{4}\)', '', text)


def get_year(text: str) -> str | None:
    if 'Тяжелый металл 2000' in text:
        return '1999'
    matched = re.search('.*(\d{4}).*$', text)
    if matched:
        return matched.groups()[0]


def get_cleaned_data(text: str) -> str:
    text = remove_space_prefix(text).strip()
    text = remove_dot_prefix(text).strip()
    text = remove_bracket_prefix(text).strip()
    text = remove_dash_prefix(text).strip()
    text = remove_year(text)
    return text.strip()
