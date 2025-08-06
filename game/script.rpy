init python:
    from character_data import Character, CharacterState, Sprite

default character_store = { }
default alice = Character("alice", "Алиса", "#f4a")

label init_characters:
    $ alice.add_state("blush", CharacterState([Sprite("alice blush", zoom=(0.6, 0.6))]))
    $ alice.add_state("doubt", CharacterState([Sprite("alice doubt", zoom=(0.6, 0.6))]))
    $ alice.add_state("embarrassed", CharacterState([Sprite("alice embarrassed", zoom=(0.6, 0.6))]))
    $ alice.add_state("happy", CharacterState([Sprite("alice happy", zoom=(0.6, 0.6))]))
    $ alice.add_state("idle", CharacterState([Sprite("alice idle", zoom=(0.6, 0.6))]))
    $ alice.add_state("teasing", CharacterState([Sprite("alice teasing", zoom=(0.6, 0.6))]))
    $ alice.add_state("worried", CharacterState([Sprite("alice worried", zoom=(0.6, 0.6))]))
    return


label start:
    call init_characters

    scene bg city

    # !!!!! ИИ генерированный диалог !!!!!

    $ alice.set_position(500, 150)
    $ alice.set_state("idle")
    $ alice.say("Привет! Я Алиса, твой гид по Ren'Py.")

    $ alice.set_flipped(True)
    $ alice.set_state("happy")
    $ alice.say("Давай начнем наше путешествие!")

    $ alice.set_state("teasing")
    $ alice.say("Ты готов к приключениям?") 

    $ alice.set_state("worried")
    $ alice.say("Не переживай, всё будет хорошо!")

    $ alice.set_flipped(False)
    $ alice.set_state("idle")
    $ alice.say("Если что-то пойдет не так, просто перезагрузи игру.")

    $ alice.set_state("blush")
    $ alice.say("А теперь давай посмотрим, что мы можем сделать с Ren'Py.")

    $ alice.set_state("doubt")
    $ alice.say("Ты можешь создавать свои собственные истории и делиться ими с миром.")

    $ alice.set_state("embarrassed")
    $ alice.say("Не бойся экспериментировать и пробовать что-то новое!")

    $ alice.set_flipped(True)
    $ alice.set_state("happy")
    $ alice.say("Надеюсь, тебе понравится создавать игры с Ren'Py!")

    $ alice.set_state("teasing")
    $ alice.say("Надеюсь, ты получил удовольствие от нашего путешествия.")

    $ alice.set_state("happy")
    $ alice.say("До новых встреч!")
    
    $ alice.hide()

    return
