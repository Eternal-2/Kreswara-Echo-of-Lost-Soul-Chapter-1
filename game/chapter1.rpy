label chapter1_full:

    scene bg_desa_siang with dissolve
    play music "audio/backsound/Chapter 1/[Scene Suasana Desa].mp3" fadein 2.0
    play sound "audio/sfx/chapter 1/1.suara jangkrik.mp3" loop

    nr "Suasana langit jingga menerpa kehangatannya ke sebuah desa kecil yang selalu dialiri tawa semua jiwa di sana, baik tua maupun muda."
    nr "Tak terkecuali seorang pemuda menawan yang tubuhnya penuh kepuasan batin setelah melepas penat"
    nr "saat kakinya sekali lagi mengantarkannya ke rumahnya: sang bunda tercinta."

    show ibu_k at Position(xalign=0.5, yalign=0.3) with dissolve
    i "Waraaa. Pulang nak, udah hampir malem."
    hide ibu_k

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Tersenyum)"
    hide k_smile

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Iya bu."
    hide k_talk
    
    stop sound

    scene bg_ruangan_malam with dissolve
    play music "audio/backsound/Chapter 1/Chapter 1 Scene rumah kreswara saat malam hari.mp3" fadein 1.5
    play sound "audio/sfx/chapter 1/2.suara ambience rumah malam.mp3" loop

    show bpk_k at Position(xalign=0.5, yalign=0.1), napas_berat with dissolve
    b "(Sedikit marah)"
    b "Kreswara Radyana. Kan sudah bapak bilang beberapa kali"
    b "dirimu ini cukup diam di desa, hidup enak di sini,"
    b "dan jangan membujuk bapak dengan idemu itu lagi!"
    hide bpk_k

    show k_talk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "(Kecewa)"
    k "T-tapi pak..."
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
    play music "audio/backsound/Chapter 1/choise_pasrahmarah.mp3" fadein 1.0
    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Kecewa)"
    k "I-iya pak.... Wara ngerti."
    hide k_talk
    show bpk_k at Position(xalign=0.5, yalign=0.1) with dissolve
    b "Bagus kalau kau ngerti."
    hide bpk_k
    jump scene_kamar


label pilihan_marah:
    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "TAPI WARA CAPEK PAK NGIKUTIN EGO BAPAK TERUS!"
    k "WARA PUN PENGEN PUNYA KEINGINAN BUAT HIDUP WARA SENDIRI!!"
    hide k_angrytalk

    show bpk_k at Position(xalign=0.5, yalign=0.1), getar with dissolve
    play sound "audio/sfx/chapter 1/3.suara tamparan.mp3"
    b "DASAR ANAK GATAU DIRI."
    b "BAPAK SUDAH CAPEK-CAPEK BEKERJA DAN SEKARANG KAMU DENGAN LANTANGNYA"
    b "MINTA HAL YANG BAPAK GAK SETUJUI."
    b "BALIK SEKARANG KE KAMARMU, CEPAT!!"
    hide bpk_k
    jump scene_kamar

