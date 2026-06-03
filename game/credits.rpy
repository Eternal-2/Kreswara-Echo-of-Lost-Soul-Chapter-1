## =============================================================================
## CREDITS
## =============================================================================

# 1. ANIMASI SCROLL: Menggeser teks dari bawah layar ke atas
transform credits_scroll_anim(waktu_scroll):
    xalign 0.5
    yanchor 0.0 ypos 1.0                      # Memulai posisi tepat di bawah layar
    linear waktu_scroll yanchor 1.0 ypos 0.0  # Bergerak perlahan hingga melewati batas atas layar

screen credits_screen(ending_type="good"):
    modal True
    zorder 300

    # Latar Belakang
    if ending_type == "good":
        add "images/BG/Ending/credit_scene_good.png" xalign 0.5 yalign 0.5 fit "cover"
        add "#00000099"
    else:
        add "images/BG/Ending/credit_scene_bad.png" xalign 0.5 yalign 0.5 fit "cover"
        add "#000000bb"

    # Tombol SKIP di pojok kanan atas
    frame:
        xalign 0.98
        yalign 0.02
        background "#00000000"
        textbutton "SKIP":
            text_size 16
            text_color "#c8a96eaa"
            text_hover_color "#c8a96e"
            action Return("skip")

    # 2. KOTAK TEKS (VBOX) YANG BERGERAK
    # Angka 45.0 adalah kecepatan (dalam detik). Silakan perbesar angkanya jika terlalu cepat.
    vbox at credits_scroll_anim(50.0):
        spacing 15
        xalign 0.5

        ## Ruang kosong agar konten mulai dari bawah layar
        null height 1080

        ## ── Judul ────────────────────────────────────────────────────────
        null height 60
        text "Kreswara Studio":
            xalign 0.5
            size 54
            color "#c8a96e"
            bold True
            text_align 0.5

        text "Kreswara Echo Of the Lost Souls":
            xalign 0.5
            size 26
            color "#f5ead8cc"
            italic True
            text_align 0.5

        null height 20
        frame:
            xalign 0.5
            xsize 400
            ysize 2
            background "#c8a96e88"
        null height 60

        ## ── Ucapan Terima Kasih ──────────────────────────────────────────
        text "Terima Kasih Telah Bermain":
            xalign 0.5
            size 22
            color "#ddd8cc"
            bold True
            text_align 0.5

        null height 14
        text "Game ini dibuat dengan penuh semangat\noleh tim mahasiswa PSTI Kelas 2A.":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
            line_spacing 8

        null height 60
        frame:
            xalign 0.5
            xsize 600
            ysize 1
            background "#ffffff22"
        null height 60

        ## ── SUPERVISOR ───────────────────────────────────────────────────
        text "SUPERVISOR":
            xalign 0.5
            size 13
            color "#c8a96e"
            kerning 4.0
            bold True
            text_align 0.5
        null height 14
        text "Lili Fidini Rizqi":
            xalign 0.5
            size 20
            color "#f5ead8"
            text_align 0.5
        null height 50

        ## ── KETUA PROJECT ────────────────────────────────────────────────
        text "KETUA PROJECT":
            xalign 0.5
            size 13
            color "#c8a96e"
            kerning 4.0
            bold True
            text_align 0.5
        null height 14
        text "Zamzam Firdaus":
            xalign 0.5
            size 20
            color "#f5ead8"
            text_align 0.5
        null height 50

        ## ── LEADER ───────────────────────────────────────────────────────
        text "LEADER":
            xalign 0.5
            size 13
            color "#c8a96e"
            kerning 4.0
            bold True
            text_align 0.5
        null height 14
        text "Sultan Maulana Akbar":
            xalign 0.5
            size 20
            color "#f5ead8"
            text_align 0.5

        null height 70
        frame:
            xalign 0.5
            xsize 600
            ysize 1
            background "#ffffff22"
        null height 60

        ## ── ADMINISTRASI & DOKUMENTASI ───────────────────────────────────
        text "ADMINISTRASI & DOKUMENTASI":
            xalign 0.5
            size 13
            color "#c8a96e"
            kerning 4.0
            bold True
            text_align 0.5
        null height 10
        text "Qeisya Dwi Hermawan  —  Ketua":
            xalign 0.5
            size 16
            color "#ddd8ccbb"
            italic True
            text_align 0.5
        null height 20
        text "Alyya Deliani Yusuf":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Asna Nur Halimah":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Dimas Saptahadi":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Futriani":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Ginta Ramadhani":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Nayla Sucia Rahmawati":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Delina Dwi Pebriyanti":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Salwa Rahma Fahira":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5

        null height 70
        frame:
            xalign 0.5
            xsize 600
            ysize 1
            background "#ffffff22"
        null height 60

        ## ── ART AND AUDIO ────────────────────────────────────────────────
        text "ART AND AUDIO":
            xalign 0.5
            size 13
            color "#c8a96e"
            kerning 4.0
            bold True
            text_align 0.5
        null height 10
        text "Nadia Rahmayanti  —  Ketua":
            xalign 0.5
            size 16
            color "#ddd8ccbb"
            italic True
            text_align 0.5
        null height 20
        text "Delia Mutiara":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Refalisha Nurmeta":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Fatia Nuri Ramdani":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Moch Raihan Mujiyanto":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Salma Ashilah":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Zahra Apriani Sanjaya":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Naufal Aghni":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Dwifa Nusa Rahmani":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5

        null height 70
        frame:
            xalign 0.5
            xsize 600
            ysize 1
            background "#ffffff22"
        null height 60

        ## ── GAME DESIGN ──────────────────────────────────────────────────
        text "GAME DESIGN":
            xalign 0.5
            size 13
            color "#c8a96e"
            kerning 4.0
            bold True
            text_align 0.5
        null height 10
        text "Daffa Dharma Wibowo  —  Ketua":
            xalign 0.5
            size 16
            color "#ddd8ccbb"
            italic True
            text_align 0.5
        null height 20
        text "Adelio Rafa Salam":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Keira Hadellya Arifin":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Khaila Razbani":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Nadia Rodhwal Haq":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Riska Permanasari":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Shafira Zefania Fahby":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Weni Prabandani":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5

        null height 70
        frame:
            xalign 0.5
            xsize 600
            ysize 1
            background "#ffffff22"
        null height 60

        ## ── GAME DEVELOPER ───────────────────────────────────────────────
        text "GAME DEVELOPER":
            xalign 0.5
            size 13
            color "#c8a96e"
            kerning 4.0
            bold True
            text_align 0.5
        null height 10
        text "Mohammad Faiz Abdul Hafizh  —  Ketua":
            xalign 0.5
            size 16
            color "#ddd8ccbb"
            italic True
            text_align 0.5
        null height 20
        text "Bhanu Wijaksono":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Haikal Muhammad Jihad":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Mufti Althof Risdiyanto":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Muhammad Syauki Mushafa":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Novela Andauri":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Rifa Alfiyah":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Dimas Krisna Syafa'at Buheri":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Faris Zufar Arkananta":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Zhafira Alfiyya Tabriz":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Nasywaa Mawaddatul Muttaqien":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5

        null height 70
        frame:
            xalign 0.5
            xsize 600
            ysize 1
            background "#ffffff22"
        null height 60

        ## ── QUALITY ASSURANCE AND TESTING ────────────────────────────────
        text "QUALITY ASSURANCE AND TESTING":
            xalign 0.5
            size 13
            color "#c8a96e"
            kerning 4.0
            bold True
            text_align 0.5
        null height 10
        text "Zahra Mutia Rahmah  —  Ketua":
            xalign 0.5
            size 16
            color "#ddd8ccbb"
            italic True
            text_align 0.5
        null height 20
        text "Keysha Ranya Rahil":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Khoerul Sheva Marsyah Fika":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Shafa Aulia":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Rizqi Muhammad Habibi":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Shofia Qurrotaaini":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Tahta Pramesti":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Tia Ulhaq Ulaya":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Tiara Dwi Ananda":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5

        null height 70
        frame:
            xalign 0.5
            xsize 600
            ysize 1
            background "#ffffff22"
        null height 60

        ## ── SYSTEM DESIGN ────────────────────────────────────────────────
        text "SYSTEM DESIGN":
            xalign 0.5
            size 13
            color "#c8a96e"
            kerning 4.0
            bold True
            text_align 0.5
        null height 6
        text "Manajemen & Sistem":
            xalign 0.5
            size 13
            color "#c8a96eaa"
            kerning 2.0
            text_align 0.5
        null height 10
        text "Shaquel Pria Aldebran  —  Ketua":
            xalign 0.5
            size 16
            color "#ddd8ccbb"
            italic True
            text_align 0.5
        null height 20
        text "Fadhil Nurshiddiq":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Siti Zakiyyah Zahra":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Muhamad Hanif Ramadhan":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Muhammad Farrel Fallah":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Rio Putra Hermawan":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5
        null height 6
        text "Tiara Ramziyah Athallah":
            xalign 0.5
            size 17
            color "#888888"
            text_align 0.5

        null height 80
        frame:
            xalign 0.5
            xsize 500
            ysize 2
            background "#c8a96e88"
        null height 80

        ## ── Penutup ──────────────────────────────────────────────────────
        text "Dibuat menggunakan Ren'Py":
            xalign 0.5
            size 15
            color "#555555"
            text_align 0.5
        null height 10
        text "PROJECT GAME  |  PSTI KELAS 2A":
            xalign 0.5
            size 14
            color "#555555"
            kerning 2.0
            text_align 0.5
        null height 30
        text "\"Setiap baris kode adalah bagian dari cerita.\"":
            xalign 0.5
            size 18
            color "#c8a96eaa"
            italic True
            text_align 0.5

        ## Ruang kosong di bawah sebelum selesai
        null height 1080

    # 3. TIMER TUTUP OTOMATIS
    # Saat waktu mencapai 47 detik, layar ini otomatis tertutup dan kembali ke Main Menu.
    # Waktu ini DITAMBAH 2 detik dari kecepatan scroll (45.0) di atas.
    timer 52.0 action Return("done")


## =============================================================================
## LABEL CREDITS
## =============================================================================

label credits:
    # --- Matikan semua suara bising / efek dari adegan sebelumnya ---
    stop sound fadeout 2.0

    # Cek tipe ending
    $ _etype = getattr(store, "credits_ending_type", "good")

    scene black with Dissolve(1.5)
    pause 0.5

    # Mainkan BGM Credit yang Sesuai
    if _etype == "good":
        play music "audio/backsound/ending/good_ending_theme.mp3" fadein 2.0
    else:
        play music "audio/backsound/ending/bad_ending_theme.mp3" fadein 2.0

    # Panggil Screen Credits
    call screen credits_screen(ending_type=_etype) with dissolve

    # Transisi ke hitam sebelum kembali ke layar utama (Main Menu)
    scene black with Dissolve(2.0)
    return