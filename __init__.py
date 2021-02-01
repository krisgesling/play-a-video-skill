import pafy
from tempfile import gettempdir
from mycroft import MycroftSkill, intent_handler


class PlayAVideo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler("video.a.play.intent")
    def handle_yt_video_a_play(self, message):
        self.speak_dialog("video.a.play")
        url = self.get_video_stream()
        self.log.info(url)
        self.gui.play_video(url, "Youtube video")

    @intent_handler("video.test.play.intent")
    def handle_video_a_play(self, message):
        self.speak_dialog("video.a.play")
        url = "/home/mycroft/test.mp4"
        self.log.info(url)
        self.gui.play_video(url, "Test video")
        

    @staticmethod
    def get_video_stream(url="https://www.youtube.com/watch?v=Gv1I0y6PHfg",
                         download=False):
        stream = pafy.new(url).streams[0]
        if download:
            path = join(gettempdir(),
                        url.split("watch?v=")[-1] + "." + stream.extension)
            if not exists(path):
                stream.download(path)
            return path
        return stream.url

def create_skill():
    return PlayAVideo()
