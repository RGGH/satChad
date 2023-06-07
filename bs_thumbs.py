import lxml  # if on mac, pip/conda install lxml

metadata = {}
for _id in (video_ids):
    r = requests.get(f"https://www.youtube.com/watch?v={_id}")
    soup = BeautifulSoup(r.content, "lxml")  # lxml package is used here
    try:
        title = soup.find("meta", property="og:title").get("content")
        thumbnail = soup.find("meta", property="og:image").get("content")
        metadata[_id] = {"title": title, "thumbnail": thumbnail}
    except Exception as e:
        print(e)
        print(_id)
        metadata[_id] = {"title": "", "thumbnail": ""}

print(metadata)