label scene_kamar:
    stop sound
    scene bg_ruangan_malam with fade
    play music "audio/backsound/Chapter 1/Memperlihatkan_Laptop_Kreswara.mp3" fadein 1.5
    play sound "audio/sfx/chapter 1/1.suara langkah kaki di tanah.mp3"
    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Gatau aja dia aku sudah ngumpulin uang buat beli laptop."
    hide k_smile

    scene bg_desa_siang with fade
    play music "audio/backsound/chapter 1/[Scene Suasana Desa].mp3"
    play sound "audio/sfx/chapter 1/4.suara kenalpot nyala.mp3"
    
    nr "Cahaya matahari yang memancarkan panas kemegahannya hari ini menjadi tumpuan Kreswara untuk membuat pilihan tersembunyinya."
    nr "Suara deru knalpot motor temannya mengantarnya ke rumah kenalan yang bersedia membantu."

    stop sound
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

    scene bg_cod with fade
    play sound "audio/sfx/chapter 1/4.suara motor nyala.mp3"

    d "Halah ada-ada aja lu hahaha."
    d "Yaudeh, hati-hati ya baliknya."
    
    k "Iya, makasih ya sekali lagi."

    stop sound

    scene bg_ruangan_siang with fade
    play music "audio/backsound/Chapter 1/Panggung_dekat_rumah_Kreswara__pertunjukkan.mp3" fadein 1.5
    play sound "audio/sfx/chapter 1/1.suara orang berbincang.mp3"
    play sound "audio/sfx/chapter 1/1.suara langkah kaki di tanah.mp3"
    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Mantap banget laptopnya udah aku dapat!"
    k "Ga sabar ingin cepat-cepat mencoba semua hal yang sudah kupelajari."
    hide k_smile

    stop sound
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

    scene bg_panggung with fade
    nr "Suasana panggung temaram di bawah lampu redup—menambah kesan kuat akan pementasan yang sebentar lagi akan berjalan."
    nr "Para wayang masih tergeletak rapi, belum ditancapkan ke gedebog pisang."

    stop sound
    play sound "audio/sfx/chapter 1/5.suara gesekan wayang.mp3"

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

    scene bg_panggung_khusus with fade

    play music "audio/backsound/Chapter 1/scene pertunjukan wayang chapter 1.mp3" fadein 1.0
    play sound "audio/sfx/chapter 1/6.suara tepuk tangan dan suara.mp3"

    k "Seperti biasa, Bapak sangat jago menjadi Dalang."
    k "Melihat hal ini membuatku menyadari suatu hal:"
    k "aku sangat mencintai seni yang ada di keluargaku ini—"
    k "tapi aku juga menyukai saat bisa melakukan apapun dengan baris kode yang setiap malam kupelajari."

    stop sound

    nr "Singkat cerita, pertunjukan wayang sudah selesai digelar."

    stop music fadeout 1.0

    scene bg_ruangan_malam with fade
    play music "audio/backsound/Chapter 1/Panggung_dekat_rumah_Kreswara__pertunjukkan.mp3"
    play sound "audio/sfx/chapter 1/2.suara ambience rumah malam.mp3"
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

    play sound "audio/sfx/chapter 1/4.suara motor nyala.mp3"

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Iya pak, hati-hati di jalan."
    hide k_talk

    stop sound

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Gatau aja aku bakal main laptop semalaman ini hehe."
    hide k_smile

    nr "Kekosongan rumah yang merekah ke setiap sudut menandakan waktu kebebasan semu untuk Kreswara menyentuh apa yang dia tunggu dari tempo lalu."

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Akhirnyaa...."
    hide k_talk

    play sound "audio/sfx/chapter 1/4.suara buka tas.mp3"

    nr "Sebuah laptop yang siapapun melihatnya pasti menyadari ia sudah cukup sering berpindah tangan."
    nr "Sebuah jejak teknologi mengukuhkan kehadirannya di antara pemuda dan gerbang tradisional yang melekat dalam dirinya—"
    nr "membuat ledakan emosi kecil tentang bagaimana semua impian Kreswara akhirnya memperlihatkan jalannya."

    play sound "audio/sfx/chapter 1/7.suara laptop menyala.mp3"

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Oke... kita lihat isi dalemnya."
    hide k_talk

    nr "Folder dibuka satu-satu. Ada yang biasa, ada yang aneh. Sampai satu file bikin Kreswara berhenti."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "'darul_baka.exe'?"
    hide k_think

    show k_normal at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Namanya kayak bukan program biasa."
    hide k_normal

    play sound "audio/sfx/chapter 1/8.suara klik.mp3"

    nr "..."
    nr "Tidak terjadi apa-apa."
    nr "Tiba-tiba...."

    scene black

    show bg_ruangan_malam at efek_kedap_kedip

    pause 1.0

    play sound "audio/sfx/chapter 1/8.suara listrik 1.mp3"
    play music "audio/backsound/Chapter 1/Aktivasi_gagal.mp3" fadein 0.5

    nr "Layar tiba-tiba berkedip. Lampu rumah ikut goyang."

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "Hah? Kenapaa iniii???!!"
    hide k_angrytalk

    scene bg_ruangan_malam with dissolve

    stop music

    play music "audio/backsound/Chapter 1/WAYANG_BERGERAK__BENANG_LISTRIK__WAYANG_HILANG.mp3" fadein 0.5 

    play sound "audio/sfx/chapter 1/8.suara listrik 1.mp3"
    play sound "audio/sfx/chapter 1/8.suara static noise.mp3"

    nr "Sambaran listrik mengaumkan kehadirannya ke seluruh ruangan—"
    nr "sangat cepat sampai yang bisa dipikirkan Kreswara hanyalah: 'MUNDUR!'"

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "WOI WOI WOI!!"
    hide k_angrytalk

    nr "Putaran energi itu terjadi beriringan dengan tarian menyeramkan yang mengalir ke dinding panggung—"
    nr "melebarkan genggaman volt panasnya, lalu berhenti di satu titik yang tak pernah Kreswara sangka"

    nr "Rak wayang."
    play sound "audio/sfx/chapter 1/5.suara boneka yang di tancapkan pada pohon pisang.mp3"

    nr "Wayang mulai bergerak. Benang tak terlihat penuh aliran listrik mengikat mereka."
    nr "Satu naik, dua ikut, semuanya pelan-pelan terangkat."
    stop sound

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "(Panik)"
    k "HEY!! JANGAN!!"
    hide k_angrytalk

    nr "Wayang Hilang."
    nr "Rak terakhir yang kebetulan Kreswara sentuh sekarang terasa kosong."

    stop sound
    stop sound

    scene bg_ruangan_malam with fade
    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Bingung)"
    k "Duh... barusan aku ngapain sih..."
    k "Wayang bapak... ada yang ilang..."
    hide k_think

    stop music

    play music "audio/backsound/Chapter 1/asleen berwujud.mp3" fadein 1.0
    play sound "audio/sfx/chapter 1/8.suara glitch digital.mp3"

    show a_siluet at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Pengguna terdeteksi."
    hide a_siluet

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "(Shock)"
    k "HAH?! SIAPA ITU?!"
    k "Apa ada saksi yang lihat semuanya?!"
    hide k_angrytalk

    nr "....."

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Pastinya engga lah wara"
    k "Jam segini warga desa pasti sudah tidur lelap semua..."
    hide k_talk

    show a_siluet at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Tenang. Saya tidak berbahaya."
    hide a_siluet

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "...."
    hide k_angrytalk

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Kamu dari mana sih?!"
    k "Coba muncul dulu atuh!"
    hide k_think

    show a_siluet at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Saya aktif setelah lonjakan energi tadi."
    a "Tepatnya 7 menit 56 detik yang lalu."
    hide a_siluet

    nr "Kreswara langsung diam. Matanya ke laptop, lalu ke seluruh pojok ruangan, tidak menemukan sumber suara."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Sepertinya program yang tadi bukanlah sekadar hal yang normal..."
    k "Wayang itu... ke mana?"
    hide k_think

    show a_siluet at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Ada. Tidak hilang."
    a "Mereka hanya berpindah ke dunia hybrid-virtual."
    a "Hal yang tentunya tidak bisa kau lihat. Untuk saat ini."
    hide a_siluet

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "...dan sekarang aku harus ngapain?"
    hide k_talk

    show a_siluet at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Mengambilnya kembali."
    hide a_siluet

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "o-oke... Caranya?"
    hide k_talk

    show a_siluet at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Dengan masuk ke sana. Tentu saja."
    hide a_siluet

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Senyum kecil, setengah nekat setengah kesal)"
    k "Yaudah... masukin aja langsung."
    hide k_smile

    show a_siluet at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Tidak bisa."
    hide a_siluet

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "Terus harus gimana sih?! Serba salah!"
    hide k_angrytalk

    show a_siluet at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Kamu harus membuat perangkat bernama PUPILS."
    hide a_siluet

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "PUPILS...? Sejenis bagian yang ada di mata?"
    k "...Seriusan harus bikin sendiri?"
    hide k_think

    show a_siluet at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Ya. Gunakan yang ada di sekitarmu. Penglihatan kamu masih bekerja kan?"
    hide a_siluet

    show k_angry at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Nyebelin..."
    hide k_angry

    show a_siluet at Position(xalign=0.5, yalign=0.3) with dissolve
    nr "Kreswara memeriksa sekitar rumah dan panggung."
    hide a_siluet

    scene bg_rakit_pupils with dissolve

    a "Siapkan helm bekas sebagai struktur utama."
    a "Tambahkan kardus atau plastik keras di bagian samping dan belakang."
    a "Buat bagian belakang sebagai inti sistem."

    k "(Sudah mulai mengambil barang)"
    k "Oke... lanjut."

    a "Tambahkan kotak kecil sebagai modul inti."
    a "Sambungkan kabel dari modul ke bagian depan dan samping. Biarkan terbuka, tidak perlu rapi."

    nr "Tangannya langsung bergerak cepat. Seperti sudah menjadi kebiasaannya sehari-hari."

    a "Pasang busa di dalam helm, lalu tambahkan kawat atau logam di sisi kepala sebagai sensor."
    a "Tambahkan earphone atau visor di depan."
    a "Jangan lupa beri tanda seperti 'SYNC' atau 'NODE'."

    nr "Beberapa menit berlalu. Helm itu sekarang sudah tak berbentuk helm biasa lagi."

    scene bg_ruangan_malam with dissolve
    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Senyum puas)"
    hide k_smile

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Huftt... akhirnya selesai juga..."
    hide k_talk

    play sound "audio/sfx/chapter 1/8.suara klik.mp3"

    nr "Tidak ada reaksi."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Bingung)"
    hide k_think

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Loh? Kok ga nyala?"
    hide k_talk

    show a_siluet at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Karena saya masih di dalam sistem lama."
    a "Saya harus dipindahkan ke PUPILS."
    hide a_siluet

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Jadi aku harus mindahin kamu ke helm?"
    hide k_talk

    show a_siluet at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Benar! Agar saya bisa menjadi inti sistem dan membimbingmu langsung di dunia hybrid."
    a "Gunakan komputer dengan koneksi lebih stabil."
    hide a_siluet

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(Berpikir) Di mana tempat aku untuk melakukan itu?... Aku tau!"
    hide k_think

    scene bg_desa_malam with fade
    play music "audio/backsound/Chapter 1/perpustakaan_desa.mp3" fadein 1.5

    nr "Kreswara berjalan mengelilingi desa, lalu sampai di perpustakaan desa."
    play sound "audio/sfx/chapter 1/2.suara pintu.mp3"

    scene bg_perpus with fade

    nr "Komputer yang terlihat usang itu menyala—namun Kreswara tidak bisa langsung mengaksesnya."
    nr "Ia membutuhkan sandi untuk mengakses komputer."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Hmm... ada password komputer. Tapi aku punya cara untuk masuk."
    hide k_think

    play sound "audio/sfx/chapter 1/7.suara ketikan keyboard.mp3"

    nr "Kreswara menyambungkan semua kabel untuk memindahkan AS-LEEN."

    show effect_1 at truecenter with dissolve

    a "Memulai transfer..."

    play sound "audio/sfx/chapter 1/8.suara glitch digital.mp3"

    a "Transfer selesai. Saya sekarang berada di PUPILS."

    scene bg_masuk_pupils with fade

    k "Oke... sekarang rasanya lebih serius."

    stop music fadeout 1.0
    play music "audio/ambient_hybrid.mp3" fadein 2.0

    play sound "audio/sfx/chapter 1/energy charging .mp3"

    show effect_10 at truecenter with dissolve

    pause 3.0 

    scene bg_dunia_lain with dissolve
    play music "audio/backsound/Chapter 1/asleen berwujud.mp3" fadein 1.0

    nr "Cahaya yang sangat terang menutupi tubuh Kreswara."
    nr "Ia berpindah ke dunia hybrid. Pandangannya menghilang dalam kegelapan sekejap."

    nr "Kreswara membuka matanya perlahan."
    nr "Desa terlihat seperti tidak terjadi apa-apa, namun tidak seperti biasanya."
    nr "Lampu menjadi energi utama. Udara di sekitar pun terasa sangat berat."

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

    nr "Kreswara terdiam kagum. AS-LEEN tampak seperti hologram namun sangat nyata"
    nr "paras cantik dengan mata bulat besar dan ekspresi yang nyaris tidak pernah berubah."

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
    play music "audio/backsound/Chapter 1/BOSSSSSS.mp3" fadein 1.0
    $ boss_hp       = 3
    $ boss_attempts += 1
    $ fase1_benar   = 0
    $ fase2_benar   = 0
    $ fase3_benar   = 0

    stop music

    scene bg_dunia_lain with dissolve
    play music "audio/backsound/Chapter 1/boss_1-buta_cakil.mp3" fadein 0.5
    play sound "audio/sfx/chapter 1/8.suara distorsi audio.mp3"

    show screen radar_roh_screen(level=1)    
    pause 2.5

    show screen state_roh_screen("WASPADA")
    pause 2.5

    stop sound

    nr "Belum sempat melakukan apa-apa, Kreswara merasakan tanah mulai bergerak,"
    nr "memunculkan keretakan. Tiba-tiba sosok besar muncul di hadapannya."
    nr "Gerakannya kaku seperti wayang yang rusak."

    scene bg_versus with dissolve

    a "Waspada, Wara itu Buta Cakil. Entitas pertama yang mengunci wayang."
    a "Data obsesinya sangat kuat. Satu kesalahan bisa melumpuhkanmu."

    show effect_3 at truecenter with dissolve

    play sound "audio/sfx/chapter 1/8.suara glitch digital.mp3"

    pause 3.0 

    stop sound
    scene bg_dunia_lain with dissolve

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

    nr "── FASE 1: Kenali Pola Serangan ──"
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
            k "UGHHH—! Itu salah, aku jadi kena serangan nya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "7.5 bukan integer. Coba soal yang lebih mudah dulu untuk pulihkan energimu!"
            hide a_talk
            jump cadangan_1

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
            play sound "audio/sfx/chapter 1/monster.mp3"
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
            jump cadangan_1

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
            jump cadangan_1


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
            jump cadangan_2

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
            jump cadangan_2

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
            jump cadangan_2

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
            play sound "audio/sfx/chapter 1/monster.mp3"
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
            jump cadangan_3

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
            play sound "audio/sfx/chapter 1/monster.mp3"
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
            jump cadangan_3

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
            jump cadangan_3

    if fase1_benar >= 2:
        show k_angrytalk at Position(xalign=0.5, yalign=0.3) with dissolve
        k "Aku mulai bisa membaca gerakanmu, Buta Cakil."
        k "Setiap serangan datamu... aku akan patahkan satu per satu."
        hide k_angrytalk

    jump boss_buta_cakil_fase2


