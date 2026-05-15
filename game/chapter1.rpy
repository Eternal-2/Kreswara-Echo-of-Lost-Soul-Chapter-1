init python:
    def countdown(st, at, length=50.0):
        remaining = max(0.0, length - st) # Memastikan angka tidak minus
        return Text("%.1f" % remaining, color="#ff4444", size=40, bold=True), 0.1

default quiz_score    = 0
default quiz_total    = 7
default boss_hp       = 3
default boss_attempts = 0
default fase1_benar   = 0
default fase2_benar   = 0
default fase3_benar   = 0

screen timer_screen(length=50.0):
    timer length action Jump("waktu_habis_boss")
    add DynamicDisplayable(countdown, length=length) xalign 0.92 yalign 0.05

screen radar_roh_screen(level=0):
    $ img_radar = "images/ASSET/RADAR ROH/radar roh #%s.png" % level
    add img_radar at efek_kedip_radar
        
    timer 1.5 action Hide("radar_roh_screen")

screen state_roh_screen(state="tenang"):
    $ img_state = "images/ASSET/STATE ROH/%s.png" % state
    add img_state at efek_kedip_state
        
    timer 1.5 action Hide("state_roh_screen")

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
    add "images/BG/bg cave.png" zoom 1.0 at kalah_fadein

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
    ## Overlay gelap seluruh layar
    add "#000000aa"

    ## Panel utama — tepat di atas area pilihan menu
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

            ## ── Header ──────────────────────────────
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

                ## Garis pemisah
                frame:
                    background "#c8a96e55"
                    xfill True
                    ysize 1

            ## ── Blok kode (hanya jika ada) ──────────
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

            ## ── Pertanyaan ───────────────────────────
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


define k  = Character("Kreswara", color="#5bc8ff")
define a  = Character("AS-LEEN", color="#c3b1e1")
define i  = Character("Ibu Kreswara", color="#f5c8a0")
define b  = Character("Bapak Kreswara", color="#e07050")
define d  = Character("Damar", color="#80d4a0")
define nr = Character(None, what_style="centered_text")
define bc = Character("Buta Cakil", color="#ff3333")


image k_normal:
    im.Scale("images/kreswara/kreswara_normal.png", 750, 1500)
image k_smile:
    im.Scale("images/kreswara/kreswara_smile.png", 750, 1500)
image k_talk:
    im.Scale("images/kreswara/kreswara_talk.png", 750, 1500)
image k_angry:
    im.Scale("images/kreswara/kreswara_angry.png", 750, 1500)
image k_angrytalk:
    im.Scale("images/kreswara/kreswara_angrytalk.png", 750, 1500)
image k_think:
    im.Scale("images/kreswara/kreswara_thinking.png", 750, 1500)

image a_normal:
    im.Scale("images/asleen/asleen_normal.png", 850, 1600)
image a_talk:
    im.Scale("images/asleen/asleen_talk.png", 850, 1600)

image ibu_k:
    im.Scale("images/NPC/NPC_Kreswara Mother.png", 750, 1500)
image bpk_k:
    im.Scale("images/NPC/NPC_Kreswara Father.png", 850, 1700)
image damar:
    im.Scale("images/NPC/NPC_Damar.png", 850, 1900)

image bc_normal:
    im.Scale("images/BOSS/Buta cakil/butacakil_normal.png", 750, 1600)
image bc_talk:
    im.Scale("images/BOSS/Buta cakil/butacakil_talk.png", 750, 1600)


image bg_desa       = "images/BG/bg swamp.png"    
image bg_malam      = "images/BG/bg cave.png"        
image bg_starry     = "images/BG/bg starrysky.png"   
image bg_n2         = "images/BG/bg n2.png"        

image effect_1 = Movie(play="images/EFFECT/1.webm", loop=True, size=(1920, 3413))
image effect_2 = Movie(play="images/EFFECT/2.webm", loop=True, size=(1920, 3413))
image effect_3 = Movie(play="images/EFFECT/3.webm", loop=True, size=(1920, 3413))
image effect_4 = Movie(play="images/EFFECT/4.webm", loop=True, size=(1920, 3413))
image effect_5 = Movie(play="images/EFFECT/5.webm", loop=True, size=(1920, 3413))
image effect_6 = Movie(play="images/EFFECT/6.webm", loop=True, size=(1920, 3413))
image effect_7 = Movie(play="images/EFFECT/7.webm", loop=True, size=(1920, 3413))
image effect_8 = Movie(play="images/EFFECT/8.webm", loop=True, size=(1920, 3413))
image effect_9 = Movie(play="images/EFFECT/9.webm", loop=True, size=(1920, 3413))


