import time, pyttsx3, keyboard, pygame
from plyer import notification

def music_player():
    pygame.init()
    pygame.mixer.init()

    alarm_music = pygame.mixer.Sound("music/alarm.mp3")
    alarm_music.set_volume(1)

    while not keyboard.is_pressed("space"):
        alarm_music.play()

    alarm_music.stop()

def set_alarm(alarm_time):
    engine = pyttsx3.init()

    notification.notify(
        title="Alarm Set",
        message=f"Alarm set to {alarm_time}",
        app_name="Tracy alarm system",
        timeout=10
    )

    while True:
        current_time = time.strftime("%H:%M:%S")

        if current_time == alarm_time:
            notification.notify(
                title="Alarm Ringing...",
                message=f"The current time is {current_time}, time to wake up I guess.",
                app_name="Tracy alarm system",
                timeout=10
            )

            music_player()

            engine.say("Wake up")
            engine.runAndWait()
            break