label boss_buta_cakil_fase2:
    play music "audio/backsound/Chapter 1/BOSS 2.mp3" fadein 1.0
    hide screen state_roh_screen

    show effect_8 at truecenter with dissolve

    pause 3.0 

    scene bg_dunia_lain with dissolve

    nr "── FASE 2: RAGE STATE — Buta Cakil Mengamuk! ──"

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
            a "KAA bukan di Jakarta! Itu di Bandung. Coba soal lebih mudah dulu!"
            hide a_talk
            jump cadangan_4

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
            jump cadangan_4

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
            play sound "audio/sfx/chapter 1/monster.mp3"
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
            a "KAA bukan di Malaysia! Coba soal lebih mudah dulu!"
            hide a_talk
            jump cadangan_4


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
            a "input() selalu menghasilkan teks! Coba soal lebih mudah dulu!"
            hide a_talk
            jump cadangan_5

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
            a "float itu desimal. input() selalu str! Coba soal lebih mudah!"
            hide a_talk
            jump cadangan_5

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
            jump cadangan_5

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
            play sound "audio/sfx/chapter 1/monster.mp3"
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
    hide screen soal_panel 

    scene bg_dunia_lain with dissolve

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Kita masih bisa, Wara. Buta Cakil sudah lemah—tinggal fase terakhir!"
    hide a_talk

