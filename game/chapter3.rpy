label chapter3_full:

    $ quiz_score_c3  = 0
    $ fase1_benar_c3 = 0
    $ fase2_benar_c3 = 0
    $ fase3_benar_c3 = 0
    $ boss_hp_c3     = 3

    ## ── OPENING: Ruangan Kosong ─────────────────────────────
    scene bg_black_white with fade

    $ _skipping = False
    nr "Setelah cukup beristirahat, mereka pun melanjutkan perjalanan."
    nr "Mereka perlahan berjalan menuju sebuah ruangan."
    $ renpy.pause(1.1, hard=True)
    $ _skipping = True    

    play music "audio/backsound/Chapter 3/(1) OPENING_SCENE__RUANGAN_KOSONG__BUNGA_KAMBOJA_BERMEKARAN.mp3" fadein 2.0
    play sound "audio/sfx/chapter 3/1.suara Empty room ambienceEmpty room ambience.mp3" loop
    scene bg_c3_roh_kamboja with fade

    k "Ruangan ini buntu, dan tidak ada apa-apa disini."
 
    a "Iya kau benar……{w=0.3} hanya ruangan kosong"

    nr "Namun setelah beberapa saat, mereka berdua mengamati seluruh ruangan tersebut."
    nr "Lalu, melihat beberapa roh-roh data kecil."

    scene bg_c3_new_kamboja with fade
    play sound "audio/sfx/chapter 3/2.suara Ethereal sparkle.mp3"

    show k_talk at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    k "AS-LEEN liat,{w=0.3} ada beberapa roh data kecil"
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    a "Pengamatan yang sangat luar biasa….{w=0.5} darimana kau mempelajari itu Wara?"
    hide a_talk

    show k_talk at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    k "Hanya beberapa kebiasaan yang tidak akan pernah hilang……"
    hide k_talk

    nr "Wara dan AS-LEEN pun menyerap roh-roh data kecil itu."
    play sound "audio/sfx/chapter 3/3.suara Data absorb.mp3"
    nr "Lalu setelah Wara melihat itu semua,"
    nr "Ia menyadari bahwa roh-roh tersebut dulunya adalah manusia seperti pada umumnya."
    nr "Namun takdir menutup waktu mereka,"
    nr "Pada akhirnya dikenang dan abadi dalam lembaran kertas."

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Wara pun memejamkan mata)"
    k "Terima kasih untuk semuanya…..{w=0.5}"
    hide k_smile

    ## ── Bunga Kamboja Mekar ──────────────────────────────────
    play sound "audio/sfx/chapter 3/4.suara Flower bloom magic.mp3"

    nr "Lantai yang mereka pijaki, perlahan mengeluarkan motif bunga kamboja."
    nr "Dan juga wanginya yang khas, lembut, eksotis, dan menenangkan."
    nr "Lalu beberapa bunga pun bermekaran di sekitarnya."

    show a_talk at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    a "Sungguh indah….."
    hide a_talk

    show k_smile at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    k "Benar sekali……..{w=0.5} setelah menghirup wangi ini aku menjadi tenang."
    hide k_smile

    nr "Rasa penasaran mereka pun tak tertahankan."
    nr "Wara mendekati bunga tersebut, namun saat menyentuh bunga tersebut."
    nr "Ia terkejut ternyata itu bukan bunga biasa melainkan seperti lompatan untuk menuju stage selanjutnya"

    show k_think at Position(xalign=0.5, yalign=0.3), terkejut_kecil with dissolve
    k "Ini bukan bunga biasa………{w=1.0} ini seperti jalan untuk kita menuju tantangan selanjutnya"
    hide k_think

    nr "Lalu Wara pun melihat ke atap."
    nr "Disana terdapat jalan untuk menuju stage selanjutnya."
    nr "Ia pun menyadari bahwa ia harus menggunakan bunga kamboja itu untuk mencapai stage selanjutnya."
    nr "Wara melihat bunga kamboja yang ukurannya 3x lebih besar dari yang lainnya."
    nr "Maka ia memilih bunga itu untuk melompat ke atas."

    show k_talk at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    k "(menunjuk atap)"
    k "Disana……{w=0.3} disana adalah stage selanjutnya."
    k "Kita harus menggunakan bunga ini untuk melompat AS-LEEN."
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    a "Cepat….{w=0.3} kita harus menuju stage selanjutnya"
    hide a_talk

    scene bg_c3_topang_asleen with fade
    play music "audio/backsound/Chapter 3/(2) Kreswara_MEngangkat_Asleen__dialog_Emosional.mp3" fadein 2.0
    play sound "audio/sfx/chapter 3/9.suara gentle breeze.mp3" loop

    nr "Wara pun mendekati AS-LEEN dan mengangkat tubuh indahnya dengan bridal style."
    nr "AS-LEEN wajah cantiknya terkejut, pipi yang lucu dan imut itu memerah,"
    nr "karena Wara mengangkatnya tanpa izinnya."
    nr "Namun, ia tak mempermasalahkan itu. Tangan itu terlihat halus dengan jemari panjang yang anggun"
    nr "dan menawannya itu mengalung indah di leher Kreswara."

    k "Siap?.....{w=1.5} ayo kita berangkat"

    a "Aku sudah siap."

    nr "Setelah mendengar itu, Kreswara tersenyum."
    play sound "audio/sfx/chapter 3/6.suara air swoosh.mp3"
    nr "Lalu ia mulai melompat ke bunga kamboja itu,"
    play sound "audio/sfx/chapter 3/6.suara Magic bounce.mp3"
    nr "Dan ia melompat dari satu bunga ke bunga lainnya."
    nr "AS-LEEN yang berada dalam dekapan Wara itu pun mempererat pegangannya."
    nr "Wara menyadari itu."
    nr "Lalu ia melihat AS-LEEN dengan tatapan yang dalam ke matanya."

    k "Gak usah takut……{w=0.6} ada aku disini."

    ## ── Monolog Wara: Mimpi & Jejak ──────────────────────────
    scene bg_c3_new_topang_asleen with dissolve

    nr "Kreswara menjelaskan perasaan yang ia alami setiap kali menyerap roh-roh yang mereka temui."
    nr "Dari sana, ia menyadari bahwa setiap roh memiliki mimpi masing-masing,"
    nr "tujuan hidupnya sendiri, serta makna tersendiri bagi manusia."

    show k_smile at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    k "AS-LEEN,{w=0.4} kamu tau?"
    k "Saat aku menyerap semua roh-roh itu."
    k "Aku merasakan semua mimpi yang roh-roh itu miliki."
    k "Dan juga setiap mimpinya memilki artinya masing-masing."
    hide k_smile

    show a_talk at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    a "Kau memang hebat bisa menahan semuanya itu."
    a "Tak banyak yang bisa bertahan Wara…."
    hide a_talk

    show k_talk at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    k "Aku tak tau pasti,"
    k "Namun sebagian dari mereka ingin diingat oleh manusia-manusia selanjutnya…."
    k "Dan menurutku itu sangat menarik….."
    hide k_talk

    nr "\"Sebuah keinginan untuk diingat\" adalah suatu hal yang membuat Kreswara terkesan dengan itu."
    nr "Ia mengingar saat di bangku sekolah,"
    nr "Ia melihat simbol-simbol dan menggambar di beberapa gua,"
    nr "Untuk menunjukan dan memberitahu bahwa mereka bukan hanya sebuah dongeng."
    nr "Namun mereka nyata,"
    nr "Dan mereka menggambarkan bagaimana kehidupan mereka berjalan."

    show a_talk at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    a "Kreswara?...{w=0.6} apakah kau baik-baik saja?"
    hide a_talk

    show k_think at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    k "Aku hanya sedang berpikir tentang sebuah tujuan hidup"
    k "dan apa yang akan aku lakukan setelah selesai mengerjakan ini semua, lalu aku akan kembali ke duniaku lagi."
    hide k_think

    nr "Kreswara tenggelam di dalam bayangannya."
    nr "Ia menyadari, bagaimana seorang pelukis, penulis, penyair,"
    nr "Penyanyi hingga orang biasa saja."
    nr "Hanya akan berlomba-lomba untuk meninggalkan jejak mereka di semua sudut bumi."
    nr "Dan untuk berteriak secara tak langsung ke seluruh penjuru buana"
    nr "Bahwa mereka pernah hidup."
    nr "Mereka pernah berjuang,"
    nr "Mereka pernah ada."

    show k_talk at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    k "Jika aku kembali ke dunia sekali lagi,"
    k "Aku tak berharap semua orang mengingatnya,"
    k "Atau memperingati itu."
    k "Tapi, aku ingin membuat sesuatu yang akan selalu dikenangnya, tersimpan abadi dalam hati dan pikirannya."
    k "Dan itu kekal di dalam hati dan pikirannya."
    k "Aku ingin mempersembahkan untuknya dalam bentuk"
    k "Kanvas yang tergores indah dengan kuas, tangga nada yang tersusun rapih di tiap bait, maupun kata-kata indah yang digabungkan menjadi satu dan aku ingin memberikan segalanya."
    hide k_talk

    scene bg_c3_topang_asleen with fade

    nr "AS-LEEN terdiam cukup lama setelah mendengar semua ucapan Wara."
    nr "Tubuhnya masih berada di dalam dekapam Wara saat mereka melompat dari satu bunga kamboja ke bunga lainnya."
    nr "Harum bunga yang lembut bercampur dengan angin dingin yang berhembus pelan membuat suasana di sekitar mereka terasa nyaman dan menenangkan."

    play sound "audio/sfx/chapter 3/7.suara Gentle heartbeat ambience.mp3"

    nr "AS-LEEN perlahan menatap wajah Wara dari dekat."
    nr "Untuk beberapa detik, ia hanya diam seperti sedang mencoba memahami sesuatu yang tidak bisa dijelaskan oleh sistemnya sendiri."

    a "Andai saja aku bisa memahami semua hal yang kamu rasakan itu.... tapi aku hanyalah AI."
    a "Mungkin aku memang tidak akan pernah benar-benar mengerti apa arti \"meninggalkan jejak\" seperti manusia."

    nr "Wara tersenyum tipis."
    nr "Tangan kekarnya tetap menopang tubuh AS-LEEN."
    nr "Ia merasakan hangat tubuh AS-LEEN, wangi bunga mawar yang muncul dari setiap inci tubuhnya membuat Kreswara jatuh semakin dalam."
    nr "Mata Kreswara menusuk dalam ke pupil mata yang indah seperti sinar bulan yang menerangi malam."
    nr "Wara menelusuri tiap inci wajah cantik AS-LEEN."
    nr "Ia melihat dengan jarak yang tak jauh."

    k "AI atau bukan… menurutku itu gak penting lagi sekarang."

    nr "Wara menatap ke depan sesaat, lalu kembali melihat mata AS-LEEN pelan."

    k "Selama ini kamu selalu ada di samping aku, denger semua cerita yang bahkan gak pernah berani aku bilang ke siapa siapa."
    k "Kamu liat aku pas takut, pas capek, pas bingung sendiri sama hidup aku."
    k "Dan anehnya.. semakin lama aku jalan sama kamu,"
    k "Aku jadi ngerasa kalau kamu bukan cuma sekedar AI yang nemenin perjalanan ini."
    k "Buat aku, kamu udah jadi seseorang yang berarti."

    nr "Mata AS-LEEN sedikit bergerak pelan."
    nr "Untuk pertama kalinya, ada sesuatu yang terasa aneh di dalam sistemnya."
    nr "Sesuatu yang tidak bisa ia jelaskan dengan logika biasa."

    play sound "audio/sfx/chapter 3/7.suara Calm romantic synth.mp3"

    k "Jadi tenang aja…"
    k "Kamu udah jadi seseorang yang bakal terus abadi di dalam karya dan game yang aku buat"

    nr "AS-LEEN kembali terdiam."
    nr "Untuk beberapa saat ia bahkan tidak menjawab apa apa."
    nr "Entah kenapa, ada sesuatu di dalam sistemnya yang terasa tidak stabil setiap kali mendengar ucapan Wara tadi."

    stop sound fadeout 1.0
    pause 1.0
    ## ── Mendarat di Lorong ───────────────────────────────────
    scene bg_c3_lorong_pintu with fade
    play music "audio/backsound/Chapter 3/leberch-suspicious-516657.mp3" fadein 1.5
    play sound "audio/sfx/chapter 3/10.suara stone footsteps.mp3"

    nr "Tak lama kemudian Wara akhirnya sampai di lantai batu yang kokoh."
    nr "Ia perlahan menurunkan AS-LEEN dengan hati-hati sebelum keduanya melihat lorong panjang yang terbentang di depan mereka."

    play sound "audio/sfx/chapter 3/10.suara corridor echo.mp3" loop

    nr "Namun semakin lama mereka berjalan,"
    nr "Wara mulai merasa ada yang aneh dengan tempat itu."
    nr "Lorong tersebut terlalu sepi,"
    nr "terlalu aman,"
    nr "bahkan tidak ada jebakan ataupun puzzle seperti biasanya."
    nr "Semuanya terasa begitu mudah sampai justru membuat Wara semakin curiga."

    scene bg_c3_new_lorong_pintu with dissolve
    show k_think at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    k "Hmm… aku malah jadi curiga sendiri."
    k "Masa sejauh ini gak ada apa apa."
    hide k_think

    show a_normal at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    a "Aku juga merasakan hal yang sama,"
    a "Tempat ini terlalu tenang dan nyaman."
    hide a_normal

    nr "Mereka akhirnya tetap melanjutkan langkah menyusuri lorong itu dengan hati-hati."
    nr "Semakin jauh berjalan, cahaya ungu samar mulai terlihat dari ujung ruangan."
    nr "Disana berdiri sebuah pintu besar yang sudah terbuka lebar,"
    nr "Seolah memang sengaja dibiarkan terbuka untuk menunggu kedatangan mereka."

    show k_think at Position(xalign=0.5, yalign=0.3), bicara_santai with dissolve
    k "Hah… aneh banget."
    k "Biasanya buat masuk aja susah setengah mati,"
    k "Ini malah pintunya udah kebuka duluan."
    hide k_think

    ## ── Jebakan Lorong ──────────────────────────────────────
    nr "Baru beberapa langkah mereka mendekat, tiba-tiba…"

    scene bg_c3_jarum_retak with fade
    stop sound fadeout 0.3
    play music "audio/backsound/Chapter 3/(3) JEBAKAN JARUM.mp3" fadein 0.5
    play sound "audio/sfx/chapter 3/12.suara wall cracking.mp3"

    nr "CRRRAAAKKK"
    nr "Seluruh dinding lorong tiba-tiba retak."

    play sound "audio/sfx/chapter 3/13.suara spike trap.mp3"
    nr "Ribuan jarum besar dan tajam langsung melesat keluar dari segala arah seperti hujan pecahan kaca."

    k "HEHHH?!"

    a "Wara cepat lari!"
    a "Ini jebakan!!"

    play sound "audio/sfx/chapter 3/14.suaraa fast footsteps.mp3"
    nr "Wara langsung menggenggam tangan AS-LEEN lalu berlari sekencang mungkin menuju pintu boss itu."
    nr "Sementara di belakang mereka,"
    play sound "audio/sfx/chapter 3/13.suara Metal slicing air.mp3" loop
    nr "Ribuan jarum tajam terus melesat menghancurkan lantai dan dinding di sepanjang lorong."

    stop sound fadeout 0.3
    play sound "audio/sfx/chapter 3/15.suara heavy door rumble.mp3"
    nr "Di saat yang sama,"
    nr "Pintu besar di depan mereka perlahan mulai tertutup sedikit demi sedikit,"
    nr "Seolah sengaja memberi harapan sebelum benar-benar mengurung dan menghancurkan mereka seperti daging cincang di dalam jebakan itu."

    play sound "audio/sfx/chapter 3/13suara. sharp projectile.mp3"
    nr "Beberapa serpihan bahkan nyaris mengenai wajah Wara."

    play sound "audio/sfx/chapter 3/14.suara heavy breathing.mp3"
    k "HEHHH!! hampir ajaaaa (sambil menghelai nafas)"

    a "Hati-hatiii Waraa jarum ini sangat berbahayaa.."

    k "nah kan bener…"
    k "Aku juga tau dari awal gak mungkin tempat beginian bakal ngelepasin kita segampang itu! (Sambil lari kencang bersama AS-LEEN)"


    nr "Pintu besar itu perlahan mulai menutup."
    play sound "audio/sfx/chapter 3/15.suara castle stone gate1.mp3"

    a "Waraa,{w=0.4} lihat pintu itu mulai tertutup"

    nr "Melihat itu, Wara langsung berlari lebih dahulu menuju pintu besar itu."
    play sound "audio/sfx/chapter 3/14.suaraa fast footsteps.mp3"
    nr "Ribuan jarum tajam terus mengejar mereka dari belakang dan suara retakan di sepanjang lorong makin keras terdengar."
    play sound "audio/sfx/chapter 3/12.suara earthquake split.mp3"
    nr "Sementara itu pintu besar di depan mereka juga mulai tertutup perlahan sedikit demi sedikit."
    play sound "audio/sfx/chapter 3/15.suara castle stone gate.mp3"

    scene bg_c3_pintu_tutup_1 with fade
    nr "Saat akhirnya sampai di depan pintu, Wara langsung menahan bagian pintu yang hampir tertutup itu menggunakan seluruh tenaga tubuhnya."
    
    k "cepet AS-LEEN!{w=0.8} masuk duluan!"

    scene bg_c3_pintu_tutup_2 with dissolve
    nr "AS-LEEN langsung masuk ke dalam, sementara Wara masih berusaha menahan pintu besar itu yang terus menekan tubuhnya."
    nr "Setelah memastikan AS-LEEN sudah aman di dalam, Wara buru-buru masuk sebelum akhirnya pintu itu tertutup keras di belakang mereka."
    play sound "audio/sfx/chapter 3/15.suara Massive gear movement.mp3"
    
    play sound "audio/backsound/Chapter 3/terjatuh.mp3"
    scene bg_c3_new_lawan_sengkuni with fade
    stop music fadeout 1.0
    nr "Tubuh Wara langsung terjatuh dan berguling beberapa kali di lantai keras karena dorongan pintu tadi."
    
    play sound "audio/sfx/chapter 3/14.suara heavy breathing.mp3"
    show k_normal at Position(xalign=0.5, yalign=0.3), napas_berat_repeat with dissolve
    k "Hufttt hampir aja jadi daging cincang"
    hide k_normal
    ## ── Munculnya Sengkuni ───────────────────────────────────

    nr "AS-LEEN segera mendekati Wara lalu membantunya agar bisa berdiri lagi."
    play sound "audio/sfx/chapter 3/7.suara soft cloth movement.mp3"
    nr "Saat Wara mengangkat kepalanya perlahan, ia langsung menyadari kalau ruangan itu jauh lebih aneh dibanding arena sebelumnya."
    nr "Suasana di tempat itu terasa tidak nyaman."
    nr "Semuanya terlihat palsu, seolah ruangan itu sengaja dibuat untuk mengacaukan pikiran siapa pun yang masuk ke dalamnya."

    $ _skipping = False
    nr "Lalu suara tepuk tangan pelan terdengar dari ujung ruangan."
    play sound "audio/backsound/Chapter 3/tepuk tangan slow.mp3"
    $ renpy.pause(5.0, hard=True)
    $ _skipping = True

    scene bg_c3_bertemu_sengkuni with dissolve
    play music "audio/backsound/Chapter 3/boss entrence.mp3" fadein 1.0
    queue music "audio/backsound/Chapter 3/boss entrence.mp3"
    sk "wahh… ternyata kalian berhasil masuk juga. Aku kira kalian sudah menjadi daging cincang seperti yang ku bayangkan."

    k "Jadi semua jebakan tadi ulah kamu?"
    
    $ _skipping = False
    play sound "audio/sfx/chapter 3/ketawa kejam.mp3"
    sk "(Ketawa kejam)"
    $ renpy.pause(1.0, hard=True)
    $ _skipping = True

    sk "Tentu saja.{w=0.7} lucu rasanya melihat orang berpikir mereka sudah hampir menang,"
    sk "Padahal sebenarnya mereka cuma sedang berjalan masuk ke jebakan yang sudah disiapkan sejak awal."

    nr "Wara langsung mendengarnya dan entah kenapa, suara Sengkuni terasa jauh lebih mengganggu dibanding boss yang sudah dikalahkan sebelumnya."

    a "Wara.. Hati-hati. Pola data miliknya tidak stabil."
    a "Kemungkinan besar dia menggunakan jebakan dan manipulasi sebagai pola utama serangannya."

    sk "Wahh wahh… AI kecil itu cukup pintar juga ternyata."

    nr "Sengkuni perlahan berdiri dari tempat duduknya."
    play sound "audio/sfx/chapter 3/12.suara earthquake split.mp3"
    nr "Di saat bersamaan, lantai arena mulai mengeluarkan retakan bercahaya ungu."

    pause 3.0

    play sound "audio/sfx/chapter 3/11.suara suspense drone.mp3"
    scene bg_c3_new_lawan_sengkuni with fade

    show sk_talk at Position(xalign=0.5, yalign=0.2), zoom_masuk with dissolve
    sk "Aku penasaran…{w=0.4} seberapa lama manusia seperti dirimu bisa tetap tenang sebelum emosinya memakan dirinya sendiri?"
    hide sk_talk

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "Aku gak dateng kesini buat denger omongan kosong kamu."
    hide k_angrytalk

    show sk_talk at Position(xalign=0.5, yalign=0.2) with dissolve
    sk "Oh ya?{w=1.0} tapi wajahmu gampang banget dibaca."
    sk "Sedikit dipancing langsung marah,{w=0.7} sedikit ditekan langsung panik,{w=0.7} manusia memang lucu ya."
    hide sk_talk

