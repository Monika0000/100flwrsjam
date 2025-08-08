default persistent.pixel_voice_enabled = True
default last_typewriter_sound_time = 0.0

init python:
    import time 

    renpy.music.register_channel("typewriter", mixer="voice", loop=False, tight=True)    

    def play_voice_sound(what):
        if not persistent.pixel_voice_enabled:
            return 

        if preferences.text_cps <= 0:
            return

        global last_typewriter_sound_time 
        interval = max(1.0 / preferences.text_cps, 0.075)
        if time.time() - last_typewriter_sound_time < interval:
            return

        renpy.play("sfx/single_type.wav", channel="typewriter")
        last_typewriter_sound_time = time.time()