label chapter1_full:

    scene bg_desa with dissolve
    play music "audio/lemonade-by-snoozybeats.mp3" fadein 1.5

    nr "Suasana langit jingga menerpa kehangatannya ke sebuah desa kecil yang selalu dialiri tawa semua jiwa di sana, baik tua maupun muda."
    nr "Tak terkecuali seorang pemuda menawan yang tubuhnya penuh kepuasan batin setelah melepas penat—"
    nr "saat kakinya sekali lagi mengantarkannya ke rumahnya: sang bunda tercinta."

    show ibu_k at Position(xalign=0.5, yalign=0.3) with dissolve
    i "Waraaa. Pulang nak, udah hampir malem."
    hide ibu_k

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Tersenyum) Iya bu."
    hide k_smile

    scene bg_malam with fade

    show bpk_k at Position(xalign=0.5, yalign=0.1), napas_berat with dissolve
    b "(Sedikit marah)"
    b "Kreswara Radyana. Kan sudah bapak bilang beberapa kali—"
    b "dirimu ini cukup diam di desa, hidup enak di sini,"
    b "dan jangan membujuk bapak dengan idemu itu lagi!"
    hide bpk_k

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Kecewa) T-tapi pak..."
    k "Di brosur kampus yang Wara pengen ada biaya diskon UKT untuk penerima beasiswa."
    k "Wara akan usahain beasiswa itu kok pak.."
    hide k_talk

    show bpk_k at Position(xalign=0.5, yalign=0.1), getar with dissolve
    b "(Tegas) Jawabannya tetap TIDAK, Wara."
    b "Lagipula jika kau merantau dan berkuliah pun belum tentu sukses,"
    b "angka pengangguran masih tinggi untuk lulusan S1."
    b "Bagaimana jika bapak sudah keluar uang banyak tapi kau malah gagal!?"
    hide bpk_k

    menu:
        "Pasrah":
            jump pilihan_pasrah
        "Marah":
            jump pilihan_marah


label pilihan_pasrah:
    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Kecewa) I-iya pak.... Wara ngerti."
    hide k_talk
    show bpk_k at Position(xalign=0.5, yalign=0.1) with dissolve
    b "Bagus kalau kau ngerti."
    hide bpk_k
    jump scene_kamar


label pilihan_marah:
    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "(Marah) TAPI WARA CAPEK PAK NGIKUTIN EGO BAPAK TERUS!"
    k "WARA PUN PENGEN PUNYA KEINGINAN BUAT HIDUP WARA SENDIRI!!"
    hide k_angrytalk

    play sound "audio/sfx_tamparan.mp3"
    show bpk_k at Position(xalign=0.5, yalign=0.1), getar with dissolve
    b "DASAR ANAK GATAU DIRI."
    b "BAPAK SUDAH CAPEK-CAPEK BEKERJA DAN SEKARANG KAMU DENGAN LANTANGNYA"
    b "MINTA HAL YANG BAPAK GAK SETUJUI."
    b "BALIK SEKARANG KE KAMARMU, CEPAT!!"
    hide bpk_k
    jump scene_kamar