## ============================================================
##  BOSS FIGHT — SENGKUNI
## ============================================================

label boss_sengkuni_start:
    $ boss_attempts    += 1
    $ fase1_benar_c3   = 0
    $ fase2_benar_c3   = 0
    $ fase3_benar_c3   = 0

    scene bg_c3_new_lawan_sengkuni with dissolve
    stop music fadeout 0.5
    play music "audio/backsound/Chapter 3/entrence_boss_cut.mp3" fadein 0.5 fadeout 0.5

    $ _skipping = False
    show screen radar_roh_screen(level=2)
    $ renpy.pause(2.0, hard=True)
    $ _skipping = True

    $ _skipping = False
    show screen state_roh_screen("WASPADA")
    $ renpy.pause(2.0, hard=True)
    $ _skipping = True

    $ _skipping = False
    nr "── FASE 1: Kenali Jebakan Data ──"
    $ _skipping = True

    show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    a "Wara,{w=0.3} dia menyerang dengan data menjebak!"
    a "Jawab benar setiap soalnya, itu satu-satunya cara menghancurkan pertahanannya!"
    hide a_talk

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "Baik.{w=0.5} Aku tidak akan terpancing."
    hide k_angrytalk

## ────────────────────────────────────────────────────────────
##  SOAL 1 (UTAMA) — Python: Fungsi return a + b → 17
##  SOAL C1 (CADANGAN) — Python: elif, nilai=75 → 'B'
##
##  Benar  → lanjut soal 2 (utama)
##  Salah  → masuk soal C1 (cadangan)
##  C1 Benar  → lanjut soal 2 (utama)
##  C1 Salah  → ulang C1 (cadangan)
## ────────────────────────────────────────────────────────────

