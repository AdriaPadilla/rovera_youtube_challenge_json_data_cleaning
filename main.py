import glob
import videos as v
import search as s
import merge as m

if __name__ == '__main__':

    search_json_files = glob.glob("search/*.json")
    video_json_files = glob.glob("videos/*.json")

    search_df = s.grab_search(search_json_files)
    video_df = v.grab_video_info(video_json_files)
    m.merge_datasets(search_df, video_df)