label scene_kamar:
    scene bg_desa with fade
    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Gatau aja dia aku sudah ngumpulin uang buat beli laptop."
    hide k_smile

    scene bg_malam with fade
    centered "Cahaya matahari yang memancarkan panas kemegahannya hari ini menjadi tumpuan Kreswara untuk membuat pilihan tersembunyinya."
    centered "Suara deru knalpot motor temannya mengantarnya ke rumah kenalan yang bersedia membantu."

    play sound "audio/sfx_knalpot.mp3"

    show damar at Position(xalign=0.5, yalign=0.2) with dissolve
    d "Nih laptop yang lu pengen dari kemarin."
    d "Gila juga nyali lu sampai nabung gini Ra."
    hide damar

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Bahagia)"
    hide k_smile

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Iyalah, meskipun kata kamu laptop bekas."
    k "Yang penting ada buat belajar, ya kan?"
    hide k_talk

    show damar at Position(xalign=0.5, yalign=0.2) with dissolve
    d "(Tertawa) Iyadeh, si paling belajar."
    d "Tapi gua gatau juga isinya, nemunya di toko loak sih."
    hide damar

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Ah gampang itu mah Mar."
    k "Di tangan aku mah, langsung jadi jet tempur ni laptop."
    hide k_talk

    show damar at Position(xalign=0.5, yalign=0.2) with dissolve
    d "Halah ada-ada aja lu hahaha."
    d "Yaudeh, hati-hati ya baliknya."
    hide damar

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Iya, makasih ya sekali lagi."
    hide k_talk

    scene bg_n2 with fade
    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Mantap banget laptopnya udah aku dapat!"
    k "Ga sabar ingin cepat-cepat mencoba semua hal yang sudah kupelajari."
    hide k_smile

    show bpk_k at Position(xalign=0.5, yalign=0.1) with dissolve
    b "Waraaa... Kamu sudah menyiapkan buat pertunjukan nanti malam belum nak?"
    hide bpk_k

    show k_normal at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "wa-waduh... Bapak masih di dapur, untung dia ga liat aku bawa laptop."
    hide k_normal

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Iya pak bentar, Wara baru pulang main sama teman!"
    hide k_talk

    show bpk_k at Position(xalign=0.5, yalign=0.1) with dissolve
    b "Nak, tolong siapkan wayang-wayangnya dulu ya."
    b "Bapak mau bicara dulu sama niyaga dan sinden."
    hide bpk_k

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Iya pak, siap."
    hide k_talk

    centered "Suasana panggung temaram di bawah lampu redup—menambah kesan kuat akan pementasan yang sebentar lagi akan berjalan."
    centered "Para wayang masih tergeletak rapi, belum ditancapkan ke gedebog pisang."

    play sound "audio/sfx_wayang_tancap.mp3"

    show k_normal at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Oke, mari kita mulai menyimping wayang."
    k "Urutan simping berada di sebelah kanan serta kiri dalang, dari yang terbesar sampai terkecil."
    k "Dimulai dari Tuguwasesa; untuk simping kiri biasanya para raksasa seperti Nirwatakawaca."
    k "Simpingan yang di kanan dalang adalah lambang keutamaan dan kebijakan;"
    k "simpingan yang di kiri adalah angkara murka."
    hide k_normal

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Sip, selesai deh!"
    hide k_smile

    show bpk_k at Position(xalign=0.5, yalign=0.1) with dissolve
    b "Sudah beres nak?"
    hide bpk_k

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Sudah pak, silahkan."
    hide k_talk

    show bpk_k at Position(xalign=0.5, yalign=0.1) with dissolve
    b "(Senyum) Terimakasih ya."
    hide bpk_k

    show k_talk at Position(xalign=0.5, yalign=0.3)with dissolve
    k "Sama-sama pak!"
    hide k_talk

    play music "audio/gamelan_wayang.mp3" fadein 1.0

    show k_normal at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Seperti biasa, Bapak sangat jago menjadi Dalang."
    k "Melihat hal ini membuatku menyadari suatu hal:"
    k "aku sangat mencintai seni yang ada di keluargaku ini—"
    k "tapi aku juga menyukai saat bisa melakukan apapun dengan baris kode yang setiap malam kupelajari."
    hide k_normal

    centered "Singkat cerita, pertunjukan wayang sudah selesai digelar."

    stop music fadeout 1.0

    show bpk_k at Position(xalign=0.5, yalign=0.1) with dissolve
    b "Nak, nanti tolong jaga rumah ya."
    b "Bapak dan ibu akan pergi keluar kota karena ada urusan dengan teman bapak."
    hide bpk_k

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Oh iya pak gapapa. Kreswara akan jaga rumah kok pak!"
    hide k_talk

    show bpk_k at Position(xalign=0.5, yalign=0.1) with dissolve
    b "Nah, itu baru anak bapak."
    b "Bapak berangkat sekarang ya, jangan lupa bereskan wayang lalu kunci pintunya."
    hide bpk_k

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Iya pak, hati-hati di jalan."
    hide k_talk

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Gatau aja aku bakal main laptop semalaman ini hehe."
    hide k_smile

    centered "Kekosongan rumah yang merekah ke setiap sudut menandakan waktu kebebasan semu untuk Kreswara menyentuh apa yang dia tunggu dari tempo lalu."

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Akhirnyaa...."
    hide k_talk

    play sound "audio/sfx_resleting.mp3"

    centered "Sebuah laptop yang siapapun melihatnya pasti menyadari ia sudah cukup sering berpindah tangan."
    centered "Sebuah jejak teknologi mengukuhkan kehadirannya di antara pemuda dan gerbang tradisional yang melekat dalam dirinya—"
    centered "membuat ledakan emosi kecil tentang bagaimana semua impian Kreswara akhirnya memperlihatkan jalannya."

    play sound "audio/sfx_laptop_on.mp3"

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Oke... kita lihat isi dalemnya."
    hide k_talk

    centered "Folder dibuka satu-satu. Ada yang biasa, ada yang aneh. Sampai satu file bikin Kreswara berhenti."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "'darul_baka.exe'?"
    hide k_think

    show k_normal at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Namanya kayak bukan program biasa."
    hide k_normal

    play sound "audio/sfx_klik.mp3"

    centered "..."
    centered "Tidak terjadi apa-apa."
    centered "Tiba-tiba...."

    play sound "audio/sfx_listrik.mp3"

    centered "Layar tiba-tiba berkedip. Lampu rumah ikut goyang."

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "Hah? Kenapaa iniii???!!"
    hide k_angrytalk

    scene bg_malam with dissolve

    stop music

    centered "Sambaran listrik mengaumkan kehadirannya ke seluruh ruangan—"
    centered "sangat cepat sampai yang bisa dipikirkan Kreswara hanyalah: 'MUNDUR!'"

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "WOI WOI WOI!!"
    hide k_angrytalk

    centered "Putaran energi itu terjadi beriringan dengan tarian menyeramkan yang mengalir ke dinding panggung—"
    centered "melebarkan genggaman volt panasnya, lalu berhenti di satu titik yang tak pernah Kreswara sangka:"
    centered "Rak wayang."

    play sound "audio/sfx_wayang_move.mp3"

    centered "Wayang mulai bergerak. Benang tak terlihat penuh aliran listrik mengikat mereka."
    centered "Satu naik, dua ikut, semuanya pelan-pelan terangkat."

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "(Panik)"
    k "HEY!! JANGAN!!"
    hide k_angrytalk

    centered "Wayang Hilang."
    centered "Rak terakhir yang kebetulan Kreswara sentuh sekarang terasa kosong."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Bingung)"
    k "Duh... barusan aku ngapain sih..."
    k "Wayang bapak... ada yang ilang..."
    hide k_think

    play sound "audio/sfx_asleen_boot.mp3"

    a "Pengguna terdeteksi."

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "(Shock)"
    k "HAH?! SIAPA ITU?!"
    k "Apa ada saksi yang lihat semuanya?!"
    hide k_angrytalk

    centered "....."

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Pastinya engga lah wara"
    k "Jam segini warga desa pasti sudah tidur lelap semua..."
    hide k_talk

    a "Tenang. Saya tidak berbahaya."

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "...."
    hide k_angrytalk

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Kamu dari mana sih?!"
    k "Coba muncul dulu atuh!"
    hide k_think

    a "Saya aktif setelah lonjakan energi tadi."
    a "Tepatnya 7 menit 56 detik yang lalu."

    centered "Kreswara langsung diam. Matanya ke laptop, lalu ke seluruh pojok ruangan, tidak menemukan sumber suara."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Sepertinya program yang tadi bukanlah sekadar hal yang normal..."
    k "Wayang itu... ke mana?"
    hide k_think

    a "Ada. Tidak hilang."
    a "Mereka hanya berpindah ke dunia hybrid-virtual."
    a "Hal yang tentunya tidak bisa kau lihat. Untuk saat ini."

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "...dan sekarang aku harus ngapain?"
    hide k_talk

    a "Mengambilnya kembali."

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "o-oke... Caranya?"
    hide k_talk

    a "Dengan masuk ke sana. Tentu saja."

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Senyum kecil, setengah nekat setengah kesal)"
    k "Yaudah... masukin aja langsung."
    hide k_smile

    a "Tidak bisa."

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "Terus harus gimana sih?! Serba salah!"
    hide k_angrytalk

    a "Kamu harus membuat perangkat bernama PUPILS."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "PUPILS...? Sejenis bagian yang ada di mata?"
    k "...Seriusan harus bikin sendiri?"
    hide k_think

    a "Ya. Gunakan yang ada di sekitarmu. Penglihatan kamu masih bekerja kan?"

    show k_angry at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Nyebelin..."
    hide k_angry

    centered "Kreswara memeriksa sekitar rumah dan panggung."

    a "Siapkan helm bekas sebagai struktur utama."
    a "Tambahkan kardus atau plastik keras di bagian samping dan belakang."
    a "Buat bagian belakang sebagai inti sistem."

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Sudah mulai mengambil barang)"
    k "Oke... lanjut."
    hide k_talk

    a "Tambahkan kotak kecil sebagai modul inti."
    a "Sambungkan kabel dari modul ke bagian depan dan samping. Biarkan terbuka, tidak perlu rapi."

    centered "Tangannya langsung bergerak cepat. Seperti sudah menjadi kebiasaannya sehari-hari."

    a "Pasang busa di dalam helm, lalu tambahkan kawat atau logam di sisi kepala sebagai sensor."
    a "Tambahkan earphone atau visor di depan."
    a "Jangan lupa beri tanda seperti 'SYNC' atau 'NODE'."

    centered "Beberapa menit berlalu. Helm itu sekarang sudah tak berbentuk helm biasa lagi."

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Senyum puas)"
    hide k_smile

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Huftt... akhirnya selesai juga..."
    hide k_talk

    play sound "audio/sfx_klik.mp3"

    centered "Tidak ada reaksi."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Bingung)"
    hide k_think

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Loh? Kok ga nyala?"
    hide k_talk

    a "Karena saya masih di dalam sistem lama."
    a "Saya harus dipindahkan ke PUPILS."

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Jadi aku harus mindahin kamu ke helm?"
    hide k_talk

    a "Benar! Agar saya bisa menjadi inti sistem dan membimbingmu langsung di dunia hybrid."
    a "Gunakan komputer dengan koneksi lebih stabil."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Berpikir) Di mana tempat aku untuk melakukan itu?... Aku tau!"
    hide k_think

    scene bg_n2 with fade
    play music "audio/ambient_perpustakaan.mp3" fadein 1.0

    centered "Kreswara berjalan mengelilingi desa, lalu sampai di perpustakaan desa."
    play sound "audio/sfx_pintu_buka.mp3"

    centered "Komputer yang terlihat usang itu menyala—namun Kreswara tidak bisa langsung mengaksesnya."
    centered "Ia membutuhkan sandi untuk mengakses komputer."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Hmm... ada password komputer. Tapi aku punya cara untuk masuk."
    hide k_think

    play sound "audio/sfx_kabel_pasang.mp3"

    centered "Kreswara menyambungkan semua kabel untuk memindahkan AS-LEEN."

    show effect_1 at truecenter with dissolve

    a "Memulai transfer..."

    play sound "audio/sfx_data_flow.mp3"

    a "Transfer selesai. Saya sekarang berada di PUPILS."

    scene bg_n2 with fade

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Senyum senang)"
    hide k_smile

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Oke... sekarang rasanya lebih serius."
    hide k_talk

    stop music fadeout 1.0
    play music "audio/ambient_hybrid.mp3" fadein 2.0

    play sound "audio/sfx_energi_aktif.mp3"

    show effect_7 at truecenter with dissolve

    pause 3.0 

    scene bg_starry with dissolve

    centered "Cahaya yang sangat terang menutupi tubuh Kreswara."
    centered "Ia berpindah ke dunia hybrid. Pandangannya menghilang dalam kegelapan sekejap."

    centered "Kreswara membuka matanya perlahan."
    centered "Desa terlihat seperti tidak terjadi apa-apa, namun tidak seperti biasanya."
    centered "Lampu menjadi energi utama. Udara di sekitar pun terasa sangat berat."

    show a_normal at Position(xalign=0.5, yalign=0.3) with dissolve
    a "..."
    hide a_normal

    show k_think at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "(Kebingungan) .....?"
    hide k_think

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Saya AS-LEEN."
    hide a_talk

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Terkesima)"
    k "Jadi ini wujudnya..."
    hide k_smile

    centered "Kreswara terdiam kagum. AS-LEEN tampak seperti hologram namun sangat nyata"
    centered "paras cantik dengan mata bulat besar dan ekspresi yang nyaris tidak pernah berubah."

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Jadi apakah wayang itu ada di sini?"
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Ya, wayang itu berada di sekitar sini."
    a "Namun mereka tidak bebas."
    a "Setiap kelompok dikunci oleh entitas kuat."
    a "Kamu harus mengalahkan mereka untuk mengembalikan wayang."
    hide a_talk

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Senyum tipis) Baiklah... waktunya game dimulai."
    hide k_smile

