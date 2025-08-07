init python:
    from character_data import CharacterController, CharacterState, Sprite

default custom_text_color = "#ffffff"
default character_store = { }

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