label boss_buta_cakil_fase3:
    play music "audio/backsound/Chapter 1/BOSS 3.mp3" fadein 1.0
    hide screen state_roh_screen
    show screen state_roh_screen("marah")
    pause 1.0

    show effect_3 at truecenter with dissolve

    pause 3.0 

    scene bg_dunia_lain with dissolve

    nr "── FASE 3: ENRAGED MODE — Chaos Pressure! ──"

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
    show screen timer_screen(length=25.0)
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
            a "Dwikora bukan soal Amerika! Coba soal serupa yang berbeda!"
            hide a_talk
            jump cadangan_6

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
            a "Konflik dengan Belanda berbeda konteksnya! Coba soal serupa!"
            hide a_talk
            jump cadangan_6

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
            a "Soviet dekat dengan Indonesia saat itu! Coba soal serupa!"
            hide a_talk
            jump cadangan_6

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
            play sound "audio/sfx/chapter 1/monster.mp3"
            show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            bc "GRAAAHHHH— Tidak mungkin... tidak... MUNGKIN!"
            hide bc_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Satu pukulan lagi, Wara. Akhiri dia sekarang!"
            hide a_talk


label soal_7:
    show screen timer_screen(length=25.0)
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
            jump cadangan_7

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
            play sound "audio/sfx/chapter 1/monster.mp3"
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
            jump cadangan_7

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
            jump cadangan_7