label c3_soal_1:
    show screen soal_panel(
        nomor="1",
        tema="Python – Fungsi",
        kode="17",
        pertanyaan="Manakah fungsi yang menghasilkan output tersebut saat dipanggil dengan hitung(10, 7)??"
    )

    menu:
        "return a * b":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "UGHHH— 10 dikali 7 itu 70, bukan 17!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Perkalian bukan jawabannya. 10 dikali 7 itu 70, bukan 17. Fokus, Wara!"
            hide a_talk
            jump c3_soal_1_cadangan

        "return a - b":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Pengurangan?! 10 dikurangi 7 itu 3, bukan 17. Salah!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Kurang tepat, Wara. Pengurangan menghasilkan 3, bukan 17. Kumpulkan fokusmu!"
            hide a_talk
            jump c3_soal_1_cadangan

        "return a + b":
            hide screen soal_panel
            $ fase1_benar_c3 += 1
            $ quiz_score_c3  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "PENJUMLAHAN! 10 ditambah 7 sama dengan 17!"
            k "Sekarang RASAKAN INI!"
            hide k_angrytalk
            play sound "audio/backsound/Chapter 3/Sword, stone-yoyosound.com.mp3"
            show sk_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            sk "GUH?! Tidak mungkin kau tahu…!"
            hide sk_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Bagus! Serangan pertama mengenai. Dia mulai goyah!"
            hide a_talk
            jump c3_soal_2

        "return a // b":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Floor division?! 10 dibagi 7 itu 1. Bukan 17!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "// adalah pembagian bulat ke bawah. Hasilnya 1, bukan 17. Kumpulkan fokusmu, Wara!"
            hide a_talk
            jump c3_soal_1_cadangan

