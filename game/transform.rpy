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
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    linear 0.8 alpha 0.0

transform efek_kedip_state:
    xalign 0.5 yalign 0.5 zoom 0.45
    alpha 0.0
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    linear 0.8 alpha 0.0

transform efek_kedap_kedip:
    alpha 0.0           # Mulai dari gelap
    pause 0.1           # Jeda sangat singkat
    alpha 1.0           # Terang (gambar muncul)
    pause 0.1
    alpha 0.0           # Gelap lagi
    pause 0.1
    alpha 1.0           # Terang lagi
    pause 0.2           # Tahan sedikit lebih lama
    alpha 0.0           # Gelap
    pause 0.1
    alpha 1.0           # Terang dan menetap