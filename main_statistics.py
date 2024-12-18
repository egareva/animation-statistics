from structures import ChannelData, AnimationInfoStatistics
from raw_data_loader import RawDataLoader, DatabaseLoader
from collections import OrderedDict, defaultdict


def count_statistics(channel_data_list: list[ChannelData]) -> OrderedDict[str, AnimationInfoStatistics]:
    animation_statistics: OrderedDict[str, AnimationInfoStatistics] = OrderedDict()

    for channel_data in channel_data_list:
        for info in channel_data.votes:
            if info.name not in animation_statistics:
                animation_statistics[info.name] = AnimationInfoStatistics(
                    title=info.name,
                    total_rating=0,
                    total_votes=0,
                    rating_dict={5: 0, 3: 0, 2: 0, 1: 0},
                    places_dict={i: 0 for i in range(1, 31)},
                    final_place=None,
                    average_vote_place=None,
                )
            animation_statistics[info.name].total_rating += info.rating
            animation_statistics[info.name].total_votes += 1
            animation_statistics[info.name].rating_dict[info.rating] += 1
            animation_statistics[info.name].places_dict[info.index] += 1

    for animation_statistic in animation_statistics.values():
        places_sum = 0
        places_count = 0
        for place, count in animation_statistic.places_dict.items():
            if count:
                places_sum += place
                places_count += 1
        animation_statistic.average_vote_place = places_sum/places_count
    return animation_statistics


def sort_animation_info_by_rating(
        animation_info_statistics: OrderedDict[str, AnimationInfoStatistics]
) -> list[AnimationInfoStatistics]:
    sorted_values: list[AnimationInfoStatistics] = sorted(
        animation_info_statistics.values(),
        key=lambda item: (
            item.total_rating,
            item.total_votes,
            item.rating_dict[5],
            item.rating_dict[3],
            item.rating_dict[2],
            item.rating_dict[1],
            item.places_dict[2],
            item.places_dict[3],
            item.places_dict[4],
            item.places_dict[5],
            item.places_dict[6],
            item.places_dict[7],
            item.places_dict[8],
            item.places_dict[9],
            item.places_dict[10],
            item.places_dict[11],
            item.places_dict[12],
            item.places_dict[13],
            item.places_dict[14]
        ),
        reverse=True,
    )
    for index, value in enumerate(sorted_values, start=1):
        # value.title_name = f"{value.title_name} [{index}]"
        value.final_place = index
    return sorted_values


def main():
    database = DatabaseLoader.load("animation_database.csv")
    chanel_infos = RawDataLoader.get_titles_info_from_folder("./raw", database)
    print(f"Всего каналов: {len(chanel_infos)}")
    stats = count_statistics(chanel_infos)
    for stat_unit in sort_animation_info_by_rating(stats):
        print(f"{stat_unit.final_place}. {stat_unit.title} {stat_unit.total_rating}/{stat_unit.total_votes}")
        # print(f"Распределение мест: {stat_unit.places_dict}")
        # print(f"Среднее место: {round(stat_unit.average_vote_place, 3)}")


if __name__ == "__main__":
    main()
