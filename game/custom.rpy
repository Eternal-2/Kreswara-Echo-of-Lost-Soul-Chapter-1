init python:
    def countdown(st, at, length=50.0):
        remaining = max(0.0, length - st)
        return Text("%.1f" % remaining, color="#ff4444", size=40, bold=True), 0.05

    def countdown_bar(st, at, length=50.0):
        remaining = max(0.0, length - st)
        ratio = remaining / length  # 1.0 = penuh, 0.0 = habis

        # Warna bar berubah: hijau → kuning → merah
        if ratio > 0.5:
            r = int(255 * (1.0 - ratio) * 2)
            g = 220
        else:
            r = 220
            g = int(220 * ratio * 2)
        color = "#{:02x}{:02x}00".format(min(r, 220), min(g, 220))

        bar_width = int(600 * ratio)
        bar_width = max(0, bar_width)

        return Fixed(
            Solid(color, xsize=bar_width, ysize=18),
            xsize=600, ysize=18
        ), 0.05

    def countdown_text_color(st, at, length=50.0):
        remaining = max(0.0, length - st)
        ratio = remaining / length
        if ratio <= 0.25:
            blink = int(st * 4) % 2
            col = "#ff2222" if blink else "#ff8888"
        elif ratio <= 0.5:
            col = "#ffaa00"
        else:
            col = "#88ffcc"
        return Text("%.0f" % remaining, color=col, size=58, bold=True,
                    outlines=[(3, "#000000aa", 0, 0)]), 0.05


default quiz_score    = 0
default quiz_total    = 7
default boss_hp       = 3
default boss_attempts = 0
default fase1_benar   = 0
default fase2_benar   = 0
default fase3_benar   = 0