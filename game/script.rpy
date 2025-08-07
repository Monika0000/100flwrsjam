init python:
    from character_data import CharacterController, CharacterState, Sprite
    import time 
    import renpy.text.textsupport as ts

    renpy.music.register_channel("typewriter", mixer="sfx", loop=False, tight=True)
    
    def play_voice_sound(what):
        global last_sound_time 
        interval = max(1.0 / preferences.text_cps, 0.05)
        if time.time() - last_sound_time < interval:
            return

        renpy.play("sfx/single_type.wav", channel="typewriter")
        last_sound_time = time.time()

default last_sound_time = 0.0
default custom_text_color = "#f4a"
default character_store = { }
default alice = CharacterController("alice", "Алиса", "#f4a")

screen say(who, what):
    window:
        id "window"
        style "say_window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                padding (5, 5, 10, 15)
                text who id "who" color custom_text_color bold False size 45 

        text what id "what" size 35 layout "subtitle" xmaximum 1200 xpos 400 slow_cps preferences.text_cps

        if renpy.get_displayable(screen="say",id="what").slow_done:
            timer 0.01 repeat True action Function(play_voice_sound, what)

label init_characters:
    $ alice.add_state("blush", CharacterState([Sprite("alice blush", zoom=(0.6, 0.6))]))
    $ alice.add_state("doubt", CharacterState([Sprite("alice doubt", zoom=(0.6, 0.6))]))
    $ alice.add_state("embarrassed", CharacterState([Sprite("alice embarrassed", zoom=(0.6, 0.6))]))
    $ alice.add_state("happy", CharacterState([Sprite("alice happy", zoom=(0.6, 0.6))]))
    $ alice.add_state("idle", CharacterState([Sprite("alice idle", zoom=(0.6, 0.6))]))
    $ alice.add_state("teasing", CharacterState([Sprite("alice teasing", zoom=(0.6, 0.6))]))
    $ alice.add_state("worried", CharacterState([Sprite("alice worried", zoom=(0.6, 0.6))]))
    $ alice.set_position(500, 175)
    return

label say_custom(text, who):
    $ last_sound_time = 0.0
    show screen say(who, text)
    $ renpy.pause()
    hide screen say
    return

define e = Character(display_name="Элис", color="#c8ffc8", tag="elce")

label start:
    call init_characters

    scene bg city

    # !!!!! ИИ генерированный диалог !!!!!

    $ alice.set_state("idle")
    $ alice.say("Привет!{w=0.2} Я Алиса,{w=0.2} твой гид по Ren'Py.")

    $ alice.set_animation("single_bounce_animation")
    $ alice.set_flipped(True)
    $ alice.set_state("happy")
    $ alice.say("Давай {color=#f4a}начнем наше{w=0.25}.{w=0.25}.{w=0.25}.{w=0.25} путешествие!{/color}")

    $ alice.set_state("teasing")
    $ alice.say("Ты готов к приключениям?")

    $ alice.set_state("worried")
    $ alice.say("Не переживай,{w=0.2} {color=#f22}всё{/color} будет хорошо!")

    $ alice.set_flipped(False)
    $ alice.set_state("idle")
    $ alice.say("Если {b}{w=0.15}ч{w=0.15}т{w=0.15}о{w=0.15}{w=0.15}-{w=0.15}т{w=0.15}о{w=0.15}{/b} пойдет не так,{w=0.2} {cps=20}просто перезагрузи игру.")

    $ alice.set_state("blush")
    $ alice.say("А теперь давай посмотрим,{w=0.2} что мы можем сделать с Ren'Py.")

    $ alice.set_state("doubt")
    $ alice.say("Ты можешь создавать свои собственные истории и делиться ими с миром.")
    $ alice.say("А можешь даже добавить немного магии с помощью скриптов!")

    $ alice.set_state("embarrassed")
    $ alice.say("Не бойся экспериментировать и пробовать что-то новое!")

    $ alice.set_flipped(True)
    $ alice.set_animation("single_bounce_animation")
    $ alice.set_state("happy")
    $ alice.say("Надеюсь, тебе понравится создавать игры с Ren'Py!")

    $ alice.set_state("teasing")
    $ alice.say("Надеюсь, ты получил удовольствие от нашего путешествия.")

    $ alice.set_state("happy")
    $ alice.say("До новых встреч!")
    
    $ alice.hide()

    return