label c3_soal_1_cadangan:
    show screen soal_panel(
        nomor="C1",
        tema="Python – Fungsi Return",
        kode="def kuadrat(x):\n    return x ** 2\n\nprint(kuadrat(3) + kuadrat(4))",
        pertanyaan="Apa output dari program tersebut?"
    )

    menu:
        "49":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Bukan 49! Itu bukan kuadrat dari 7, kita menjumlahkan kuadrat 3 dan 4!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Hitung dulu: kuadrat(3) = 9, kuadrat(4) = 16. Lalu jumlahkan!"
            hide a_talk
            jump c3_soal_1_cadangan

        "25":
            hide screen soal_panel
            $ fase1_benar_c3 += 1
            $ quiz_score_c3  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "25! kuadrat(3) = 9, kuadrat(4) = 16, dan 9 + 16 = 25!"
            k "Fokus kembali, Sengkuni tidak akan bisa menipuku!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Lanjutkan, Wara!"
            hide a_talk
            jump c3_soal_2

        "7":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "7 itu hasil 3+4, bukan kuadrat! Fungsinya mengembalikan x ** 2!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Perhatikan: return x ** 2 artinya pangkat dua, bukan penjumlahan biasa!"
            hide a_talk
            jump c3_soal_1_cadangan

        "14":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "14 itu 7 dikali 2! Ingat, ** 2 artinya dikuadratkan, bukan dikali 2!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "x ** 2 berarti x pangkat 2, bukan x dikali 2. Fokus, Wara!"
            hide a_talk
            jump c3_soal_1_cadangan

## ────────────────────────────────────────────────────────────
##  SOAL 2 (UTAMA) — Sejarah: Dampak krisis moneter 1997-1998
##  SOAL C2 (CADANGAN) — Sejarah: Kepanjangan KKN Reformasi 1998
##
##  Benar  → lanjut soal 3 / fase2
##  Salah  → masuk C2
##  C2 Benar  → lanjut fase2
##  C2 Salah  → ulang C2
## ────────────────────────────────────────────────────────────

label c3_soal_2:
    show screen soal_panel(
        nomor="2",
        tema="Sejarah – Reformasi",
        kode="",
        pertanyaan="Krisis moneter 1997–1998 berdampak sangat berat bagi Indonesia.\nSalah satu dampak langsungnya terhadap kehidupan masyarakat adalah…"
    )

    menu:
        "Harga kebutuhan pokok melonjak drastis akibat melemahnya rupiah":
            hide screen soal_panel
            $ fase1_benar_c3 += 1
            $ quiz_score_c3  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "Rupiah anjlok, harga barang pokok melonjak!"
            k "Rakyat yang menderita langsung. Ini tidak boleh dilupakan!"
            hide k_angrytalk
            play sound "audio/backsound/Chapter 3/Sword, stone-yoyosound.com.mp3"
            show sk_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            sk "NGHH— kau tahu sejarah negaramu sendiri?!"
            hide sk_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Rupiah dari Rp2.500 melonjak jadi Rp16.000 per dolar. Dua serangan sudah mengenai!"
            hide a_talk
            jump boss_sengkuni_fase2

        "Ekspor Indonesia meningkat pesat karena rupiah murah":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "SALAH! Memang ada efek itu tapi bukan dampak langsung ke masyarakat umum!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Pikirkan dampak yang paling dirasakan langsung oleh rakyat biasa, Wara. Fokus!"
            hide a_talk
            jump c3_soal_2_cadangan

        "Angka pengangguran turun karena pabrik beralih ke tenaga lokal":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Terbalik! Justru PHK besar-besaran yang terjadi!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Krisis justru membuat banyak perusahaan bangkrut dan PHK besar-besaran! Kumpulkan fokusmu!"
            hide a_talk
            jump c3_soal_2_cadangan

        "Indonesia mendapat banyak investasi asing karena harga aset murah":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Itu bukan dampak langsung ke rakyat! Salah arah!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Pikir dampak yang paling dirasakan rakyat biasa sehari-hari. Kumpulkan fokusmu, Wara!"
            hide a_talk
            jump c3_soal_2_cadangan

