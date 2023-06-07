""" Get the JSON from YouTube
    https://www.pinecone.io/learn/youtube-search/
"""
import lxml
from bs4 import BeautifulSoup
import os
import json
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from typing import List

parent_dir = "/home/rag/Documents/python/satChad"
directory = "data/"
path = os.path.join(parent_dir, directory)

video_list = ["wA_fI-wUqnw", "Onzd5QxKaGQ"]


def dl_trans(video_id):
    """
    Get the raw transcript

    :param video_id: Unique id of YT video
    :type video_id: string
    """
    transcr = YouTubeTranscriptApi.get_transcript(video_id)
    os.mkdir(path + video_id)
    os.chdir(video_id)
    json_obj = json.dumps(transcr)
    with open("subtitles.txt", "w") as f:
        f.write(json_obj)
    os.chdir(path)


def get_meta(video_ids: List) -> List:
    """
    Fetch the thumbnails

    :param video_ids: The YT video ids
    :type video_ids: List
    """
    metadata = {}
    for _id in video_ids:
        r = requests.get(f"https://www.youtube.com/watch?v={_id}")
        soup = BeautifulSoup(r.content, "lxml")
        try:
            title = soup.find("meta", property="og:title").get("content")
            thumbnail = soup.find("meta", property="og:image").get("content")
            metadata[_id] = {"title": title, "thumbnail": thumbnail}
        except Exception as e:
            print(e)
            print(_id)
            metadata[_id] = {"title": "", "thumbnail": ""}

    return metadata


def parse_subtitles(video_list=video_list):
    """
    Parse the raw transcript to build chunks of text plus
    metadata

    :param video_list: All of the video ids
    :type video_list: List
    """
    os.chdir(path)
    splits = sorted(os.listdir(path))

    # get thumbnails url
    metadata = get_meta(video_ids=video_list)

    # iterate over each video using its folder name (video_id)
    for i, s in enumerate(splits):
        # read the contents of the raw file
        with open(path + f"{s}/subtitles.txt") as src:
            out = json.load(src)

            # create the chunk of 360 chars
            start_timestamp = "00:00:00"
            documents = []
            passage = " "
            for dct in out:
                tx = dct["text"] + " "
                print(passage)
                passage += "".join(tx)
                if len(passage) > 360:
                    # extract timestamp
                    start_second = dct["start"]
                    end_second = start_second + 30

                    documents.append(
                        {
                            "video_id": s,
                            "text": passage,
                            "start_second": start_second,
                            "end_second": end_second,
                            "url": f"https://www.youtube.com/watch?v={s}&t={start_second}s",
                            "title": metadata[s]['title'],
                            "thumbnail" : metadata[s]['thumbnail'],
                        }
                    )

                    # reset passage
                    passage = " "

            # write parsed file with meta
            with open(path + f"{s}/parsed_subtitles.txt", "w") as dest:
                json.dump(documents, dest)


if __name__ == "__main__":
    # Download and store raw Transcript in folder named as video_id
    # for i in video_list:
    # dl_trans(i)

    #Parse transcript into 360 words max
    parse_subtitles(video_list)

    # # get meta
    # print(get_meta(video_ids=video_list))