init python:
    from character_data import CharacterController, CharacterState, Sprite, NarratorNvl

default custom_text_color = "#ffffff"
define character_store = { }

default nvl_narrator = NarratorNvl()
default nvl_text = "empty text"

define narrator = nvl_narrator # For lines without a specific speaker
define gui.nvl_text_xpos = 675

label nvl_text_label:
    "[nvl_text]"
    return

# ======================================== ТУТ ПРОПИСЫВАЕМ ПЕРСОНАЖЕЙ ========================================

define ch_alice = (CharacterController("alice", "Алиса", "#f4a")   
    .add_state("blush", CharacterState([Sprite("alice blush", zoom=(0.6, 0.6))]))
    .add_state("doubt", CharacterState([Sprite("alice doubt", zoom=(0.6, 0.6))]))
    .add_state("embarrassed", CharacterState([Sprite("alice embarrassed", zoom=(0.6, 0.6))]))
    .add_state("happy", CharacterState([Sprite("alice happy", zoom=(0.6, 0.6))]))
    .add_state("idle", CharacterState([Sprite("alice idle", zoom=(0.6, 0.6))]))
    .add_state("teasing", CharacterState([Sprite("alice teasing", zoom=(0.6, 0.6))]))
    .add_state("worried", CharacterState([Sprite("alice worried", zoom=(0.6, 0.6))]))
    .set_position(500, 175)
)

define ch_narrator = CharacterController("narrator", None)
define ch_oth = CharacterController("voice", "", "#f60")
define ch_death = CharacterController("death", "Смерть", "#fff")
define ch_god = CharacterController("god", "Бог", "#fff000")

define ch_p = CharacterController("plague", "Чума", "#b3bf4a")

define ch_w = CharacterController("war", "Война", "#b33536")

define ch_h_sprite_scale = (0.25, 0.25)
define ch_h = (CharacterController("hunger", "Голод", "#88a6b9")
    .add_state("normal", CharacterState([Sprite("hunger normal", zoom=ch_h_sprite_scale)]))
    .add_state("normal shy", CharacterState([Sprite("hunger normal shy", zoom=ch_h_sprite_scale)]))
    .add_state("angry", CharacterState([Sprite("hunger angry", zoom=ch_h_sprite_scale)]))
    .add_state("disappointed", CharacterState([Sprite("hunger disappointed", zoom=ch_h_sprite_scale)]))
    .add_state("fear", CharacterState([Sprite("hunger fear", zoom=ch_h_sprite_scale)]))
    .add_state("fear shy", CharacterState([Sprite("hunger fear shy", zoom=ch_h_sprite_scale)]))
    .add_state("laughing", CharacterState([Sprite("hunger laughing", zoom=ch_h_sprite_scale)]))
    .add_state("laughing nervous", CharacterState([Sprite("hunger laughing nervous", zoom=ch_h_sprite_scale)]))
    .add_state("laughing nervous shy", CharacterState([Sprite("hunger laughing nervous shy", zoom=ch_h_sprite_scale)]))
    .set_position(400, 85)
)

# ======================================== ТУТ ПРОПИСЫВАЕМ ПЕРСОНАЖЕЙ ========================================