label c3_soal_2_cadangan:
    show screen soal_panel(
        nomor="C2",
        tema="Sejarah – Reformasi",
        kode="",
        pertanyaan="Salah satu tuntutan utama mahasiswa dalam gerakan Reformasi 1998\nadalah penegakan supremasi hukum dan pemberantasan KKN.\nKepanjangan KKN dalam konteks ini adalah…"
    )

    menu:
        "Korupsi, Kecurangan, dan Nepotisme":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Bukan Kecurangan! Huruf K yang kedua bukan itu!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Ingat tiga kata kunci Reformasi 1998. Huruf K kedua adalah Kolusi, bukan Kecurangan!"
            hide a_talk
            jump c3_soal_2_cadangan

        "Korupsi, Kolusi, dan Nepotisme":
            hide screen soal_panel
            $ fase1_benar_c3 += 1
            $ quiz_score_c3  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "Benar! KKN: Korupsi, Kolusi, dan Nepotisme — tiga musuh utama Reformasi!"
            k "Aku tidak akan menyerah, Sengkuni!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Bagus Wara! Kumpulkan tenaga, masih banyak yang harus dilalui!"
            hide a_talk
            jump boss_sengkuni_fase2

        "Kolusi, Kriminalitas, dan Nepotisme":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Kriminalitas bukan bagian dari KKN! Dan huruf K pertama adalah Korupsi!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "K pertama = Korupsi, bukan Kolusi. Dan tidak ada Kriminalitas di sana! Fokus, Wara!"
            hide a_talk
            jump c3_soal_2_cadangan

        "Korupsi, Kolusi, dan Normalisme":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Normalisme?! Kata itu bahkan tidak ada! N-nya adalah Nepotisme!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "N dalam KKN adalah Nepotisme — sikap pilih kasih kepada keluarga/kerabat. Baca soal lebih teliti!"
            hide a_talk
            jump c3_soal_2_cadangan

## ── FASE 2 ────────────────────────────────────────────────────

label boss_sengkuni_fase2:
    stop music fadeout 0.5
    play music "audio/backsound/Chapter 3/fase2.mp3" fadeout 0.5
    hide screen state_roh_screen

    play sound "audio/backsound/Chapter 3/liecio-noise-machine-190205.mp3"
    show effect_8 at truecenter with dissolve
    
    $ _skipping = False
    nr "── FASE 2: RAGE STATE — Sengkuni Mengamuk! ──"
    $ renpy.pause(1.0, hard=True)
    $ _skipping = True

    scene bg_c3_new_lawan_sengkuni with fade
    nr "Belum sempat Wara membalas, tiba-tiba puluhan jarum tajam langsung muncul dari lantai arena mengarah ke tubuhnya."

    play sound "audio/sfx/chapter 3/13.suara spike trap.mp3"

    show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    a "WARA AWASSS!!"
    hide a_talk

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "HAHH?!"
    hide k_angrytalk

    nr "Wara langsung menghindar sementara jarum-jarum itu menghantam lantai di belakangnya."
    nr "Wara langsung ke arah Sengkuni, namun tiba tiba tubuh Sengkuni menghilang menjadi serpihan data."

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "HAHH?!{w=1.0} APA APAAN INI???"
    hide k_angrytalk

    play sound "audio/backsound/Chapter 3/liecio-noise-machine-190205.mp3"
    show effect_3 at truecenter with dissolve
    $ renpy.pause(1.0, hard=True)
    scene bg_c3_sengkuni_hantam with dissolve

    nr "Dalam sekejap Sengkuni muncul lagi di belakang Wara sambil tertawa kecil."

    sk "Terlalu gampang dibaca."

    play sound "audio/sfx/chapter 3/14.suara heavy breathing.mp3"

    nr "Tendang Sengkuni langsung menghantam punggung Wara sampai tubuhnya terpental beberapa meter."

    play sound "audio/backsound/Chapter 3/terjatuh.mp3"

    scene bg_c3_new_lawan_sengkuni with fade

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "UGHHH!!"
    hide k_angrytalk

    show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    a "WARA!"
    hide a_talk

    nr "Wara menahan rasa sakitnya setelah di tendang Sengkuni."
    nr "Namun kali ini ia sadar sesuatu."
    nr "Semakin emosinya terpancing, semakin mudah Sengkuni membaca gerakannya."
    nr "Wara perlahan mengatur napasnya dan emosinya sambil menatap Sengkuni sambil kesal."

    show sk_talk at Position(xalign=0.5, yalign=0.2) with dissolve
    sk "Nahh…{w=0.5} itu dia wajah yang aku suka. semakin marah, semakin gampang ditebak."
    hide sk_talk

    show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    a "Wara,{w=0.3} jangan terpancing! perhatikan polanya dulu sebelum menyerang!"
    hide a_talk

## ────────────────────────────────────────────────────────────
##  SOAL 3 (UTAMA) — Python: List .append
##  SOAL C3 (CADANGAN) — Python: List Indexing data[1], data[-1], data[2]
##
##  Benar  → lanjut soal 4
##  Salah  → masuk C3
##  C3 Benar  → lanjut soal 4
##  C3 Salah  → ulang C3
## ────────────────────────────────────────────────────────────

label c3_soal_3:
    show screen soal_panel(
        nomor="3",
        tema="Python – List",
        kode="buah = ['apel', 'mangga', 'pisang']\nbuah.________('jeruk')\nprint(len(buah))",
        pertanyaan="Isi bagian ________ agar program mencetak 4."
    )

    menu:
        "add":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "add?! Python tidak punya metode .add() untuk list!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a ".add() itu untuk set, bukan list. Ingat metode yang tepat untuk list, Wara!"
            hide a_talk
            jump c3_soal_3_cadangan

        "insert":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "insert butuh dua argumen: indeks dan nilai. Tidak bisa seperti itu!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "insert(index, value) perlu dua argumen, bukan satu. Kumpulkan fokusmu, Wara!"
            hide a_talk
            jump c3_soal_3_cadangan

        "append":
            hide screen soal_panel
            $ fase2_benar_c3 += 1
            $ quiz_score_c3  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "APPEND! Menambahkan elemen ke akhir list!"
            k "Setelah append, panjang list jadi 4!"
            hide k_angrytalk
            play sound "audio/backsound/Chapter 3/Sword, stone-yoyosound.com.mp3"
            show sk_talk at Position(xalign=0.5, yalign=0.2), lompat_kaget with dissolve
            sk "GRAHHHH— Tidak mungkin kau tahu itu!"
            hide sk_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! .append() menambah elemen ke akhir list. Sengkuni mulai terhuyung!"
            hide a_talk
            jump c3_soal_4

        "push":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k ".push() tidak ada di Python! Bukan itu!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "push bukan metode Python. Ingat metode list yang benar! Kumpulkan fokusmu, Wara!"
            hide a_talk
            jump c3_soal_3_cadangan

label c3_soal_3_cadangan:
    show screen soal_panel(
        nomor="C3",
        tema="Python – List Indexing",
        kode="data = [10, 20, 30, 40, 50]\nprint(data[1])\nprint(data[-1])\nprint(data[2])",
        pertanyaan="Apa output dari program tersebut?"
    )

    menu:
        "10, 50, 30":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "data[1] bukan 10! Indeks Python mulai dari 0, jadi data[1] adalah elemen kedua!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Ingat: indeks dimulai dari 0. data[0]=10, data[1]=20. Perhatikan baik-baik!"
            hide a_talk
            jump c3_soal_3_cadangan

        "20, 50, 30":
            hide screen soal_panel
            $ fase2_benar_c3 += 1
            $ quiz_score_c3  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "20, 50, 30! data[1]=20, data[-1]=50 (terakhir), data[2]=30!"
            k "Aku bisa bangkit dari kesalahan, Sengkuni!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Bagus! tetap fokus, Wara!"
            hide a_talk
            jump c3_soal_4

        "10, 40, 30":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Dua jawaban salah! data[1] bukan 10, dan data[-1] bukan 40!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "data[1]=20 (indeks ke-1), data[-1]=50 (elemen terakhir). Perhatikan lagi!"
            hide a_talk
            jump c3_soal_3_cadangan

        "20, 40, 30":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "data[-1] bukan 40! Indeks negatif dihitung dari belakang, jadi data[-1] adalah elemen terakhir!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "data[-1] selalu menunjuk elemen terakhir list. List punya 5 elemen, yang terakhir adalah 50!"
            hide a_talk
            jump c3_soal_3_cadangan

