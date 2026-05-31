define k  = Character("Kreswara",      color="#5bc8ff")
define a  = Character("AS-LEEN",       color="#c3b1e1")
define i  = Character("Ibu Kreswara",  color="#f5c8a0")
define b  = Character("Bapak Kreswara",color="#e07050")
define d  = Character("Damar",         color="#80d4a0")
define nr = Character(None, what_style="centered_text")
define bc = Character("Buta Cakil",    color="#ff3333")
define ds = Character("Dursasana",    color="#ff3333")
define sk = Character("Sengkuni",  color="#9933ff")
define dur = Character("Duryodana",    color="#B4C452")


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
image a_nod:
    im.Scale("images/asleen/asleen_nod.png", 850, 1600)
image a_siluet:
    im.Scale("images/asleen/siluet_asleen.png", 850, 1600)
image a_smile:
    im.Scale("images/asleen/asleen_smile.png", 850, 1600)
image a_poisoned:
    im.Scale("images/asleen/asleen_poisoned.png", 850, 1600)
image a_poisoned_talk:
    im.Scale("images/asleen/asleen_poisoned_talk.png", 850, 1600)
image a_poisoned_smile:
    im.Scale("images/asleen/kena_poisoned_smile.png", 850, 1600)

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

image ds_normal:
    im.Scale("images/BOSS/Dursasana/dursasana_normal.png", 850, 1700)
image ds_talk:
    im.Scale("images/BOSS/Dursasana/dursasana_talk.png", 850, 1700)

image sk_normal:
    im.Scale("images/BOSS/Sengkuni/Sengkuni_normal.png", 750, 1600)
image sk_talk:
    im.Scale("images/BOSS/Sengkuni/Sengkuni_talk.png", 750, 1600)

image dur_normal:
    im.Scale("images/BOSS/Duryodana/Duryodana_.png", 850, 1700)
image dur_talk:
    im.Scale("images/BOSS/Duryodana/Duryodana ngomong_.png", 850, 1700)

# Background Chapter 1
image bg_desa_siang       = im.Scale("images/BG/BG chapter 1/rumah kreswara ketika siang hari.png", 1920, 1080)    
image bg_desa_malam       = im.Scale("images/BG/BG chapter 1/rumah kreswara malam.png", 1920, 1080)        
image bg_ruangan_siang    = im.Scale("images/BG/BG chapter 1/DALAM RUMAH KRESWARA  (SIANG).png", 1920, 1080) 
image bg_ruangan_malam    = im.Scale("images/BG/BG chapter 1/DALAM RUMAH KRESWARA (MALAM).png", 1920, 1080)
image bg_cod              = im.Scale("images/BG/BG chapter 1/Kreswara menuju pulang ke rumah .png", 1920, 1080)
image bg_nyimping         = im.Scale("images/BG/BG chapter 1/Kreswara Nyimping Wayang.png", 1920, 1080)     
image bg_panggung         = im.Scale("images/BG/BG chapter 1/panggung wayang .png", 1920, 1080) 
image bg_panggung_khusus  = im.Scale("images/BG/BG chapter 1/Wara melihat Bapaknya Jadi dalang.png", 1920, 1080)
image bg_rakit_pupils     = im.Scale("images/BG/BG chapter 1/Kreswara Rakit Pupils.png", 1920, 1080)
image bg_perpus           = im.Scale("images/BG/BG chapter 1/perpustakaan desa malam hari.png", 1920, 1080)
image bg_masuk_pupils     = im.Scale("images/BG/BG chapter 1/KRESWARA BERADA DI PERPUSTAKAAN MENGGUNAKAN PUPILS(1).png", 1920, 1080)
image bg_dunia_lain       = im.Scale("images/BG/BG chapter 1/desa digital + anomali .png", 1920, 1080)
image bg_versus           = im.Scale("images/BG/BG chapter 1/KRESWARA LAWAN BUTA CAKIL.png", 1920, 1080)
image bg_menang           = im.Scale("images/BG/BG chapter 1/KRESWARA MENGALAHKAN BUTA CAKIL.png", 1920, 1080)

