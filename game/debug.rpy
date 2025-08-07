label debug:
    scene bg city

    $ ch_narrator.say("!ИИ сгенерированный диалог!")

    $ ch_alice.set_state("idle")
    $ ch_alice.say("Привет!{w=0.2} Я Алиса,{w=0.2} твой гид по Ren'Py.")

    $ ch_alice.set_animation("single_bounce_animation")
    $ ch_alice.set_flipped(True)
    $ ch_alice.set_state("happy")
    $ ch_alice.say("Давай {color=#f4a}начнем наше{w=0.25}.{w=0.25}.{w=0.25}.{w=0.25} путешествие!{/color}")

    $ ch_alice.set_state("teasing")
    $ ch_alice.say("Ты готов к приключениям?")

    $ ch_alice.set_state("worried")
    $ ch_alice.say("Не переживай,{w=0.2} {color=#f22}всё{/color} будет хорошо!")

    $ ch_alice.set_flipped(False)
    $ ch_alice.set_state("idle")
    $ ch_alice.say("Если {b}{w=0.15}ч{w=0.15}т{w=0.15}о{w=0.15}{w=0.15}-{w=0.15}т{w=0.15}о{w=0.15}{/b} пойдет не так,{w=0.2} {cps=20}просто перезагрузи игру.")

    $ ch_alice.set_state("blush")
    $ ch_alice.say("А теперь давай посмотрим,{w=0.2} что мы можем сделать с Ren'Py.")

    $ ch_alice.set_animation("single_bounce_animation")
    $ ch_alice.set_state("doubt")
    $ ch_alice.say("Ты можешь создавать свои собственные истории и делиться ими с миром.")
    $ ch_alice.say("А можешь даже добавить немного магии с помощью скриптов!")

    $ ch_alice.set_state("embarrassed")
    $ ch_alice.say("Не бойся экспериментировать и пробовать что-то новое!")

    $ ch_alice.set_flipped(True)
    $ ch_alice.set_animation("single_bounce_animation")
    $ ch_alice.set_state("happy")
    $ ch_alice.say("Надеюсь{w=0.2}, тебе понравится создавать игры с Ren'Py!")

    $ ch_alice.set_state("teasing")
    $ ch_alice.say("Надеюсь,{w=0.2} ты получил удовольствие от нашего путешествия.")

    $ ch_alice.set_state("happy")
    $ ch_alice.say("До новых встреч!")

    $ ch_narrator.say("!ИИ сгенерированный диалог завершен!")

    $ ch_alice.hide()
