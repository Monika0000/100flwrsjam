import renpy
import renpy.store as store
import math 
import re

from dataclasses import dataclass

from typing import List

def add_auto_waits(text: str, wait: float = 0.1) -> str:
    punct = set('.,;:!?…')
    # унифицируем символ многоточия
    text = text.replace('…', '...')
    n = len(text)
    i = 0
    out: List[str] = []

    while i < n:
        ch = text[i]
        if ch in punct:
            # 1) если мы внутри тега { ... } — не трогаем знак
            last_open = text.rfind('{', 0, i)
            last_close = text.rfind('}', 0, i)
            if last_open != -1 and (last_close == -1 or last_open > last_close):
                out.append(ch)
                i += 1
                continue

            # 2) если это десятичная точка между двумя цифрами — не трогаем
            if ch == '.' and i - 1 >= 0 and i + 1 < n and text[i-1].isdigit() and text[i+1].isdigit():
                out.append(ch)
                i += 1
                continue

            # проверяем, есть ли уже тег {w=...} после знака (пропуская пробелы/теги)
            j = i + 1
            has_wait_tag = False
            while j < n:
                c = text[j]
                if c in ' \t\r\n':
                    j += 1
                    continue
                if c == '{':
                    close = text.find('}', j)
                    if close == -1:
                        break
                    tag_content = text[j+1:close]
                    if tag_content.strip().startswith('w=') or tag_content.strip() == 'w':
                        has_wait_tag = True
                        break
                    j = close + 1
                    continue
                break

            add_pause = False
            if not has_wait_tag:
                prev_is_punct = (i - 1 >= 0 and text[i-1] in punct)
                next_is_punct = (i + 1 < n and text[i+1] in punct)
                # если это часть последовательности знаков (например "...") — вставляем
                if prev_is_punct or next_is_punct:
                    add_pause = True
                else:
                    # иначе — вставляем паузу только если после знака есть "значимый" символ,
                    # а не только пробелы/тэги/конец строки
                    add_pause = (j < n)

            out.append(ch)
            if add_pause:
                out.append(f'{{w={wait}}}')
            i += 1
        else:
            out.append(ch)
            i += 1

    return ''.join(out)


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
        return self

    def set_zoom(self, zoom_x, zoom_y):
        ch = store.character_store[self.tag].copy()
        ch.zoom = (zoom_x, zoom_y)
        store.character_store[self.tag] = ch
        return self

    def set_flipped(self, flipped_x=False, flipped_y=False):
        ch = store.character_store[self.tag].copy()
        ch.flipped = (flipped_x, flipped_y)
        store.character_store[self.tag] = ch
        return self

    def set_position(self, x, y):
        ch = store.character_store[self.tag].copy()
        ch.position = (x, y)
        store.character_store[self.tag] = ch
        return self

    def set_animation(self, animation_name, reset=True):
        ch = store.character_store[self.tag].copy()
        ch.animation = animation_name
        ch.reset_animation = reset
        store.character_store[self.tag] = ch
        return self

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

    def say(self, text, auto_wait=True):
        if auto_wait:
            text = add_auto_waits(text)
        self.character(text)
        