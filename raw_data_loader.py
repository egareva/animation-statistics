import dataclasses

from structures import ChannelData, AnimationInfo, DatabaseRow
from utils import tools
from utils.rating import get_rating
from os import walk
from utils.channel_data_validator import ChannelDataValidator
import csv


class DatabaseLoader:
    @staticmethod
    def load(filename: str):
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            return [DatabaseRow(title=line[0], year=line[1]) for line in reader]


class RawDataLoader:
    @classmethod
    def load_raw_data(cls, filename: str) -> ChannelData:
        """
        Читает файл и возвращает статистику по каналу
        """
        with open(filename, "r", encoding="utf-8") as file:
            channel_name = file.readline().strip()
            channel_url = file.readline().strip()
            channel_data = ChannelData(
                title=channel_name,
                link=channel_url,
                votes=[],
            )
            index = 1

            for line in file:
                if line.startswith("#") or not line.strip():
                    # пропускаем комментарии и пустые строки
                    continue
                year = tools.get_year(line) or ''
                title_name = tools.get_cleaned_data(line)
                channel_data.votes.append(
                    AnimationInfo(
                        name=title_name,
                        year=year,
                        index=index,
                        rating=get_rating(index, channel_name)),
                )
                index += 1
        return channel_data

    @classmethod
    def get_titles_info_from_folder(cls, folder_name: str, database: list[DatabaseRow]) -> list[ChannelData]:
        filenames = next(walk(folder_name), (None, None, []))[2]
        chanel_infos: list[ChannelData] = []
        for filename in filenames:
            chanel_data = cls.load_raw_data(f"{folder_name}/{filename}")
            ChannelDataValidator.validate(chanel_data, database=database)
            chanel_infos.append(chanel_data)
        return chanel_infos


def main():
    database = DatabaseLoader.load("animation_database.csv")
    chanel_infos = RawDataLoader.get_titles_info_from_folder("./raw", database)

    titles = set()
    for chanel in chanel_infos:
        for title in chanel.votes:
            titles.add((title.name, title.year))


if __name__ == "__main__":
    main()
