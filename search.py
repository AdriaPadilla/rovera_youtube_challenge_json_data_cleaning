import pandas as pd
import json

def search_parse_json(file):
    with open(file, encoding='utf8') as f:
        content = json.load(f)
        data = content["items"]
        videos_list = []
        for video in data:
            video_data = {}
            video_data["kind"] =  video["kind"]
            video_data["query"] = file.split("_")[2]
            video_data["rank_position"] = data.index(video)+1
            video_data["videoId"] = video["id"]["videoId"]
            video_data["published_at"] = video["snippet"]["publishedAt"]
            video_data["title"] = video["snippet"]["title"]
            video_data["description"] = video["snippet"]["description"]
            video_data["channel_title"] = video["snippet"]["channelTitle"]
            video_data["channelId"] = video["snippet"]["channelId"]
            video_data["thumbnail"] = video["snippet"]["thumbnails"]["high"]["url"]
            date = "2020"+str(file.split("2020")[1].split(".")[0].split("-")[0])
            time = str(file.split("2020")[1].split(".")[0].split("-")[1])
            video_data["query_date"] = date
            video_data["query_time"] = time
            videos_list.append(video_data)
        return videos_list

def search_to_frame(list):

    df_list = []

    for search in list:
        for video in search:

            df = pd.DataFrame({
                "kind": video["kind"],
                "query": video["query"],
                "position": video["rank_position"],
                "published_at": video["published_at"],
                "title": video["title"],
                "description": video["description"],
                "channel_title": video["channel_title"],
                "channelId": video["channelId"],
                "thumbnail": video["thumbnail"],
                "search_query_date": video["query_date"],
                "search_query_time": video["query_time"],
                "id_flag": video["videoId"],
            }, index=[0])
            df_list.append(df)
    final_search_df = pd.concat(df_list, ignore_index=True)
    # final_search_df.to_excel("search_frame.xlsx")
    return final_search_df

def grab_search(search_json_files):
    search_global_list = []
    for file in search_json_files:
        videos = search_parse_json(file)
        search_global_list.append(videos)
    final_search_df = search_to_frame(search_global_list)
    return final_search_df

