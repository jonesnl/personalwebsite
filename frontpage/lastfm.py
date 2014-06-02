import urllib.request
from xml.etree import ElementTree


class Track:
    name = ""
    artist = ""


def pull_from_lastfm(num_tracks):
    tracklist = list()

    response = \
        urllib.request.urlopen('http://ws.audioscrobbler.com/2.0/'
                               '?method=user.getrecenttracks&'
                               'user=mulligan7nbj&'
                               'api_key=796f29462447bc00fad151f0617ddf9b')
    xml_data = response.read()

    root = ElementTree.fromstring(xml_data)
    xml_recent_tracks = root[0]
    for xml_track in xml_recent_tracks:
        x = Track()
        x.name = xml_track.findtext('name')
        x.artist = xml_track.findtext('artist')
        tracklist.append(x)

    return tracklist[:num_tracks]


def pull():
    print("why")