label boss_buta_cakil_menang:
    hide screen radar_roh_screen
    hide screen timer_screen
    stop music fadeout 0.5

    scene bg_menang with dissolve
    play sound "audio/sfx/chapter 1/gelombang energi .mp3"

    k "SELESAIKAN!!"

    bc "AGHHH!!! tidak... MUNGKIN!"
    bc "AKU... BUTA CAKIL..."

    bc "TIDAK MUNGKIN KALAH!!!"

    show effect_3 at truecenter with dissolve

    pause 3.0 

    scene bg_dunia_lain with dissolve

    nr "Tubuh Buta Cakil mulai pudar dan menjadi cahaya"
    nr "lalu ia perlahan masuk ke sistem."

    play music "audio/backsound/Chapter 1/asleen berwujud.mp3" fadein 2.0

    nr "Beberapa titik cahaya muncul di sekitar. Wayang yang tadi hilang... mulai kembali satu per satu."

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

    nr "Kreswara menarik napas panjang—bukan karena takut, tapi karena siap untuk melawan semua musuh yang akan datang."

    nr "── DATA ROH BUTA CAKIL TERSIMPAN ──"
    nr "Radar Roh meningkat. Satu entitas berhasil dijinakkan."


    jump chapter1_ending


label waktu_habis_boss:
    hide screen timer_screen
    hide screen radar_roh_screen
    hide screen state_roh_screen
    hide screen soal_panel
    $ renpy.block_rollback()
    
    call screen kalah_boss_screen()

    if _return == "restart":
        jump boss_buta_cakil_fase3_retry
    else:
        $ renpy.full_restart()


