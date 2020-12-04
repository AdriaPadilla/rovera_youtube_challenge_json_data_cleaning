import pandas as pd
import json


def video_parse_json(file):
    with open(file, encoding='utf8') as f:
        content = json.load(f)
        data = content["items"][0]
        video_info = {}
        video_info["id"] = data["id"]
        video_info["query_date"] = "2020" + str(file.split("2020")[1].split(".")[0].split("-")[0])
        video_info["query_time"] = str(file.split("2020")[1].split(".")[0].split("-")[1])
        video_info["duration"] = data["contentDetails"]["duration"]
        video_info["is_liscensed"] = data["contentDetails"]["licensedContent"]
        video_info["views_n"] = data["statistics"]["viewCount"]
        video_info["categoryId"] = data["snippet"]["categoryId"]
        try:
            video_info["dislikes_n"] = data["statistics"]["dislikeCount"]
        except KeyError:
            video_info["dislikes_n"] = "null"
        try:
            video_info["likes_m"] = data["statistics"]["likeCount"]
        except KeyError:
            video_info["likes_m"] = "null"
        try:
            video_info["commentCount"] = data["statistics"]["commentCount"]
        except KeyError:
            video_info["commentCount"] = "null"
        try:
            video_info["lang"] = data["snippet"]["defaultAudioLanguage"]
        except KeyError:
            video_info["lang"] = "null"
        try:
            video_info["tags"] = [data["snippet"]["tags"]]
        except KeyError:
            video_info["tags"] = "null"
        return video_info


def videos_to_frame(videos_global_list):
    df_list = []

    for video in videos_global_list:
        df = pd.DataFrame({
            "id_flag": video["id"],
            "video_query_date": video["query_date"],
            "video_query_time": video["query_time"],
            "duration": video["duration"],
            "liscensed": video["is_liscensed"],
            "views": video["views_n"],
            "category": video["categoryId"],
            "dislikes": video["dislikes_n"],
            "likes": video["likes_m"],
            "comment": video["commentCount"],
            "lang": video["lang"],
            "tags": video["tags"],
        }, index=[0])
        df_list.append(df)
    final_videos_df = pd.concat(df_list, ignore_index=True)
    # final_videos_df.to_excel("videos_frame.xlsx")
    return final_videos_df


def grab_video_info(video_json_files):
    videos_global_list = []
    for file in video_json_files:
        videos = video_parse_json(file)
        videos_global_list.append(videos)
    final_videos_df = videos_to_frame(videos_global_list)
    return final_videos_df