# Background Chapter 2
image bg_ch2_asleen_error     = im.Scale("images/BG/BG Chapter 2/BG wara dan as-leen ngobrol saat puplis eror .png", 1920, 1080)
image bg_ch2_nav_error        = im.Scale("images/BG/BG Chapter 2/Navigator As-Leen bermasalah (lebih realistis).png", 1920, 1080)
image bg_ch2_nav_error_v2     = im.Scale("images/BG/BG Chapter 2/Navigatir as-leen bermasalah .png", 1920, 1080)
image bg_ch2_labirin          = im.Scale("images/BG/BG Chapter 2/reruntuhan labirin .png", 1920, 1080)
image bg_ch2_jalan_labirin    = im.Scale("images/BG/BG Chapter 2/kreswara berjalan dan mengobrol dengan as-leen di tengah reruntuhan labirin .png", 1920, 1080)
image bg_ch2_jalan_melayang   = im.Scale("images/BG/BG Chapter 2/kreswara berjalan dan mengobrol dengan as-leen di tengah reruntuhan labirin (VERSI MELAYANG).png", 1920, 1080)
image bg_ch2_pupils_nyala     = im.Scale("images/BG/BG Chapter 2/layar PUPILS tiba tiba menyala .png", 1920, 1080)
image bg_ch2_pupils_nyala_v2  = im.Scale("images/BG/BG Chapter 2/layar PUPILS tiba tiba menyala (1).png", 1920, 1080)
image bg_ch2_puzzle           = im.Scale("images/BG/BG Chapter 2/kreswara menyusun puzzle .png", 1920, 1080)
image bg_ch2_puzzle_v2        = im.Scale("images/BG/BG Chapter 2/kreswara menyusun puzzle V2 .png", 1920, 1080)
image bg_ch2_sebelum_puzzle   = im.Scale("images/BG/BG Chapter 2/BG sebelum menyelesaikan puzzle .png", 1920, 1080)
image bg_ch2_pintu_biner      = im.Scale("images/BG/BG Chapter 2/pintu besar kode binner .png", 1920, 1080)
image bg_ch2_pintu_terbuka    = im.Scale("images/BG/BG Chapter 2/Pintu besar terbuka setelah memecahkan kode biner.png", 1920, 1080)
image bg_ch2_pintu_terbuka_v2 = im.Scale("images/BG/BG Chapter 2/Pintu besar terbuka setelah memecahkan kode biner(1).png", 1920, 1080)
image bg_ch2_sebelum_ds       = im.Scale("images/BG/BG Chapter 2/BG sebelum bertemu dursasana .png", 1920, 1080)
image bg_ch2_bertemu_ds       = im.Scale("images/BG/BG Chapter 2/Copy of Kreswara bertemu dursasana.png", 1920, 1080)
image bg_ch2_bertemu_ds_v2    = im.Scale("images/BG/BG Chapter 2/Copy of Kreswara bertemu dursasana(1).png", 1920, 1080)
image bg_ch2_lawan_ds         = im.Scale("images/BG/BG Chapter 2/kreswara melawan dursasana.png", 1920, 1080)
image bg_ch2_menang_ds        = im.Scale("images/BG/BG Chapter 2/Kreswara mengalahkan dursasana.png", 1920, 1080)

# Background Chapter 3
image bg_black_white              = im.Scale("images/BG/BG Chapter 3/black and white version .png", 1920, 1080)
image bg_panggung_dimensi_lain    = im.Scale("images/BG/BG Chapter 3/panggung wayang + dimensi lain .png", 1920, 1080)
image bg_c3_new_kamboja        = im.Scale("images/BG/BG Chapter 3/bg ruangan buntu bunga kamboja .png", 1920, 1080)
image bg_c3_new_lorong_pintu   = im.Scale("images/BG/BG Chapter 3/pintu terbuka lebar .png", 1920, 1080)
image bg_c3_new_lawan_sengkuni = im.Scale("images/BG/BG Chapter 3/bg polos wara bertemu dan melawan sengkuni .png", 1920, 1080)
image bg_c3_new_asleen_racun   = im.Scale("images/BG/BG Chapter 3/bg ketika as-leen kena racun .png", 1920, 1080)
image bg_c3_new_topang_asleen  = im.Scale("images/BG/BG Chapter 3/bg polos menopang tubuh as-leen .png", 1920, 1080)
image bg_c3_roh_kamboja    = im.Scale("images/BG/BG Chapter 3/kreswara berada di ruangan buntu dan melihat beberapa roh data kecil dengan lantai bunga kamboja .png", 1920, 1080)
image bg_c3_lorong_pintu   = im.Scale("images/BG/BG Chapter 3/kreswara dan as-leen berjalan menyusuri lorong hingga diujung bertemu pintu besar yang sudah terbuka lebar.png", 1920, 1080)
image bg_c3_jarum_retak    = im.Scale("images/BG/BG Chapter 3/setelah masuk dinding ruangan tibatiba retak ribuan jarum melesat seperti hujan pecahan kaca.png", 1920, 1080)
image bg_c3_asleen_racun   = im.Scale("images/BG/BG Chapter 3/As-leen terkena racun setelah menahan jarum yang akan mengenai kreswara.png", 1920, 1080)
image bg_c3_bertemu_sengkuni = im.Scale("images/BG/BG Chapter 3/kreswara bertemu sengkuni.png", 1920, 1080)
image bg_c3_sengkuni_hantam  = im.Scale("images/BG/BG Chapter 3/sengkuni menghantam kreswara.png", 1920, 1080)
image bg_c3_wara_serang    = im.Scale("images/BG/BG Chapter 3/kreswara menyerang sengkuni.png", 1920, 1080)
image bg_c3_sengkuni_kalah = im.Scale("images/BG/BG Chapter 3/kreswara mengalahkan Sengkuni.png", 1920, 1080)
image bg_c3_gendong        = im.Scale("images/BG/BG Chapter 3/kreswara menggendong as-leen setelah terkena racun .png", 1920, 1080)
image bg_c3_pintu_tutup_1  = im.Scale("images/BG/BG Chapter 3/pintu besar mulai tertutup sendiri yang menandakan wara dan as-leen sudah terjebak.png", 1920, 1080)
image bg_c3_pintu_tutup_2  = im.Scale("images/BG/BG Chapter 3/pintu besar mulai tertutup sendiri yang menandakan wara dan as-leen sudah terjebak  (1).png", 1920, 1080)
image bg_c3_topang_asleen  = im.Scale("images/BG/BG Chapter 3/Kreswara menopang tubuh As-leen sambil menatapnya.png", 1920, 1080)
image bg_c3_asleen_menghampiri_untuk_digendong    = im.Scale("images/BG/BG Chapter 3/as-leen menghampiri krewara untuk untuk digendong.png", 1920, 1080)