label boss_buta_cakil_start:
    $ boss_hp       = 3
    $ boss_attempts += 1
    $ fase1_benar   = 0
    $ fase2_benar   = 0
    $ fase3_benar   = 0

    scene bg_malam with dissolve
    play music "audio/bgm_boss1.mp3" fadein 0.5

    show screen radar_roh_screen(level=1)
    pause 1.0

    play sound "audio/sfx_distorsi.mp3"

    centered "Belum sempat melakukan apa-apa, Kreswara merasakan tanah mulai bergerak,"
    centered "memunculkan keretakan. Tiba-tiba sosok besar muncul di hadapannya."
    centered "Gerakannya kaku seperti wayang yang rusak."

    show screen state_roh_screen("WASPADA")
    pause 1.0

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Waspada, Wara itu Buta Cakil. Entitas pertama yang mengunci wayang."
    a "Data obsesinya sangat kuat. Satu kesalahan bisa melumpuhkanmu."
    hide a_talk

    show effect_3 at truecenter with dissolve

    pause 3.0 

    scene bg_malam with dissolve

    show bc_talk at Position(xalign=0.5, yalign=0.2) with dissolve
    bc "HAHAHAHA— Kau berani masuk ke sini, manusia?!"
    bc "Aku sudah menunggu sejak lama. Sejak LAMA sekali."
    hide bc_talk

    show k_angrytalk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "..."
    k "Aku tidak peduli kau sudah menunggu berapa lama."
    k "Kembalikan wayang bapakku."
    hide k_angrytalk

    show bc_talk at Position(xalign=0.5, yalign=0.2) with dissolve
    bc "WAYANG?! HAHAHA Kalau bisa kau rebut dari tanganku!"
    hide bc_talk

    centered "── FASE 1: Kenali Pola Serangan ──"
    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Wara, dia melempar data obsesi langsung ke pikiranmu!"
    a "Kamu harus jawab dengan benar itu satu-satunya cara menyerangnya."
    a "Salah, dan serangannya akan balik menghantammu."
    hide a_talk


