import pandas as pd

def merge_datasets(search_df, video_df):
    single = search_df.drop_duplicates(subset=["search_query_date"])
    get_dates = single["search_query_date"]
    dates = get_dates.tolist()
    print(dates)

    list_of_frames = []

    for date in dates:
        search_mask = search_df["search_query_date"].str.contains(date)
        video_mask = video_df["video_query_date"].str.contains(date)
        filtered_search = search_df[search_mask]
        filtered_videos = video_df[video_mask]

        print(filtered_videos)
        merged_df = pd.merge(filtered_search, filtered_videos, on="id_flag")

        list_of_frames.append(merged_df)

    final_frame = pd.concat(list_of_frames, ignore_index=True)
    final_frame.to_excel("merged.xlsx")
