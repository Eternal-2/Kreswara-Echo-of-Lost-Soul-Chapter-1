transform lompat_kaget:
    easein 0.1 yoffset -40  # Bergerak cepat ke atas sebanyak 40 pixel
    easeout 0.1 yoffset 0   # Bergerak kembali turun ke posisi awal

transform getar:
    linear 0.05 xoffset -10 # Geser kiri sedikit
    linear 0.05 xoffset 10  # Geser kanan sedikit
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset 0   # Kembali ke tengah

transform napas_berat:
    easein 0.5 yoffset 10   # Turun perlahan (bahu turun)
    easeout 0.5 yoffset 0

transform efek_kedip_radar:
    xalign 0.5 yalign 0.5 zoom 0.5
    alpha 0.0
    linear 0.2 alpha 1.0
    linear 0.2 alpha 0.0
    linear 0.2 alpha 1.0
    linear 0.2 alpha 0.0
    linear 0.2 alpha 1.0
    linear 0.5 alpha 0.0

transform efek_kedip_state:
    xalign 0.5 yalign 0.5 zoom 0.45
    alpha 0.0
    linear 0.2 alpha 1.0
    linear 0.2 alpha 0.0
    linear 0.2 alpha 1.0
    linear 0.2 alpha 0.0
    linear 0.2 alpha 1.0
    linear 0.5 alpha 0.0