label soal_1:
    show screen soal_panel(
        nomor="1",
        tema="Python Tipe Data",
        kode="x = 7.5\nprint(type(x))",
        pertanyaan="Apa output dari kode di atas?"
    )

    menu:
        "<class 'int'>":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "UGHHH—! Itu salah"
            k "aku jadi kena serangan nya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "7.5 bukan integer, Wara. Itu bilangan desimal—float!"
            a "Coba lagi, jangan beri dia kesempatan!"
            hide a_talk
            jump soal_1

        "<class 'float'>":
            hide screen soal_panel
            $ fase1_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "FLOAT itu jawabannya!"
            k "Sekarang RASAKAN INI!"
            hide k_angrytalk
            play sound "audio/sfx_serang.mp3"
            show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            bc "GUH!?! Tidak mungkin kau tahu itu...!"
            hide bc_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Bagus! Serangan pertama mengenai. Dia mulai goyah!"
            hide a_talk

        "<class 'str'>":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Ah sial, bukan string!"
            k "Itu sedikit menyakitkan..."
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "7.5 bukan teks, Wara. Pikirkan lagi!"
            hide a_talk
            jump soal_1

        "<class 'bool'>":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Bukan boolean,"
            k "aduh, kepalaku..."
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Bool itu True atau False. 7.5 jelas bukan itu!"
            hide a_talk
            jump soal_1