label chapter1_ending:
    stop music fadeout 1.5
    stop sound fadeout 1.0
    scene bg_dunia_lain with dissolve

    nr "── CHAPTER 1 SELESAI ──"
    nr "\"Malam Mencekam\""

    nr "Perjalanan Kreswara masih panjang."
    nr "Boss berikutnya: Dursasana — Tema Pemburuan & Hukuman."
    nr "Sampai jumpa di Chapter 2: Perburuan Fajar."

    pause 1.5
    scene black with Dissolve(2.0)
    pause 1.0

    $ persistent.chapter2_unlocked = True

    $ renpy.full_restart()


label cadangan_1:
    show screen soal_panel(
        nomor="1C",
        tema="Python – Operator Aritmatika",
        kode="a = 15\nb = 4\nprint(a // b)",
        pertanyaan="Apa output dari kode di atas?"
    )

    menu:
        "2":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Bukan 2—floor division!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "// itu pembagian bulat. 15//4 = 3, bukan 2!"
            hide a_talk
            jump cadangan_1

        "3":
            hide screen soal_panel
            $ fase1_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "3! Floor division—15 dibagi 4 sisa buang!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Bagus! Sekarang lanjut ke soal berikutnya!"
            hide a_talk
            jump soal_2

        "3.75":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "3.75 itu hasil / bukan //!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "// buang desimalnya! Bukan pembagian biasa!"
            hide a_talk
            jump cadangan_1

        "4":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "4 itu dibulatkan ke atas! // bulatkan ke bawah!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Floor division membulatkan ke bawah, jadi 3 bukan 4!"
            hide a_talk
            jump cadangan_1


label cadangan_2:
    show screen soal_panel(
        nomor="2C",
        tema="Sejarah – Orde Lama",
        kode="",
        pertanyaan="Gerakan 30 September 1965 (G30S) pada akhirnya\nmenjadi salah satu penyebab keluarnya..."
    )

    menu:
        "Dekrit Presiden 5 Juli 1959":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Dekrit 1959?! Itu jauh sebelum G30S!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "G30S terjadi 1965. Dekrit 1959. Urutan waktunya berbeda!"
            hide a_talk
            jump cadangan_2

        "Supersemar 1966":
            hide screen soal_panel
            $ fase1_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "SUPERSEMAR! G30S → kekacauan → Soeharto dapat mandat!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Sekarang lanjut ke soal berikutnya!"
            hide a_talk
            jump soal_3

        "Konferensi Asia-Afrika di Bandung":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "KAA 1955?! Itu 10 tahun sebelum G30S!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "KAA dan G30S tidak ada hubungannya langsung!"
            hide a_talk
            jump cadangan_2

        "Dewan Konstituante":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Konstituante dibubarkan Dekrit 1959, bukan G30S!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "G30S → Supersemar. Itu urutan yang benar!"
            hide a_talk
            jump cadangan_2


