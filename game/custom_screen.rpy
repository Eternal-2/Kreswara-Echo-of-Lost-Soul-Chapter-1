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
            # Kedip merah saat kritis
            blink = int(st * 4) % 2
            col = "#ff2222" if blink else "#ff8888"
        elif ratio <= 0.5:
            col = "#ffaa00"
        else:
            col = "#88ffcc"
        return Text("%.0f" % remaining, color=col, size=58, bold=True,
                    outlines=[(3, "#000000aa", 0, 0)]), 0.05


screen timer_screen(length=50.0):
    zorder 200
    modal False

    # Jalankan jump waktu habis
    timer length action Jump("waktu_habis_boss")

    # Container tengah atas
    frame:
        xalign 0.5
        yalign 0.0
        yoffset 18
        xsize 680
        ysize 90
        background Frame("#0a0a0aee", 10, 10)
        left_padding 20
        right_padding 20
        top_padding 10
        bottom_padding 10

        vbox:
            xfill True
            spacing 6

            # Baris atas: label + angka
            hbox:
                xfill True
                yalign 0.5

                # Label TIMER
                hbox:
                    spacing 8
                    yalign 0.5
                    text "⏱":
                        size 22
                        yalign 0.5
                    text "WAKTU TERSISA":
                        size 14
                        color "#c8a96e"
                        kerning 2.0
                        yalign 0.5

                # Angka countdown (kanan)
                add DynamicDisplayable(countdown_text_color, length=length):
                    xalign 1.0
                    yalign 0.5

            # Bar countdown
            frame:
                xfill True
                ysize 18
                background Frame("#1a1a2aee", 4, 4)
                left_padding 0
                right_padding 0
                top_padding 0
                bottom_padding 0

                add DynamicDisplayable(countdown_bar, length=length):
                    xalign 0.0
                    yalign 0.5

screen radar_roh_screen(level=0):
    $ img_radar = "images/ASSET/RADAR ROH/radar roh #%s.png" % level
    add img_radar at efek_kedip_radar
        
    timer 2.0 action Hide("radar_roh_screen")

screen state_roh_screen(state="tenang"):
    $ img_state = "images/ASSET/STATE ROH/%s.png" % state
    add img_state at efek_kedip_state
        
    timer 2.0 action Hide("state_roh_screen")

screen panel_coding(border="border1", show_error=False):
    if show_error:
        add "images/ASSET/PANEL CODING/border_error.png" xalign 0.5 yalign 0.5 zoom 0.6
    else:
        add "images/ASSET/PANEL CODING/[border].png" xalign 0.5 yalign 0.5 zoom 0.6
    imagebutton:
        idle "images/ASSET/PANEL CODING/button_run.png"
        hover "images/ASSET/PANEL CODING/button_run.png"
        at transform:
            zoom 0.35
            xalign 0.72 
            yalign 0.78
        action Return(True)

screen feedback_screen(result="berhasil"):
    add "images/ASSET/FEEDBACK VISUAL/[result].png" xalign 0.5 yalign 0.5 zoom 0.55
    timer 1.5 action Hide("feedback_screen")

transform kalah_fadein:
    alpha 0.0 yoffset 40
    linear 0.6 alpha 1.0 yoffset 0

transform kalah_title_in:
    alpha 0.0 yoffset -20
    linear 0.5 alpha 1.0 yoffset 0

screen kalah_boss_screen():
    add "images/BG/desa digital + anomali .png" zoom 1.0 at kalah_fadein

    vbox:
        xalign 0.5 yalign 0.45 spacing 50
        at kalah_title_in

        text "Kamu Kalah..." size 52 color "#ff4444" xalign 0.5

        hbox:
            xalign 0.5 spacing 60
            imagebutton:
                idle  "images/ASSET/KALAH BOSS MENU/button_restart.png"
                hover "images/ASSET/KALAH BOSS MENU/button_restart.png"
                at transform:
                    zoom 0.5
                action Return("restart")
            imagebutton:
                idle  "images/ASSET/KALAH BOSS MENU/button_kembali ke menu.png"
                hover "images/ASSET/KALAH BOSS MENU/button_kembali ke menu.png"
                at transform:
                    zoom 0.5
                action Return("menu")

screen soal_panel(nomor="1", tema="", kode="", pertanyaan=""):
    add "#000000aa"

    frame:
        xalign 0.5
        yalign 0.3
        xsize 820
        xpadding 36
        ypadding 30
        background Frame("#111318ee", 12, 12)

        vbox:
            spacing 20
            xfill True

            vbox:
                spacing 6
                xfill True

                hbox:
                    spacing 10
                    xfill True
                    text "⚔ SERANGAN DATA":
                        size 12
                        color "#c8a96e"
                        kerning 3.0
                        yalign 0.5
                    text "#[nomor]":
                        size 12
                        color "#c8a96e"
                        bold True
                        yalign 0.5

                text "[tema]":
                    size 22
                    color "#f5ead8"
                    bold True

                frame:
                    background "#c8a96e55"
                    xfill True
                    ysize 1

            if kode != "":
                frame:
                    background "#0d1117"
                    xfill True
                    xpadding 18
                    ypadding 14
                    left_margin 0
                    text "[kode]":
                        size 18
                        color "#79c0ff"
                        font "gui/font/SourceCodePro-Regular.ttf"
                        line_spacing 8

            text "[pertanyaan]":
                size 19
                color "#e0e0e0"
                xalign 0.5
                text_align 0.5
                line_spacing 4


screen dialog_choice_hint(mode="cari"):
    if mode == "cari":
        add "images/ASSET/DIALOG CHOICE/cari informasi.png" xalign 0.85 yalign 0.85 zoom 0.28
    else:
        add "images/ASSET/DIALOG CHOICE/serap roh.png"      xalign 0.85 yalign 0.85 zoom 0.28