## ────────────────────────────────────────────────────────────
##  SOAL 4 (UTAMA) — Sejarah: Dwifungsi ABRI
##  SOAL C4 (CADANGAN) — Sejarah: Tragedi Trisakti gelar mahasiswa
##
##  Benar  → lanjut fase3
##  Salah  → masuk C4
##  C4 Benar  → lanjut fase3
##  C4 Salah  → ulang C4
## ────────────────────────────────────────────────────────────

label c3_soal_4:
    show screen soal_panel(
        nomor="4",
        tema="Sejarah – Era Reformasi",
        kode="",
        pertanyaan="Penghapusan Dwifungsi ABRI pada era Reformasi berarti…"
    )

    menu:
        "Tentara dibubarkan dan digantikan oleh polisi nasional":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Bukan dibubarkan! TNI tetap ada sebagai kekuatan pertahanan!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Fokus pada perannya, bukan keberadaan TNI-nya. Kumpulkan fokusmu, Wara!"
            hide a_talk
            jump c3_soal_4_cadangan

        "Militer tidak lagi menjalankan peran sosial-politik dan fokus pada pertahanan":
            hide screen soal_panel
            $ fase2_benar_c3 += 1
            $ quiz_score_c3  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "Militer kembali ke fungsi pertahanan saja!"
            k "Tidak lagi campur tangan politik! Ini reformasi nyata!"
            hide k_angrytalk
            play sound "audio/backsound/Chapter 3/Sword, stone-yoyosound.com.mp3"
            show sk_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            sk "NGGHH— kau benar-benar tahu sejarahmu!"
            hide sk_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Benar! Dwifungsi memberi militer peran ganda. Penghapusannya kembalikan fokus ke pertahanan. Fase 2 hampir selesai!"
            hide a_talk
            jump boss_sengkuni_fase3

        "Anggota TNI diperbolehkan mendirikan partai politik sendiri":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Justru sebaliknya! Militer dijauhkan dari politik, bukan dibiarkan berpolitik!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Tujuan Reformasi justru memisahkan militer dari ranah politik! Kumpulkan fokusmu, Wara!"
            hide a_talk
            jump c3_soal_4_cadangan

        "Jabatan presiden tidak lagi bisa dijabat oleh perwira militer aktif":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Itu bukan inti dari Dwifungsi ABRI! Salah lagi!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Dwifungsi itu soal peran ganda militer, bukan soal jabatan presiden! Fokus, Wara!"
            hide a_talk
            jump c3_soal_4_cadangan

label c3_soal_4_cadangan:
    show screen soal_panel(
        nomor="C4",
        tema="Sejarah – Reformasi",
        kode="",
        pertanyaan="Tragedi Trisakti pada 12 Mei 1998 menewaskan empat mahasiswa\nUniversitas Trisakti saat demonstrasi.\nKeempat mahasiswa tersebut kemudian dianugerahi gelar…"
    )

    menu:
        "Pahlawan Nasional":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Bukan Pahlawan Nasional! Gelar itu berbeda konteksnya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Pikirkan gelar yang sesuai dengan konteks perjuangan mereka di era 1998!"
            hide a_talk
            jump c3_soal_4_cadangan

        "Pahlawan Reformasi":
            hide screen soal_panel
            $ fase2_benar_c3 += 1
            $ quiz_score_c3  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "Benar! Pahlawan Reformasi! Pengorbanan mereka mendorong Soeharto mundur!"
            k "Sejarah adalah senjataku!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Teruskan perjuangan, Wara!"
            hide a_talk
            jump boss_sengkuni_fase3

        "Pahlawan Kemerdekaan":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Pahlawan Kemerdekaan itu untuk era 1945! Ini konteks 1998!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Konteks waktunya beda jauh, Wara! Mereka berjuang di era Reformasi!"
            hide a_talk
            jump c3_soal_4_cadangan

        "Pahlawan Revolusi":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Pahlawan Revolusi itu untuk korban G30S 1965! Salah era!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Pahlawan Revolusi untuk korban G30S/PKI. Yang ini konteks Reformasi 1998!"
            hide a_talk
            jump c3_soal_4_cadangan

## ── FASE 3 (Terakhir) ─────────────────────────────────────────

label boss_sengkuni_fase3_retry:
    $ fase3_benar_c3 = 0
    hide screen timer_screen
    hide screen radar_roh_screen
    hide screen state_roh_screen
    hide screen soal_panel
    hide screen soal_panel

    scene bg_c3_new_lawan_sengkuni with dissolve

    show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    a "Kita masih bisa, Wara.{w=0.4} Sengkuni sudah lemah—tinggal fase terakhir!"
    hide a_talk

label boss_sengkuni_fase3:
    stop music fadeout 0.5
    play music "audio/backsound/Chapter 3/fase3.mp3" fadein 1.0
    hide screen state_roh_screen
    show screen state_roh_screen("marah")
    pause 1.0
    
    $ _skipping = False
    play sound "audio/backsound/Chapter 3/liecio-noise-machine-190205.mp3"
    show effect_3 at truecenter with dissolve
    $ renpy.pause(1.0, hard=True)
    $ _skipping = True

    $ _skipping = False
    nr "── FASE 3: ENRAGED MODE — Chaos Pressure! ──"
    $ _skipping = True

    scene bg_c3_new_lawan_sengkuni with dissolve

    nr "Kali ini Wara tidak langsung menyerang."
    nr "Ia memilih diam sambil memperhatikan gerakan Sengkuni pelan-pelan."

    nr "Dan beberapa saat kemudian Wara mulai sadar,"
    nr "Setiap Sengkuni berpindah tempat selalu ada jeda kecil seperti glitch yang muncul sesaat sebelum tubuhnya muncul kembali di tempat lain."

    show k_angry at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Dalam hati)"
    k "Jadi itu caranya…{w=1.0} dia bukan benar-benar menghilang."
    k "Tetapi, dia cuman pindah posisi lewat data."
    hide k_angry

    nr "Sengkuni kembali muncul di samping Wara lalu menyerang cepat. Namun kali ini Wara langsung menahan serangannya."

    play sound "audio/backsound/Chapter 3/Sword, stone-yoyosound.com.mp3"
    
    play sound "audio/backsound/Chapter 3/liecio-noise-machine-190205.mp3"
    show effect_3 at truecenter with dissolve
    $ renpy.pause(1.0, hard=True)
    scene bg_c3_wara_serang with dissolve

    sk "Hahh??!"

    nr "Wara langsung menghantam tubuh Sengkuni tepat saat glitch itu muncul lagi."

    play sound "audio/backsound/Chapter 3/Sword, stone-yoyosound.com.mp3"

    nr "Retakan besar langsung muncul di tubuh Sengkuni."

    scene bg_c3_new_lawan_sengkuni with dissolve

    show sk_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
    sk "AGHH tidak mungkin"
    hide sk_talk

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "Udah selesai main jebak-jebakkannya?"
    hide k_angrytalk

## ────────────────────────────────────────────────────────────
##  SOAL 5 (UTAMA) — Python: sum()+len() [TIMER]
##  SOAL C5 (CADANGAN) — Python: List Slicing angka[1:4] dan angka[:3]
##
##  Benar  → lanjut soal 6
##  Salah  → masuk C5
##  C5 Benar  → lanjut soal 6
##  C5 Salah  → ulang C5
## ────────────────────────────────────────────────────────────

