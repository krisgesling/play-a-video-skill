import pafy
from tempfile import gettempdir
from mycroft import MycroftSkill, intent_handler


class PlayAVideo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler("video.a.play.intent")
    def handle_yt_video_a_play(self, message):
        url = self.get_video_stream()
        self.log.info(url)
        self.gui.play_video(url, "Youtube video")

    @intent_handler("video.test.play.intent")
    def handle_video_a_play(self, message):
        url = "/home/mycroft/test.mp4"
        self.log.info(url)
        self.gui.play_video(url, "Test video")

    @staticmethod
    def get_video_stream(url=None):
        if url is None:
            url = "https://www.youtube.com/watch?v=YE7VzlLtp-4"
        stream = pafy.new(url).streams[0]
        return stream.url

def create_skill():
    return PlayAVideo()
