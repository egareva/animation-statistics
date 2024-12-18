def get_rating(index: int, channel_name: str) -> int:
    if index == 1:
        return 5
    if 2 <= index <= 5:
        return 3
    if 6 <= index <= 10:
        return 2
    if index > 30:
        raise Exception(f"{channel_name} has more than 30 films")
    return 1
