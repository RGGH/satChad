""" Get the JSON from YouTube
    https://www.pinecone.io/learn/youtube-search/
    
    A list of 3 video ids will produce:                                                        ─╯
    .
    ├── mC43pZkpTec
    │   ├── parsed_subtitles.txt
    │   └── subtitles.txt
    ├── Onzd5QxKaGQ
    │   ├── parsed_subtitles.txt
    │   └── subtitles.txt
    └── wA_fI-wUqnw
        ├── parsed_subtitles.txt
        └── subtitles.txt
    
"""
import lxml
from bs4 import BeautifulSoup
import os
import json
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from typing import List

parent_dir = "/home/admin/satChad"
directory = "data/"
path = os.path.join(parent_dir, directory)

#video_list = ["wA_fI-wUqnw", "Onzd5QxKaGQ","mC43pZkpTec","qEU0goAeNPk","v4na2pycrcc","x4-e5wq5AJ8"]

# use pre-prepared text file of video ids
with open("saylor-vids.txt") as f:
    video_list = f.read().splitlines()

def dl_trans(video_id):
    """
    Get the raw transcript

    :param video_id: Unique id of YT video
    :type video_id: string
    """
    transcr = YouTubeTranscriptApi.get_transcript(video_id)
    print(f"fetch :",video_id)
    os.mkdir(path + video_id)
    os.chdir(path + video_id)
    json_obj = json.dumps(transcr)
    with open("subtitles.txt", "w") as f:
        f.write(json_obj)
    os.chdir(path)


def get_meta(video_ids: List) -> List:
    print("get meta")
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
    print("parse subtitles")
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
    print(f"processing raw subtitles {metadata}")
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
                    start_second = int(round(start_second,0))
                    if start_second > 4:
                        start_second -= 3
                    
                    end_second = start_second + 30
                    end_second = int(round(end_second,0))
                    

                    documents.append(
                        {
                            "video_id": s,
                            "text": passage,
                            "start_second": start_second,
                            "end_second": end_second,
                            "url": f"https://www.youtube.com/watch?v={s}?feature=share&t={start_second}",
                            "title": metadata[s]['title'],
                            "thumbnail" : metadata[s]['thumbnail'],
                        }
                    )

                    # reset passage
                    passage = ""

            # write parsed file with meta
            with open(path + f"{s}/parsed_subtitles.txt", "w") as f:
                for doc in documents:
                    json.dump(doc, f)
                    f.write('\n')


if __name__ == "__main__":
    
    #Download and store raw Transcript in folder named as video_id
    for i in video_list:
        try:
            dl_trans(i)
        except:
            pass
        
    #Parse transcript into 360 words max
    parse_subtitles(video_list)
    
    print("Done")
