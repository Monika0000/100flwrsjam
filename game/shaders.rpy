define config.gl2 = True  # включаем OpenGL2, нужно для шейдеров

init python:
    def redraw_each_frame(trans, st, at):
        renpy.redraw(trans, 0)  # перерисовывать каждый кадр
        return 0

    def redraw_with_delay(trans, st, at):
        renpy.redraw(trans, 20)
        return 120

    renpy.register_textshader(
        "shake",
        variables="""
            uniform float u__amplitude;       // сила тряски (px)
            uniform float u__speed;           // скорость тряски
            uniform float u_time;             // системное время
            uniform float u_text_to_drawable; // коэффициент для масштабирования
            attribute float a_text_index;     // индекс символа
        """,

        vertex_40="""
            float shake_x = sin(u_time * u__speed + a_text_index * 13.0) * u__amplitude;
            float shake_y = cos(u_time * u__speed + a_text_index * 17.0) * u__amplitude;
            gl_Position.xy += vec2(shake_x, shake_y) * u_text_to_drawable;
        """,

        u__amplitude=2.0,   # по умолчанию сдвиг в пикселях
        u__speed=20.0,      # скорость по умолчанию
        redraw=0.0,

        doc="""
        The shake text shader makes each glyph jitter randomly.

        `u__amplitude`
            Pixel offset range (default 2.0).
        `u__speed`
            Oscillation speed (default 20.0).
        """
    )
    
    renpy.register_shader("blur.shader", variables="""
        varying vec2 v_tex_coord;
        attribute vec2 a_tex_coord;
        uniform float u_lod_bias;
        uniform float u_time;
        //uniform vec4 u_random;
        uniform sampler2D tex0;
    """, vertex_600="""
        v_tex_coord = a_tex_coord;
    """, fragment_600="""
        float max_offset = 0.05;
        vec2 size = vec2(1920, 1080);
        float multiplier = (sin(u_time) * cos(u_time)) / 5.0;
        float x_offset = (sin(v_tex_coord.x * size.x / 4.0) + multiplier) * 0.5 * max_offset;
        float y_offset = (sin(v_tex_coord.y * size.y / 4.0) + multiplier) * 0.5 * max_offset;
        vec2 v_tex_coord_fixed = v_tex_coord.xy + vec2(x_offset, y_offset);
        vec4 original = texture2D(tex0, v_tex_coord_fixed.xy, u_lod_bias);
        gl_FragColor = original;
    """)

    renpy.register_shader("chromatic.shader", variables="""
        varying vec2 v_tex_coord;
        attribute vec2 a_tex_coord;
        uniform float u_lod_bias;
        uniform sampler2D tex0;
    """, vertex_600="""
        v_tex_coord = a_tex_coord;
    """, fragment_600="""
        float offset_strength = 0.005 + (1.0 * 0.0025);
        vec2 offset = vec2(offset_strength, 0.0);

        // Смещаем каждый канал по-разному
        float r = texture2D(tex0, v_tex_coord - offset).r;
        float g = texture2D(tex0, v_tex_coord).g;
        float b = texture2D(tex0, v_tex_coord + offset).b;

        gl_FragColor = vec4(r, g, b, 1.0);
    """)


    renpy.register_shader("glitch.shader", variables="""
        varying vec2 v_tex_coord;
        attribute vec2 a_tex_coord;
        uniform float u_time;
        uniform float u_lod_bias;
        uniform sampler2D tex0;
    """, vertex_600="""
        v_tex_coord = a_tex_coord;
    """, fragment_600="""
        float line_height = 0.03; // высота строки "глитча"
        float glitch_strength = 0.15; // насколько сильно смещать

        // какая "строчка" экрана
        float y_band = floor(v_tex_coord.y / line_height);

        // рандом на основе y_band + времени
        float time_step = 0.25; // шаг времени в секундах
        float quantized_time = floor(u_time / time_step) * time_step;

        float rand = fract(sin(dot(vec2(y_band, quantized_time), vec2(12.9898,78.233))) * 43758.5453);

        // если rand выше порога — сместить
        if (rand > 0.5) {
            float offset = (rand - 0.5) * 2.0 * glitch_strength;
            vec2 glitch_uv = vec2(v_tex_coord.x + offset, v_tex_coord.y);
            gl_FragColor = texture2D(tex0, glitch_uv, u_lod_bias);
        } else {
            gl_FragColor = texture2D(tex0, v_tex_coord, u_lod_bias);
        }
    """)

transform blur_shader:
    shader "blur.shader"
    function redraw_each_frame

transform chromatic_shader:
    shader "chromatic.shader"

transform glitch_shader:
    shader "glitch.shader"
    function redraw_each_frame