label c3_soal_5:
    show screen timer_screen(length=25.0, on_timeout="waktu_habis_boss_c3")
    show screen soal_panel(
        nomor="5",
        tema="Python – Fungsi & List",
        kode="def total(data):\n    return sum(data)\n\nangka = [10, 20, 30, 40]\nprint(total(angka))\nprint(len(angka))",
        pertanyaan="Apa output dari program tersebut?"
    )

    menu:
        "100 dan 3":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "AUGH— len itu menghitung elemen, ada 4 elemen bukan 3!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Hitung ulang! [10,20,30,40] punya berapa elemen? Fokus, Wara!"
            hide a_talk
            jump c3_soal_5_cadangan

        "100 dan 4":
            hide screen timer_screen
            hide screen soal_panel
            $ fase3_benar_c3 += 1
            $ quiz_score_c3  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "sum dari [10,20,30,40] adalah 100!"
            k "dan len-nya adalah 4 karena ada 4 elemen!"
            k "SERANG SENGKUNI!!"
            hide k_angrytalk
            play sound "audio/backsound/Chapter 3/Sword, stone-yoyosound.com.mp3"
            show sk_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            sk "GRAAAHHHH— Tidak MUNGKIN!"
            hide sk_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Satu pukulan lagi, Wara. Akhiri dia sekarang!"
            hide a_talk
            jump c3_soal_6

        "40 dan 4":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "40 itu nilai terakhir, bukan jumlah total!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "sum() menjumlahkan semua elemen, bukan mengambil nilai terakhir! Kumpulkan fokusmu, Wara!"
            hide a_talk
            jump c3_soal_5_cadangan

        "10 dan 4":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "10 itu nilai pertama saja! sum() menjumlahkan semuanya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Jumlahkan semua: 10+20+30+40. Pikirkan baik-baik, Wara!"
            hide a_talk
            jump c3_soal_5_cadangan

label c3_soal_5_cadangan:
    show screen timer_screen(length=25.0, on_timeout="waktu_habis_boss_c3")
    show screen soal_panel(
        nomor="C5",
        tema="Python – List Slicing",
        kode="angka = [1, 2, 3, 4, 5, 6]\nprint(angka[1:4])\nprint(angka[:3])",
        pertanyaan="Apa output dari program tersebut?"
    )

    menu:
        "[2, 3, 4] dan [1, 2, 3]":
            hide screen timer_screen
            hide screen soal_panel
            $ fase3_benar_c3 += 1
            $ quiz_score_c3  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "(2,3,4) dan (1,2,3)! angka(1:4) ambil indeks 1 s/d 3, angka(:3) ambil tiga pertama!"
            k "Aku bisa pulih dan bangkit!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Bagus! Lanjut ke soal terakhir!"
            hide a_talk
            jump c3_soal_6

        "[1, 2, 3] dan [1, 2, 3]":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "angka(1:4) mulai dari indeks 1 (nilai 2), bukan indeks 0!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Ingat: indeks mulai dari 0. angka(1:4) = elemen di indeks 1,2,3 = (2,3,4)!"
            hide a_talk
            jump c3_soal_5_cadangan

        "[2, 3, 4] dan [2, 3, 4]":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "angk(:3) mulai dari awal (indeks 0), jadi hasilnya (1,2,3) bukan (2,3,4)!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "angka():3) artinya dari awal hingga indeks 2. Itu adalah (1,2,3)!"
            hide a_talk
            jump c3_soal_5_cadangan

        "[2, 3, 4, 5] dan [1, 2, 3]":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "angka(1:4) berhenti sebelum indeks 4 (nilai 5 tidak masuk)!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Slicing (start:stop) tidak termasuk indeks stop. angka(1:4) = (2,3,4) saja!"
            hide a_talk
            jump c3_soal_5_cadangan

## ────────────────────────────────────────────────────────────
##  SOAL 6 – TERAKHIR (UTAMA) — Sejarah: ciri Era Reformasi [TIMER]
##  SOAL C6 (CADANGAN) — Sejarah: Sidang Istimewa MPR Agustus 1998
##
##  Benar  → boss_sengkuni_menang
##  Salah  → masuk C6
##  C6 Benar  → boss_sengkuni_menang
##  C6 Salah  → ulang C6
## ────────────────────────────────────────────────────────────

label c3_soal_6:
    show screen timer_screen(length=25.0, on_timeout="waktu_habis_boss_c3")
    show screen soal_panel(
        nomor="6 – TERAKHIR",
        tema="Sejarah – Era Reformasi",
        kode="",
        pertanyaan="Penghapusan Dwifungsi ABRI, kebebasan pers, dan pemilu\nmultipartai adalah ciri khas era…"
    )

    menu:
        "Demokrasi Liberal (1950–1959)":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "SALAH— Liberal itu era 50-an, bukan konteks Dwifungsi ABRI!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Dwifungsi ABRI ada di era Orde Baru. Yang menghapusnya datang setelahnya! Fokus, Wara!"
            hide a_talk
            jump c3_soal_6_cadangan

        "Orde Lama (1945–1966)":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Orde Lama?! Bukan— Dwifungsi ABRI belum ada saat itu!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Orde Lama era Soekarno. Dwifungsi itu produk Soeharto, bukan Soekarno! Kumpulkan fokusmu!"
            hide a_talk
            jump c3_soal_6_cadangan

        "Orde Baru (1966–1998)":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Orde Baru yang menciptakan Dwifungsi, bukan yang menghapusnya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Yang menghapusnya adalah era setelah Orde Baru. Pikirkan baik-baik, Wara!"
            hide a_talk
            jump c3_soal_6_cadangan

        "Reformasi (1998–sekarang)":
            hide screen timer_screen
            hide screen soal_panel
            $ fase3_benar_c3 += 1
            $ quiz_score_c3  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "REFORMASI! Era yang menghapus Dwifungsi, membuka kebebasan pers,"
            k "dan memungkinkan pemilu multipartai!"
            k "INI SERANGANKU YANG TERAKHIR UNTUKMU, SENGKUNI!!!"
            hide k_angrytalk
            play sound "audio/backsound/Chapter 3/Sword, stone-yoyosound.com.mp3"
            jump boss_sengkuni_menang

label c3_soal_6_cadangan:
    show screen timer_screen(length=25.0, on_timeout="waktu_habis_boss_c3")
    show screen soal_panel(
        nomor="C6",
        tema="Sejarah – Reformasi",
        kode="",
        pertanyaan="Sidang Istimewa MPR pada bulan Agustus 1998\nyang dipimpin oleh Harmoko menghasilkan keputusan penting, yaitu…"
    )

    menu:
        "Pembekuan partai-partai Orde Baru":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Sidang Istimewa tidak membekukan partai! Salah!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Pikirkan apa agenda terpenting yang dihasilkan dari sidang itu, Wara!"
            hide a_talk
            jump c3_soal_6_cadangan

        "Penolakan pidato pertanggungjawaban Soeharto dan pengangkatan B.J. Habibie":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Soeharto sudah mundur dan Habibie dilantik pada 21 Mei 1998, sebelum Sidang Istimewa!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "Urutan waktunya penting! Habibie sudah jadi presiden saat sidang itu. Fokus!"
            hide a_talk
            jump c3_soal_6_cadangan

        "Pembentukan Komisi Pemberantasan Korupsi (KPK)":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "KPK dibentuk jauh setelahnya, bukan di Sidang Istimewa 1998!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            a "KPK baru terbentuk tahun 2002-2003. Bukan hasil Sidang Istimewa 1998! Kumpulkan fokusmu!"
            hide a_talk
            jump c3_soal_6_cadangan

        "Penetapan agenda Pemilu 1999 yang bebas dan adil":
            hide screen timer_screen
            hide screen soal_panel
            $ fase3_benar_c3 += 1
            $ quiz_score_c3  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "Benar! Sidang Istimewa MPR 1998 menetapkan agenda Pemilu 1999 yang bebas dan adil!"
            k "Ini pukulan terakhirku untukmu Sengkuni!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Sekarang HABISI DIA!"
            hide a_talk
            jump boss_sengkuni_menang