label cadangan_3:
    show screen soal_panel(
        nomor="3C",
        tema="Python – Tipe Data Boolean",
        kode="x = 10\ny = 20\nprint(x > y)\nprint(type(x > y))",
        pertanyaan="Apa output dari kode di atas?"
    )

    menu:
        "True dan <class 'int'>":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "10 > 20?! Itu False, bukan True!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "10 tidak lebih besar dari 20. Dan typenya bool, bukan int!"
            hide a_talk
            jump cadangan_3

        "False dan <class 'bool'>":
            hide screen soal_panel
            $ fase1_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "False dan bool! 10 tidak lebih besar dari 20!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Perbandingan selalu menghasilkan bool. Lanjut!"
            hide a_talk
            jump soal_4

        "True dan <class 'bool'>":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Type-nya benar bool, tapi nilainya False bukan True!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "10 > 20 adalah False! 10 tidak lebih besar dari 20!"
            hide a_talk
            jump cadangan_3

        "False dan <class 'int'>":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Nilai benar False, tapi typenya bool bukan int!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Perbandingan selalu menghasilkan bool, bukan int!"
            hide a_talk
            jump cadangan_3


label cadangan_4:
    show screen soal_panel(
        nomor="4C",
        tema="Sejarah – Orde Lama",
        kode="",
        pertanyaan="Pemberontakan PKI Madiun 1948\nberhasil ditumpas oleh pasukan pimpinan..."
    )

    menu:
        "Jenderal A.H. Nasution":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Nasution sendirian? Bukan, ada Soeharto juga!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Keduanya memimpin bersama—Nasution DAN Soeharto!"
            hide a_talk
            jump cadangan_4

        "Kolonel A.E. Kawilarang":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Kawilarang bukan di Madiun!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Yang menumpas PKI Madiun adalah Nasution dan Soeharto!"
            hide a_talk
            jump cadangan_4

        "Kolonel A.H. Nasution dan Letkol Soeharto":
            hide screen soal_panel
            $ fase2_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "Nasution dan Soeharto! Dua nama yang menumpas PKI Madiun!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Lanjut ke soal berikutnya!"
            hide a_talk
            jump soal_5

        "Panglima Sudirman":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Sudirman tidak memimpin langsung penumpasan Madiun!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Yang memimpin di lapangan adalah Nasution dan Soeharto!"
            hide a_talk
            jump cadangan_4


label cadangan_5:
    show screen soal_panel(
        nomor="5C",
        tema="Python – Konversi Tipe",
        kode="nilai = '3.14'\nprint(float(nilai))\nprint(int(float(nilai)))",
        pertanyaan="Apa output dari kode di atas?"
    )

    menu:
        "3.14 dan 3":
            hide screen soal_panel
            $ fase2_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "3.14 lalu 3! float() konversi string, int() potong desimal!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Lanjut ke soal terakhir fase ini!"
            hide a_talk
            jump soal_6

        "3.14 dan 3.14":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "int() memotong desimalnya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "int(3.14) = 3, bukan 3.14! Desimalnya dipotong!"
            hide a_talk
            jump cadangan_5

        "'3.14' dan 3":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Baris pertama bukan string lagi! float() mengubahnya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "float('3.14') = 3.14 (angka), bukan '3.14' (string)!"
            hide a_talk
            jump cadangan_5

        "Error: tidak bisa konversi":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Tidak error! Python bisa konversi string angka ke float!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "float('3.14') berjalan normal. Tidak ada error!"
            hide a_talk
            jump cadangan_5


label cadangan_6:
    show screen timer_screen(length=25.0)
    show screen soal_panel(
        nomor="6C",
        tema="Sejarah – Orde Lama",
        kode="",
        pertanyaan="Sistem ekonomi yang diterapkan pada masa\nDemokrasi Terpimpin (1959–1965) adalah..."
    )

    menu:
        "Ekonomi liberal dengan pasar bebas":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Liberal?! Di era Soekarno?! Salah besar!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Demokrasi Terpimpin justru anti-liberal! Coba soal serupa lagi!"
            hide a_talk
            jump cadangan_6b

        "Ekonomi kapitalis pro investasi asing":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Kapitalis?! Soekarno nasionalisasi perusahaan asing!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Era ini menutup investasi asing! Coba soal serupa lagi!"
            hide a_talk
            jump cadangan_6b

        "Ekonomi terpimpin dengan peran besar negara":
            hide screen timer_screen
            hide screen soal_panel
            $ fase3_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "EKONOMI TERPIMPIN! Negara kendalikan segalanya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Sekarang soal terakhir—kerahkan semua kekuatanmu!"
            hide a_talk
            jump soal_7

        "Ekonomi campuran dengan koperasi":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Koperasi bukan inti Demokrasi Terpimpin!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Ekonomi terpimpin—negara yang pegang kendali penuh! Coba lagi!"
            hide a_talk
            jump cadangan_6b

