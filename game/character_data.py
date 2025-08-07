import renpy
import renpy.store as store
import math 

from dataclasses import dataclass

def single_bounce_animation(trans, st, at):
    duration = 0.2 
    amplitude = 20
    frequency = math.pi / duration

    if st > duration:
        trans.yoffset = 0
        return None

    offset = -math.fabs(math.sin(st * frequency)) * amplitude
    trans.yoffset = offset

    return 1 / 60.0

@dataclass
class CharacterStore:
    zoom: tuple[float, float] = (1.0, 1.0)  # масштаб спрайта
    position: tuple[int, int] = (0, 0)  # позиция спрайта
    flipped: tuple[bool, bool] = (False, False)  # зеркалирование по осям (x, y)
    state: str | None = None  # текущее состояние персонажа
    animation: str | None = None  # имя анимации, если есть
    reset_animation: bool = False # сброс анимации после показа состояния

    def copy(self):
        return CharacterStore(zoom=self.zoom, position=self.position, flipped=self.flipped, state=self.state, animation=self.animation, reset_animation=self.reset_animation)


class Sprite:
    def __init__(self, name: str, zoom=(1.0, 1.0), position=(0, 0), flipped=(False, False)):
        self.name = name         # имя спрайта
        self.zoom = zoom         # масштаб спрайта
        self.position = position # позиция спрайта
        self.flipped = flipped   # зеркалирование по осям (x, y)
        self.layer = None        # слой, на котором будет отображаться спрайт (если нужно)
        self.z_index = 0         # индекс по оси Z (глубина)

    def set_position(self, x, y):
        self.position = (x, y)
    
    def set_zoom(self, zoom_x, zoom_y):
        self.zoom = (zoom_x, zoom_y)

    def set_flipped(self, flipped_x=False, flipped_y=False):
        self.flipped = (flipped_x, flipped_y)


class CharacterState:
    def __init__(self, sprites: list[Sprite]):
        self.sprites: list[Sprite] = sprites


class CharacterController:
    def __init__(self, tag: str, display_name: str, color: str = "#ffffff"):
        self.tag: str = tag  # уникальный тег персонажа (для show/hide)
        self.display_name: str = display_name
        self.character = renpy.character.Character(display_name, color=color)#, what_callback=typewriter_sound_callback) # , callback=typewriter_sound_callback , voice="audio/sfx/single_type.wav" what=custom_type_writer
        self.states: dict[str, CharacterState] = {}  # имя состояния → [спрайты]

        if tag not in store.character_store:
            store.character_store[tag] = CharacterStore()

    def add_state(self, name: str, state: CharacterState):
        self.states[name] = state

    def set_zoom(self, zoom_x, zoom_y):
        ch = store.character_store[self.tag].copy()
        ch.zoom = (zoom_x, zoom_y)
        store.character_store[self.tag] = ch

    def set_flipped(self, flipped_x=False, flipped_y=False):
        ch = store.character_store[self.tag].copy()
        ch.flipped = (flipped_x, flipped_y)
        store.character_store[self.tag] = ch

    def set_position(self, x, y):
        ch = store.character_store[self.tag].copy()
        ch.position = (x, y)
        store.character_store[self.tag] = ch

    def set_animation(self, animation_name, reset=True):
        ch = store.character_store[self.tag].copy()
        ch.animation = animation_name
        ch.reset_animation = reset
        store.character_store[self.tag] = ch

    def set_state(self, name):
        """Показать персонажа с нужным состоянием"""
        
        if name not in self.states:
            raise Exception(f"State '{name}' not found for character '{self.tag}'!")

        ch_store = store.character_store[self.tag].copy()
        ch_store.state = name
        store.character_store[self.tag] = ch_store

        for sprite in self.states[name].sprites:
            # Комбинируем зеркалирование и скейл
            parent_xzoom = -ch_store.zoom[0] if ch_store.flipped[0] else ch_store.zoom[0]
            parent_yzoom = -ch_store.zoom[1] if ch_store.flipped[1] else ch_store.zoom[1]

            child_xzoom = -sprite.zoom[0] if sprite.flipped[0] else sprite.zoom[0]
            child_yzoom = -sprite.zoom[1] if sprite.flipped[1] else sprite.zoom[1]
        
            final_xzoom = parent_xzoom * child_xzoom
            final_yzoom = parent_yzoom * child_yzoom
        
            # Итоговая позиция с учётом скейла персонажа
            final_x = ch_store.position[0] # TODO: + (sprite.position[0] * abs(parent_xzoom))
            final_y = ch_store.position[1] # TODO: + (sprite.position[1] * abs(parent_yzoom))

            transform = renpy.store.Transform(
                function=globals()[ch_store.animation] if ch_store.animation != None else None,
                #function=globals()['single_bounce_animation'],
                xzoom=final_xzoom,
                yzoom=final_yzoom,
                xpos=final_x,
                ypos=final_y
            )
            renpy.exports.show(sprite.name, at_list=[transform], tag=self.tag, layer=sprite.layer, zorder=sprite.z_index)

        if ch_store.reset_animation:
            ch_store = ch_store.copy()
            ch_store.animation = None
            store.character_store[self.tag] = ch_store

    def hide(self):
        renpy.exports.hide(self.tag)

    def say(self, text):
        self.character(text)
        