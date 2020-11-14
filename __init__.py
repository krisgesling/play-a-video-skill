from mycroft import MycroftSkill, intent_file_handler


class PlayAVideo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('video.a.play.intent')
    def handle_video_a_play(self, message):
        self.speak_dialog('video.a.play')


def create_skill():
    return PlayAVideo()