label cadangan_7:
    show screen timer_screen(length=25.0)
    show screen soal_panel(
        nomor="7C",
        tema="Python – Operator Gabungan",
        kode="x = 5\nx += 3\nx *= 2\nprint(x)",
        pertanyaan="Apa output dari kode di atas?"
    )

    menu:
        "10":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Bukan 10! Kamu lupa langkah += dulu baru *=!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "x=5, lalu +=3 jadi 8, lalu *=2 jadi 16! Coba soal serupa!"
            hide a_talk
            jump cadangan_7b

        "13":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "13?! Kamu tidak mengalikan dengan 2!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Setelah +=3 jadi 8, lalu *=2 jadi 16! Coba soal serupa!"
            hide a_talk
            jump cadangan_7b

        "16":
            hide screen timer_screen
            hide screen soal_panel
            $ fase3_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "16! 5+3=8, 8×2=16! HABISI DIA SEKARANG!"
            hide k_angrytalk
            play sound "audio/sfx/chapter 1/monster.mp3"
            show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            bc "TIDAK MUNGKIN... KAU BISA MEMECAHKAN SEMUANYA?!"
            hide bc_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "SELESAI! Buta Cakil tidak bisa bertahan lagi!"
            hide a_talk
            jump chapter1_ending

        "11":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "11?! Kamu salah urutan operasi!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Ikuti urutan: +=3 dulu → 8, baru *=2 → 16! Coba soal serupa!"
            hide a_talk
            jump cadangan_7b


label cadangan_6b:
    show screen timer_screen(length=25.0)
    show screen soal_panel(
        nomor="6C-2",
        tema="Sejarah – Orde Lama",
        kode="",
        pertanyaan="Indonesia keluar dari keanggotaan PBB\npada tahun 1965. Penyebab utamanya adalah..."
    )

    menu:
        "Sengketa wilayah Papua dengan Belanda":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Papua dan PBB berbeda konteksnya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Masalah Papua sudah selesai sebelum 1965. Ini soal Malaysia!"
            hide a_talk
            jump cadangan_6b

        "Protes atas diterimanya Malaysia sebagai anggota DK PBB":
            hide screen timer_screen
            hide screen soal_panel
            $ fase3_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "Malaysia masuk DK PBB—Soekarno langsung keluar!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Politik Konfrontasi total! Lanjut soal terakhir!"
            hide a_talk
            jump soal_7

        "Penolakan terhadap bantuan Amerika Serikat":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Bantuan AS bukan alasan keluar PBB!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Alasannya adalah Malaysia masuk Dewan Keamanan PBB!"
            hide a_talk
            jump cadangan_6b

        "Konflik dengan negara Asia Tenggara lainnya":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Terlalu umum! Ada satu negara spesifik yang jadi penyebabnya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Malaysia masuk DK PBB—itulah pemicunya!"
            hide a_talk
            jump cadangan_6b

label cadangan_7b:
    show screen timer_screen(length=25.0)
    show screen soal_panel(
        nomor="7C-2",
        tema="Python – Penamaan Variabel",
        kode="",
        pertanyaan="Manakah nama variabel yang TIDAK VALID\ndalam Python?"
    )

    menu:
        "nilai_akhir":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "nilai_akhir valid! Underscore diperbolehkan!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Variabel boleh pakai underscore. Cari yang diawali angka!"
            hide a_talk
            jump cadangan_7b

        "_nama":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "_nama valid! Underscore boleh di awal!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Diawali underscore itu valid di Python. Cari yang diawali angka!"
            hide a_talk
            jump cadangan_7b

        "2data":
            hide screen timer_screen
            hide screen soal_panel
            $ fase3_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "2data! Tidak boleh diawali angka—Python langsung error!"
            hide k_angrytalk
            play sound "audio/sfx/chapter 1/monster.mp3"
            show bc_talk at Position(xalign=0.5, yalign=0.2), getar with dissolve
            bc "TIDAK MUNGKIN... KAU BISA MEMECAHKAN SEMUANYA?!"
            hide bc_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "SELESAI! Buta Cakil tidak bisa bertahan lagi!"
            hide a_talk
            jump boss_buta_cakil_menang

        "dataKe2":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "dataKe2 valid! Angka boleh di tengah atau akhir!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Yang tidak boleh hanya angka DI AWAL nama variabel!"
            hide a_talk
            jump cadangan_7b