label soal_2:
    show screen soal_panel(
        nomor="2",
        tema="Sejarah Orde Lama",
        kode="",
        pertanyaan="Dekrit Presiden 5 Juli 1959 oleh Soekarno\nmenyatakan Indonesia kembali ke..."
    )

    menu:
        "Konstitusi RIS":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "SALAH, aku seharusnya tau itu!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "RIS sudah dibubarkan jauh sebelum 1959, Wara. Fokus!"
            hide a_talk
            jump soal_2

        "UUDS 1950":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Bukan"
            k "AUGH, salah lagi!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Justru Dekrit itu membubarkan UUDS 1950, bukan kembali ke sana!"
            hide a_talk
            jump soal_2

        "Piagam Jakarta":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Ugh!"
            k "Piagam Jakarta?"
            k "Seperti nya bukan itu..."
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Piagam Jakarta pernah jadi perdebatan, tapi bukan itu yang dimaksud!"
            hide a_talk
            jump soal_2

        "Undang-Undang Dasar 1945":
            hide screen soal_panel
            $ fase1_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "UUD 1945"
            k "kembali ke konstitusi awal!"
            k "Ini untuk wayang bapakku"
            k "SERANG!!"
            hide k_angrytalk
            play sound "audio/sfx_serang.mp3"
            show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            bc "NGHH"
            bc "Kau... kau tahu sejarah?!"
            hide bc_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Benar! Dekrit itu mengembalikan UUD 1945 dan membubarkan Konstituante."
            a "Dua serangan sudah mengenai. Dia mulai kewalahan!"
            hide a_talk


label soal_3:
    show screen soal_panel(
        nomor="3",
        tema="Python Operator Modulo",
        kode="a = 10\nb = 3\nprint(a %% b)",
        pertanyaan="Apa output dari kode di atas?"
    )

    menu:
        "3":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "CIHH 3 itu hasil baginya, bukan sisanya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Modulo bukan pembagian biasa—itu SISA pembagian!"
            hide a_talk
            jump soal_3

        "1":
            hide screen soal_panel
            $ fase1_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "SATU!!"
            k "10 dibagi 3, sisa 1!"
            k "Aku tidak akan berhenti sampai semua wayang kembali!"
            hide k_angrytalk
            play sound "audio/sfx_serang.mp3"
            show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            bc "GRAAAAHHH Tiga kali?! TIDAK MUNGKIN!"
            hide bc_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Luar biasa, Wara. Fase 1 selesai. Buta Cakil mulai terhuyung!"
            hide a_talk

        "0":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "0?!"
            k "Bukan itu kalau habis dibagi sempurna!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "10 tidak habis dibagi 3. Hitung lagi, cepat!"
            hide a_talk
            jump soal_3

        "3.33":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Itu hasil bagi desimal bukan modulo!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Modulo pakai operator %%, hasilnya sisa—bukan desimal!"
            hide a_talk
            jump soal_3

    if fase1_benar >= 2:
        show k_angrytalk at Position(xalign=0.5, yalign=0.3) with dissolve
        k "Aku mulai bisa membaca gerakanmu, Buta Cakil."
        k "Setiap serangan datamu... aku akan patahkan satu per satu."
        hide k_angrytalk

    jump boss_buta_cakil_fase2


label boss_buta_cakil_fase2:
    hide screen state_roh_screen

    show effect_8 at truecenter with dissolve

    pause 3.0 

    scene bg_malam with dissolve

    centered "── FASE 2: RAGE STATE — Buta Cakil Mengamuk! ──"

    show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
    bc "CUKUP!!"
    bc "CUKUP PERMAINANNYA!"
    bc "Kalau begitu aku tidak akan menahan diri lagi!"
    hide bc_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Wara, hati-hati! Rage State aktif"
    a "Serangannya akan semakin sulit sekarang!"
    hide a_talk

    show k_angrytalk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Semakin sulit?"
    k "Bagus kalau begitu. Aku juga tidak akan menahan diri."
    hide k_angrytalk


