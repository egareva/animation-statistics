import collections

from structures import ChannelData, DatabaseRow
from utils.words_similarity import jaccard_similarity


class ChannelDataValidator:
    MAX_TITLES_COUNT = 30

    @staticmethod
    def validate_titles_count(channel_data: ChannelData):
        if len(channel_data.votes) != ChannelDataValidator.MAX_TITLES_COUNT:
            print(f"{channel_data.title} count {len(channel_data.votes)}")

    @staticmethod
    def validate_same_titles(channel_data: ChannelData):
        if len(channel_data.votes) != len(set(channel_data.votes)):
            print(f"{channel_data.title} has same titles")
            print([item for item, count in collections.Counter(channel_data.votes).items() if count > 1])

    @staticmethod
    def offer_correct_title(title: str, index: int, database_titles: set[str]):
        offer_list = []
        for d_title in database_titles:
            if jaccard_similarity(title, d_title) > 0.3:
                offer_list.append(f"[{index}] {title} -> {d_title}")
        return offer_list

    @staticmethod
    def validate_title_in_database(channel_data: ChannelData, database: list[DatabaseRow]):
        titles = {d.title for d in database}
        title_years = {(d.title, d.year) for d in database}
        for t in channel_data.votes:
            if t.name in titles and t.year and (t.name, t.year) not in title_years:
                print(f"{channel_data.title} | [{t.index}] {t.name}, {t.year} - not exist in database")
                print([f"{d.title}, {d.year}" for d in database if d.title == t.name])
            if t.name not in titles:
                print(f"{channel_data.title} | {t.name} - not exists")
                offers = ChannelDataValidator.offer_correct_title(t.name, t.index, database_titles=titles)
                if not offers:
                    print("No offers")
                else:
                    for offer in offers:
                        print(offer)


    @staticmethod
    def validate(channel_data: ChannelData, database: list[DatabaseRow] = None):
        # ChannelDataValidator.validate_titles_count(channel_data)
        ChannelDataValidator.validate_same_titles(channel_data)
        if database:
            ChannelDataValidator.validate_title_in_database(channel_data, database=database)

