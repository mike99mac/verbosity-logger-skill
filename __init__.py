from mycroft import MycroftSkill, intent_file_handler


class VerbosityLogger(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('logger.verbosity.intent')
    def handle_logger_verbosity(self, message):
        self.speak_dialog('logger.verbosity')


def create_skill():
    return VerbosityLogger()

