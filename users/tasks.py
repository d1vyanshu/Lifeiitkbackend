from background_task import background

@background(schedule=5)
def notify_new_event(tokens, message):
    for token in tokens:
        pass
        #Send notifications using Expo