label soal_4:
    show screen soal_panel(
        nomor="4",
        tema="Sejarah Konferensi Asia-Afrika",
        kode="",
        pertanyaan="Konferensi Asia-Afrika (1955)\ndiselenggarakan di kota..."
    )

    menu:
        "Jakarta, Indonesia":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Jakarta?!"
            k "ADUHH bukan, bukan Jakarta!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Serangannya makin kuat di fase ini! Fokus ini bukan Jakarta!"
            hide a_talk
            jump soal_4

        "New Delhi, India":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "India?!"
            k "WAHH!! itu sakit sekali!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "KAA 1955 bukan di India. Ini di negeri kita sendiri!"
            hide a_talk
            jump soal_4

        "Bandung, Indonesia":
            hide screen timer_screen
            hide screen soal_panel
            $ fase2_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "BANDUNG!"
            k "kota kita sendiri jadi saksi sejarah dunia!"
            k "Dan kamu, Buta Cakil— ini untuk wayang yang kau curi!"
            hide k_angrytalk
            play sound "audio/sfx_serang.mp3"
            show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            bc "GRAHHHH— Blind spot-ku...!"
            hide bc_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat sasaran! Dasasila Bandung sejarahmu adalah senjatamu!"
            hide a_talk

        "Kuala Lumpur, Malaysia":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Bukan Malaysia"
            k "aduh, serangannya keras sekali!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "KAA itu kebanggaan Indonesia, Wara. Bukan di Malaysia!"
            hide a_talk
            jump soal_4


label soal_5:
    show screen soal_panel(
        nomor="5",
        tema="Python – Tipe Data Input",
        kode="nama = input('Masukkan nama: ')",
        pertanyaan="Tanpa konversi, tipe data variabel nama adalah..."
    )

    menu:
        "integer":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "GRRR integer?!"
            k "Orang aneh mana yang nulis nama pakai angka?!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "input() tidak peduli apa yang diketik—hasilnya selalu teks!"
            hide a_talk
            jump soal_5

        "float":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Float?!"
            k "Ini nama orang, bukan desimal!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "float itu bilangan desimal. input() bukan itu!"
            hide a_talk
            jump soal_5

        "boolean":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Boolean?!"
            k "Nama seseorang bukan True atau False!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "bool itu True/False. input() tidak pernah return itu!"
            hide a_talk
            jump soal_5

        "string":
            hide screen timer_screen
            hide screen soal_panel
            $ fase2_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "String! input() selalu return teks, apapun yang diketik!"
            k "Sekarang aku tidak akan beri kau waktu bernapas, Buta Cakil!"
            hide k_angrytalk
            play sound "audio/sfx_serang.mp3"
            show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            bc "NGGHH— MUSTAHIL! Kau benar-benar tahu semua ini?!"
            hide bc_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Fase 2 selesai! Buta Cakil tersudut. Satu fase lagi!"
            hide a_talk

    if fase2_benar >= 1:
        show k_angrytalk at Position(xalign=0.5, yalign=0.3) with dissolve
        k "Aku tidak punya waktu untuk lemah di sini."
        k "Wayang itu harus kembali ke tangan bapakku."
        hide k_angrytalk

    jump boss_buta_cakil_fase3


label boss_buta_cakil_fase3_retry:
    $ fase3_benar   = 0
    hide screen timer_screen
    hide screen radar_roh_screen
    hide screen state_roh_screen

    scene bg_malam with dissolve
    play music "audio/bgm_boss1.mp3" fadein 0.5

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Kita masih bisa, Wara. Buta Cakil sudah lemah—tinggal fase terakhir!"
    hide a_talk

label boss_buta_cakil_fase3:
    hide screen state_roh_screen
    show screen state_roh_screen("marah")
    pause 1.0

    show effect_3 at truecenter with dissolve

    pause 3.0 

    scene bg_malam with dissolve

    centered "── FASE 3: ENRAGED MODE — Chaos Pressure! ──"

    show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
    bc "TIDAK... TIDAK TIDAK TIDAK!"
    bc "KALAU BEGITU AKU AKAN MENGHANCURKAN SEMUANYA BERSAMAMU!"
    hide bc_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Wara! Enraged Mode ini yang paling berbahaya!"
    a "Tapi kita sudah sejauh ini. Jangan mundur sekarang!"
    hide a_talk

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "Mundur?"
    k "Aku tidak datang ke sini untuk mundur."
    k "Ini pertarungan terakhir, Buta Cakil. Bersiaplah."
    hide k_angrytalk


