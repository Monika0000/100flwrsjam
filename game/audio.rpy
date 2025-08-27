default persistent.pixel_voice_enabled = True
default last_typewriter_sound_time = 0.0

default active_voice_path = "voice/voice.wav"
default active_voice_interval_multiplier = 1.0

init python:
    import time 

    count_channels = 10
    current_channel = 0

    for i in range(count_channels):
        renpy.music.register_channel(f"typewriter{i}", mixer="voice", loop=False, tight=True)

    def play_voice_sound(what):
        if not persistent.pixel_voice_enabled:
            return 

        if preferences.text_cps <= 0:
            return

        global last_typewriter_sound_time, current_channel, count_channels
        
        interval = max(1.0 / preferences.text_cps, 0.075 * active_voice_interval_multiplier) 
        if time.time() - last_typewriter_sound_time < interval:
            return

        ch_name = f"typewriter{current_channel + 1}"
        renpy.play(active_voice_path, channel=ch_name)
        current_channel = (current_channel + 1) % count_channels
        last_typewriter_sound_time = time.time()