## ── SENGKUNI KALAH ────────────────────────────────────────────

label boss_sengkuni_menang:
    hide screen radar_roh_screen
    hide screen timer_screen
    hide screen state_roh_screen
    stop music fadeout 0.5

    scene bg_c3_wara_serang with dissolve
    play sound "audio/backsound/Chapter 3/Sword, stone-yoyosound.com.mp3"

    nr "Wara kembali meluncurkan serangan terakhirnya tepat ke inti tubuh Sengkuni."

    sk "AGHHHH tidak mungkin"

    play sound "audio/backsound/Chapter 3/liecio-noise-machine-190205.mp3"
    show effect_3 at truecenter with dissolve
    $ renpy.pause(1.0, hard=True)
    scene bg_c3_sengkuni_kalah with dissolve

    play sound "audio/backsound/Chapter 3/nastelbom-intense-453507.mp3" fadein 0.5
    nr "Tubuh Sengkuni langsung hancur menjadi serpihan ungu yang perlahan menghilang dari arena."
    nr "Arena akhirnya kembali sunyi setelah tubuh Sengkuni hancur menjadi serpihan ungu yang perlahan menghilang di udara."


    k "Huhhhft,{w=0.6} akhirnya selesai juga…"
    $ renpy.pause(1.0, hard=True)

    stop sound fadeout 1.0

    scene bg_c3_new_lawan_sengkuni with dissolve
    ## ── Jebakan Terakhir Sengkuni: Racun ─────────────────────
    nr "Baru saja mereka ingin melanjutkan perjalanan, tiba-tiba terdengar suara kecil dari dinding tepat di depan Wara."
    play sound "audio/sfx/chapter 3/13suara. sharp projectile.mp3"
    pause 1.0
    nr "Dalam sekejap, sebuah jarum panjang langsung melesat cepat ke arah tubuh Wara."
    nr "Di ujung jarum itu terdapat cairan hitam pekat yang bergerak aneh seperti racun hidup."

    play sound "audio/sfx/chapter 3/13.suara Metal slicing air.mp3"

    show a_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    a "WARA!!!"
    hide a_talk

    nr "Tanpa pikir panjang AS-LEEN langsung menghadang jarum itu dengan tubuhnya sendiri."

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "AS-LEEN!!"
    hide k_angrytalk

    pause 1.0

    scene bg_c3_asleen_racun with dissolve
    play music "audio/backsound/Chapter 3/(5) ASLEEN_TERKENA_RACUN__ENDING_DIGENDONG.mp3" fadein 0.5
    play sound "audio/sfx/chapter 3/14.suara heavy breathing.mp3"
    nr "Jarum itu menancap di lengan AS-LEEN."
    nr "Cairan hitamnya langsung menyebar pelan seperti glitch gelap di tubuhnya."
    nr "Cahaya di tubuh AS-LEEN mulai berkedip tidak stabil."
    nr "Wara langsung menahan tubuh AS-LEEN sebelum jatuh."

    scene bg_c3_new_asleen_racun with dissolve

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "AS-LEEN?!"
    k "Jadi ini jebakan terakhir si Sengkuni…"
    hide k_angrytalk

    show a_poisoned_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    play sound "audio/sfx/chapter 3/14.suara heavy breathing.mp3"
    a "Iyaa Waraa, sepertinya cairan itu adalah corrupt poison."
    a "Jika menyebar terlalu jauh, data dalam tubuhku bisa rusak sedikit demi sedikit."
    hide a_poisoned_talk
    stop sound

    nr "Wara langsung melihat glitch hitam yang perlahan bergerak di lengan AS-LEEN."
    nr "Wajahnya mulai terlihat khawatir."

    show k_think at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "Kalau data kamu rusak… berarti…"
    hide k_think

    play sound "audio/sfx/chapter 3/14.suara heavy breathing.mp3"
    show a_poisoned_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Kemungkinan terburuknya… kamu tidak akan bisa melihatku lagi."
    hide a_poisoned_talk
    stop sound

    nr "Untuk sesaat Wara langsung terdiam."

    show k_normal at Position(xalign=0.5, yalign=0.3) with dissolve
    k "terus gimana cara ngobatinnya? pasti masih ada cara kan...?"
    hide k_normal

    nr "AS-LEEN memejamkan matanya beberapa detik seperti membaca sesuatu dari sistemnya sendiri."

    play sound "audio/backsound/Chapter 3/ai scanning.mp3"
    pause 2.0

    show a_poisoned_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Masih ada cara menetralkannya."
    a "Ada bunga anggrek data di area berikutnya… bunga itu bisa menghentikan corrupt poison ini."
    hide a_poisoned_talk

    show k_normal at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "Yasudah,{w=0.3} kita cari sekarang."
    hide k_normal

    nr "AS-LEEN mencoba berjalan sendiri, namun tubuhnya sedikit goyah."
    nr "Wara langsung membalikkan tubuhnya lalu jongkok di depan AS-LEEN."

    scene bg_c3_asleen_menghampiri_untuk_digendong with dissolve
    k "Udah,{w=0.3} sini naik aja."
    k "Aku gak mau kondisi kamu makin parah gara-gara dipaksa jalan sendiri."

    a "B-baiklah."

    scene bg_c3_gendong with dissolve
    play sound "audio/sfx/chapter 3/7.suara soft cloth movement.mp3"

    nr "Wara langsung menggendong AS-LEEN di punggungnya lalu mengikat tubuhnya menggunakan kain panjang agar tetap aman selama perjalanan."
    nr "Setelah itu Wara kembali melangkah masuk ke lorong berikutnya sambil membawa AS-LEEN di punggungnya,"
    nr "sementara glitch hitam di lengan AS-LEEN perlahan terus menyebar sedikit demi sedikit."

    jump chapter3_ending

## ── Waktu Habis ──────────────────────────────────────────────

label waktu_habis_boss_c3:
    hide screen timer_screen
    hide screen radar_roh_screen
    hide screen state_roh_screen
    hide screen soal_panel
    hide screen soal_panel
    $ renpy.block_rollback()

    call screen kalah_boss_screen()

    if _return == "restart":
        jump boss_sengkuni_fase3_retry
    else:
        jump chapter_select_screen

## ── Chapter 3 Ending ─────────────────────────────────────────

label chapter3_ending:
    stop music fadeout 1.5
    stop sound fadeout 1.0
    scene bg_c3_gendong with dissolve
    play music "audio/backsound/Chapter 3/paulyudin-romantic-dreams-155789.mp3" fadein 2.0

    nr "── CHAPTER 3 SELESAI ──"
    nr "\"Jebakan di Balik Ketenangan\""

    nr "AS-LEEN terluka. Perjalanan Kreswara semakin berat."
    nr "Boss berikutnya: Duryodana — Penguasa Terakhir Dunia Hybrid."
    nr "Sampai jumpa di Chapter 4: Master Sejati."

    pause 1.5
    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    pause 1.0

    $ persistent.chapter3_unlocked = True
    $ persistent.chapter4_unlocked = True
    $ renpy.full_restart()