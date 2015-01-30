import urllib.request
import urllib.error
from xml.etree import ElementTree
from django.conf import settings


class Track:
    name = ""
    artist = ""


def pull_from_lastfm(num_tracks):
    tracklist = list()

    if not settings.LASTFM_API_KEY:
        return list()

    try:
        response = \
            urllib.request.urlopen('http://ws.audioscrobbler.com/2.0/'
                                    '?method=user.getrecenttracks&'
                                    'user=mulligan7nbj&'
                                    'api_key=' + settings.LASTFM_API_KEY,
                                   timeout=2)
    except urllib.error.URLError:
        return tracklist

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