init python:
    from character_data import CharacterController, CharacterState, Sprite, NarratorNvl

default custom_text_color = "#ffffff"
default character_store = { }

default nvl_narrator = NarratorNvl()
default nvl_text = "empty text"

define narrator = nvl_narrator # For lines without a specific speaker
define gui.nvl_text_xpos = 675

label nvl_text_label:
    "[nvl_text]"
    return

# ======================================== ТУТ ПРОПИСЫВАЕМ ПЕРСОНАЖЕЙ ========================================

default ch_alice = (CharacterController("alice", "Алиса", "#f4a")   
    .add_state("blush", CharacterState([Sprite("alice blush", zoom=(0.6, 0.6))]))
    .add_state("doubt", CharacterState([Sprite("alice doubt", zoom=(0.6, 0.6))]))
    .add_state("embarrassed", CharacterState([Sprite("alice embarrassed", zoom=(0.6, 0.6))]))
    .add_state("happy", CharacterState([Sprite("alice happy", zoom=(0.6, 0.6))]))
    .add_state("idle", CharacterState([Sprite("alice idle", zoom=(0.6, 0.6))]))
    .add_state("teasing", CharacterState([Sprite("alice teasing", zoom=(0.6, 0.6))]))
    .add_state("worried", CharacterState([Sprite("alice worried", zoom=(0.6, 0.6))]))
    .set_position(500, 175)
)

default ch_narrator = CharacterController("narrator", None)
default ch_oth = CharacterController("voice", "Серафим", "#f60")
default ch_death = CharacterController("death", "Смерть", "#fff")
default ch_god = CharacterController("god", "Бог", "#fff000")

default ch_p = CharacterController("plague", "Чума", "#b3bf4a")

default ch_w = CharacterController("war", "Война", "#b33536")

default ch_h = CharacterController("hunger", "Голод", "#88a6b9")

# ======================================== ТУТ ПРОПИСЫВАЕМ ПЕРСОНАЖЕЙ ========================================