label soal_6:
    show screen timer_screen(length=30.0)
    show screen soal_panel(
        nomor="6",
        tema="Sejarah Politik Konfrontasi",
        kode="",
        pertanyaan="Politik Konfrontasi (Dwikora) tahun 1963\noleh Soekarno ditujukan kepada..."
    )

    menu:
        "Amerika Serikat":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "AUGH— bukan AS! Aku tidak boleh salah di titik ini!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Dwikora itu respons terhadap pembentukan negara tetangga, bukan Amerika!"
            hide a_talk
            jump soal_6

        "Belanda":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Belanda?! Bukan— itu sudah lewat waktunya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Konflik dengan Belanda soal Irian Barat berbeda konteksnya!"
            hide a_talk
            jump soal_6

        "Uni Soviet":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Soviet?! Salah— dan serangannya terasa seperti api!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Soviet justru punya hubungan dekat dengan Indonesia saat itu!"
            hide a_talk
            jump soal_6

        "Malaysia":
            hide screen timer_screen
            hide screen soal_panel
            $ fase3_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "MALAYSIA— Soekarno menolak pembentukan Federasi Malaysia!"
            k "Sejarah itu senjataku, dan aku tidak akan berhenti!"
            hide k_angrytalk
            play sound "audio/sfx_serang.mp3"
            show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            bc "GRAAAHHHH— Tidak mungkin... tidak... MUNGKIN!"
            hide bc_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Satu pukulan lagi, Wara. Akhiri dia sekarang!"
            hide a_talk


label soal_7:
    show screen timer_screen(length=30.0)
    show screen soal_panel(
        nomor="7 – TERAKHIR",
        tema="Python – Konversi Tipe",
        kode="angka = '10'\nhasil = int(angka)\nprint(hasil)\nprint(type(hasil))",
        pertanyaan="Apa output dari kode di atas?"
    )

    menu:
        "'10' dan <class 'str'>":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "TIDAK— sudah dikonversi! Bukan string lagi!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "int() mengubahnya! Hasilnya bukan str lagi. Pikirkan lagi!"
            hide a_talk
            jump soal_7

        "10 dan <class 'int'>":
            hide screen timer_screen
            hide screen soal_panel
            $ fase3_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "int dari string '10'— hasilnya 10, bertipe INTEGER!"
            k "INI SERANGANKU YANG TERAKHIR UNTUKMU, BUTA CAKIL!!!"
            hide k_angrytalk
            play sound "audio/sfx_serang.mp3"
            jump boss_buta_cakil_menang

        "10.0 dan <class 'float'>":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Float?! Ini int(), bukan float()!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "int() menghasilkan integer, bukan float. Itu beda fungsi!"
            hide a_talk
            jump soal_7

        "Error: tidak bisa mengonversi":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Error?! Tidak— '10' jelas bisa dikonversi ke int!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Python bisa konversi string angka ke int. Tidak ada error!"
            hide a_talk
            jump soal_7

label boss_buta_cakil_menang:
    hide screen radar_roh_screen
    hide screen timer_screen
    stop music fadeout 0.5

    play sound "audio/sfx_boss_ledakan.mp3"

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "SELESAIKAN!!"
    hide k_angrytalk

    show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
    bc "AGHHH!!! tidak... MUNGKIN!"
    bc "AKU... BUTA CAKIL..."
    hide bc_talk

    show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
    bc "TIDAK MUNGKIN KALAH!!!"
    hide bc_talk

    show effect_3 at truecenter with dissolve

    pause 3.0 

    scene bg_malam with dissolve

    centered "Tubuh Buta Cakil mulai pudar dan menjadi cahaya"
    centered "lalu ia perlahan masuk ke sistem."

    play music "audio/ambient_hybrid.mp3" fadein 1.5

    centered "Beberapa titik cahaya muncul di sekitar. Wayang yang tadi hilang... mulai kembali satu per satu."

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Senyum lega)"
    hide k_smile

    show k_talk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "Akhirnya......"
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Itu baru sebagian."
    hide a_talk

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "(Terkejut)"
    k " Hah!! Ya ampun.."
    hide k_angrytalk

    show k_talk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "Artinya perjalananku masih panjang ya?"
    hide k_talk
    
    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Benar sekali!"
    a "Dan berikutnya akan lebih sulit."
    hide a_talk

    centered "Kreswara menarik napas panjang—bukan karena takut, tapi karena siap untuk melawan semua musuh yang akan datang."

    centered "── DATA ROH BUTA CAKIL TERSIMPAN ──"
    centered "Radar Roh meningkat. Satu entitas berhasil dijinakkan."


    jump chapter1_ending


label waktu_habis_boss:
    hide screen timer_screen
    hide screen radar_roh_screen
    hide screen state_roh_screen
    $ renpy.block_rollback()

    play sound "audio/sfx_kalah.mp3"
    call screen kalah_boss_screen()

    if _return == "restart":
        jump boss_buta_cakil_fase3_retry
    else:
        jump chapter_select_screen


label chapter1_ending:
    stop music fadeout 1.5
    scene bg_starry with dissolve

    centered "── CHAPTER 1 SELESAI ──"
    centered "\"Malam Mencekam\""

    centered "Perjalanan Kreswara masih panjang."
    centered "Boss berikutnya: Dursasana — Tema Pemburuan & Hukuman."
    centered "Sampai jumpa di Chapter 2: Perburuan Fajar."

    pause 1.5                       
    scene black with Dissolve(2.0)   
    pause 1.0                        

    $ persistent.chapter2_unlocked = True
    jump chapter_select_screen

label chapter_select_screen:
    call screen chapter_select()
    return