# Background Chapter 4
image bg_batu             = im.Scale("images/BG/BG Chapter 4/AWAL.png", 1920, 1080)
image bg_taman            = im.Scale("images/BG/BG Chapter 4/TAMAN.png", 1920, 1080)
image bg_tamantimer       = im.Scale("images/BG/BG Chapter 4/TIMER.png", 1920, 1080)
image bg_waraobatiasleen  = im.Scale("images/BG/BG Chapter 4/wara mengobati as-leen.png", 1920, 1080)
image bg_desa_replika     = im.Scale("images/BG/BG Chapter 4/desa replika.png", 1950, 1500)
image bg_desa_replikawara = im.Scale("images/BG/BG Chapter 4/wara dan as-leen berjalan ke replikasi desa wara V2 .png", 1920, 1080)
image bg_gelut            = im.Scale("images/BG/BG Chapter 4/wara dan as-leen tiba di depan istana duryadana .png", 1920, 1080)
image bg_duryodana        = im.Scale("images/BG/BG Chapter 4/wara dan as-leen bertemu duryodana.png", 1920, 1080)
image bg_versus_dur       = im.Scale("images/BG/BG Chapter 4/wara melawan duryodana di arena battle .png", 1920, 1080)
image bg_kerajaan         = im.Scale("images/BG/BG Chapter 4/Kerajaan duryodana.png", 1950, 1500)
image bg_istana_duryodana = im.Scale("images/BG/BG Chapter 4/tanah hancur.png", 1920, 1080)
image bg_menang_dur       = im.Scale("images/BG/BG Chapter 4/wara mengalahkan duryodana.png", 1920, 1080)
image bg_langit_jingga_virtual = im.Scale("images/BG/BG Chapter 4/langit senja setelah kemenangan melawan duryodana .png", 1920, 1080)
image bg_langit_jingga_pisah = im.Scale("images/BG/BG Chapter 4/perpisahan wara dengan as-leen .png", 1920, 1080)


image rumah_sakit_good  =  im.Scale("images/BG/Ending/GOOD ENDING .png", 1920, 1080)
image rumah_sakit_good_bangun  =  im.Scale("images/BG/Ending/GOOD ENDING WARA BANGUN .png", 1920, 1080)
image rumah_sakit_bad   =  im.Scale("images/BG/Ending/BAD ENDING .png", 1920, 1080)

image effect_1 = Movie(play="images/EFFECT/1.webm", loop=True, size=(1920, 3413))
image effect_2 = Movie(play="images/EFFECT/2.webm", loop=True, size=(1920, 3413))
image effect_3 = Movie(play="images/EFFECT/3.webm", loop=True, size=(1920, 3413))
image effect_4 = Movie(play="images/EFFECT/4.webm", loop=True, size=(1920, 3413))
image effect_5 = Movie(play="images/EFFECT/5.webm", loop=True, size=(1920, 3413))
image effect_6 = Movie(play="images/EFFECT/6.webm", loop=True, size=(1920, 3413))
image effect_7 = Movie(play="images/EFFECT/7.webm", loop=True, size=(1920, 3413))
image effect_8 = Movie(play="images/EFFECT/8.webm", loop=True, size=(1920, 3413))
image effect_9 = Movie(play="images/EFFECT/9.webm", loop=True, size=(1920, 3413))
image effect_10 = Movie(play="images/EFFECT/10.webm", loop=True, size=(1920, 2030))