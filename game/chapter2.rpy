label chapter2_full:

    $ quiz_score    = 0
    $ quiz_total    = 5
    $ boss_hp       = 3
    $ boss_attempts = 0
    $ fase1_benar   = 0
    $ fase2_benar   = 0
    $ fase3_benar   = 0

    scene bg_ch2_nav_error with dissolve
    play music "audio/backsound/Chapter 2/royaltyfreemusicstudio-mystic-fantasy-ambience-441255.mp3" fadein 2.0

    centered "Setelah mengalahkan buta cakil, wara harus mencari lawan selanjutnya."
    centered "Dia pun sudah siap bergerak menuju arah yang diberikan oleh as-leen."

    play sound "audio/sfx/chapter 2/1.suara error.wav"
    centered "Namun baru beberapa langkah berjalan. tiba tiba as-leen mengeluarkan suara aneh."

    scene bg_ch2_labirin with dissolve
    play sound "audio/sfx/chapter 2/1.suara robot mulfunction.mp3"

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "A-ada apa as-leen?......... Apa kamu baik baik saja?"
    hide k_talk

    play sound "audio/sfx/chapter 2/1.suara glitch digital.wav"

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Aku baik-baik saja…..hanya saja navigasiku bermasalah."
    hide a_talk

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Baiklah….. kamu cukup memperhatikan saja, biar aku yang urus"
    hide k_talk

    # ── Perjalanan mengitari desa, menuju labirin ─────────────
    scene bg_ch2_jalan_labirin with dissolve
    play music "audio/backsound/Chapter 2/rubyzephyr-fantasy-rpg-exploration-v2-461303.mp3" fadein 2.0
    play sound "audio/sfx/chapter 2/2.suara langkah kaki di tanah (1).mp3"

    centered "Wara pun mencari boss dengan mengitari desa, untuk mencari boss nya. Selama perjalanan ia harus melewati semua tantangan yang ia lewati."
    centered "Setelah menempuh perjalanan yang jauh. Sampailah ia di sebuah tempat reruntuhan labirin."

    scene bg_ch2_labirin_kursi with dissolve
    play sound "audio/sfx/chapter 2/3.suara floating hum(dengung).mp3"

    centered "Tempat yang terlihat megah namun tertutup dengan retakan retakan yang membuat keindahan nya tertutup,"
    centered "di dalam nya penuh dengan bangku sekolah yang melayang dan tidak satupun yang menyentuh lantai."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(bingung)"
    hide k_think

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Tempat apa ini.......?"
    hide k_think

    # ── Ngobrol nostalgia di labirin ──────────────────────────
    scene bg_ch2_jalan_melayang with dissolve
    play music "audio/backsound/Chapter 2/atlasaudio-dream-518077.mp3" fadein 2.0
    play sound "audio/sfx/chapter 2/3.suara magnet levitation ambience.mp3"

    centered "Wara berjalan perlahan memasuki labirin itu, ia melihat sekitar dan menganalisis apa yang akan dia lawan pada kali ini. Terlintas di pikiran nya, ia mengingat sekolah yang dulu mengajarkan nya coding."

    scene bg_ch2_labirin_kursi with dissolve

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Hufttt… rasanya seperti nostalgia ya?"
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Kenapa wara?"
    hide a_talk

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Dulu aku disekolah, aku selalu ingin mencari tau apapun, salah satunya yaitu coding……yah,"
    k "rasanya aku jadi teringat saja masa masa itu "
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Ya…masa masa sekolah adalah yang terindah menurut data "
    a "Masa sekolah sering dianggap sebagai masa paling indah karena pada fase ini seseorang mengalami banyak pengalaman pertama yang berkesan,"
    a "seperti menemukan sahabat, mengikuti organisasi, hingga merasakan kebersamaan setiap hari dengan teman-teman."
    a "Dalam Psikologi Perkembangan, usia remaja dikenal sebagai fase pembentukan memori emosional paling kuat sehingga kenangan masa sekolah lebih mudah diingat hingga dewasa."
    a "Selain itu, kehidupan saat sekolah juga dinilai lebih menyenangkan karena tanggung jawab belum seberat masa dewasa,"
    a "tetapi kebebasan untuk bersosialisasi dan mengeksplorasi diri sudah mulai terbentuk."
    a "Karena alasan tersebut, banyak orang dewasa merasa rindu dan menganggap masa sekolah sebagai salah satu fase terbaik dalam hidup mereka."
    hide a_talk

    scene bg_ch2_jalan_melayang with dissolve

    centered "Setelah mengingat bahwa ia sekarang bisa menguasai coding, kreswara merasa bahwa semua hal bisa ia lakukan."
    centered "Dan tidak mungkin juga bahwa ia bisa memberikan itu juga ke orang yang ia sayang."

    scene bg_ch2_labirin_kursi with dissolve

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Sekarang aku sudah menjadi programer…….. Aku rasa…..aku bisa membuatmu menjadi nyata as-leen, dan sepertinya……. aku sayang padamu, mungkinnn....?"
    hide k_talk

    show a_normal at Position(xalign=0.5, yalign=0.3) with dissolve
    a "(bingung & terdiam)"
    a "………………"
    hide a_normal

    scene bg_ch2_jalan_melayang with dissolve

    centered "As-leen tidak menanggapi bualan dari wara. menurutnya wara membicarakan hal yang mustahil dan tidak penting untuk progress dalam dunia virtual ini."

    scene bg_ch2_labirin_kursi with dissolve

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(canggung)"
    k "A-apakah aku salah m-mengakatakan sesuatu?"
    hide k_think

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Tidak…..namun yang kamu katakan tidak relevan. menurut data yang saya punya,"
    a "\u201csayang\u201d yang kamu definisikan hanya kondisi biologis yang hanya terjadi di otak manusia."
    hide a_talk

    scene bg_ch2_jalan_melayang with dissolve

    centered "Wara terkejut dan tidak bisa berkata apa apa. Ia tidak percaya as-leen mengatakan itu."
    centered "Sepertinya wara lupa bahwa as-leen adalah ai. Namun menurutnya as-leen lucu dan sangat imut."

    scene bg_ch2_labirin_kursi with dissolve

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(tertawa)"
    hide k_smile

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Hahahahahaha, kau lucu sekali as-leen."
    hide k_talk

    show a_nod at Position(xalign=0.5, yalign=0.3) with dissolve
    a "(bingung)"
    a "…………?"
    hide a_nod

    scene bg_ch2_jalan_melayang with dissolve

    # ── Tanah mulai retak — lari! ─────────────────────────────
    centered "Setelah perbincangan yang begitu romantis, mereka melanjutkan perjalanannya untuk mencari arena boss yang telah ditunjukkan oleh as-leen."
    centered "Tak butuh waktu lama wara dan as-leen merasakan tanda tanda boss akan muncul."

    play sound "audio/sfx/chapter 2/4.suara ground cracking 1.mp3"
    centered "Retakan tanah keluar tak lama setelah mereka berjalan. wara dan as-leen langsung berlari dari reruntuhan yang ingin roboh tersebut."

    play music "audio/backsound/Chapter 2/surprising_media-spatial-fantasy-455240.mp3" fadein 1.0
    play sound "audio/sfx/chapter 2/5.suara footstep running.mp3"

    scene bg_ch2_labirin_kursi with dissolve

    show k_angrytalk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "As-leen lari!"
    hide k_angrytalk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Benar sekali…..ayo kita lari sebelum ini semua ini runtuh"
    hide a_talk

    scene bg_ch2_jalan_melayang with dissolve

    play sound "audio/sfx/chapter 2/5.suara crumbling ruins.mp3"

    centered "Mereka berdua pun berlari. Meskipun di dunia virtual ini as-leen sebagai ai. Ia tetap punya wujud kokoh nya sendiri di dunia ini."
    centered "Rambut as-leen terurai selagi mereka berlari. Wara melihat rambuh indah nya dari belakang, sambil menjaga dari retakan yang mengejar mereka."
    centered "Retakan itu terus mengejar mereka berdua. as-leen berada di depan dan dijaga oleh kreswara."

    scene bg_ch2_labirin_kursi with dissolve

    play sound "audio/sfx/chapter 2/4.suara ground cracking 2.mp3"

    show k_angrytalk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "As-leen…… ke kiri!"
    hide k_angrytalk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Baik…."
    hide a_talk

    scene bg_ch2_jalan_melayang with dissolve

    play sound "audio/sfx/chapter 2/5.suara debris falling.mp3"

    centered "As-leen pun berpindah ke kiri lalu selamat dari retakan di depan nya. Tak berapa lama retakan itu pun berhenti."
    centered "Mereka pun beristirahat dan mengambil napas."

    play sound "audio/sfx/chapter 2/5.suara fast breathing 1.mp3"

    centered "Wara yang sedang beristirahat melihat lubang retakan tersebut. Lalu ia melihat sebuah lapisan khusus di dalam nya."

    # ── Menemukan lapisan puzzle di dalam retakan ─────────────
    scene bg_ch2_sebelum_puzzle with dissolve
    play music "audio/backsound/Chapter 2/deuslower-fantasy-medieval-mystery-ambient-292418.mp3" fadein 2.0

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(menunjuk lapisan tersebut)"
    k "As-leen…….liat itu"
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Di dalamnya ada lapisan? untuk apa lapisan itu?"
    hide a_talk

    centered "Tanpa pikir panjang wara pun langsung loncat dan menembus lapisan tersebut."
    centered "As-leen tak punya banyak pilihan, ia pun mengikuti kreswara masuk kedalam retakan tersebut."
    centered "Setelah ia masuk kedalam retakan tersebut ia menemukan sebuah puzzle yang harus ia selesaikan."

    play sound "audio/sfx/chapter 2/7.suara puzzle click.mp3"

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(wajah tengil)"
    k "Yeah, ini cukup mudah"
    hide k_smile

    scene bg_ch2_puzzle with dissolve

    play sound "audio/sfx/chapter 2/7.suara ketikan keyboard.wav"

    centered "Dengan tangan yang terampil dan ahli kreswara menyelesaikan puzzle tersebut dengan mudah dan tanpa hambatan sama sekali."
    centered "As-leen terkejut dengan keahlian wara dalam menyelesaikan puzzle tersebut."

    scene bg_ch2_sebelum_puzzle with dissolve

    play sound "audio/sfx/chapter 2/9.suara hud activation.mp3"

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Selesai…..kita bisa melanjutkan perjalanan selanjutnya. Ayo, kita masuk as-leen."
    hide k_talk

    show a_nod at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Baiklah"
    hide a_nod

    # ── Menuju lokasi bos kedua ───────────────────────────────
    scene bg_ch2_sebelum_puzzle with dissolve
    play sound "audio/sfx/chapter 2/2.suara langkah kaki di tanah (2).mp3"

    centered "Setelah melewati semua nya. Mereka berjalan menuju lokasi bos kedua."
    centered "Tempat itu luas dan juga megah, namun beberapa retakan menyebabkan tempat itu tidak cocok untuk ditinggali makhluk manapun."

    play sound "audio/sfx/chapter 2/4.suara ground cracking 3.mp3"

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Woah……as-leen hati hati. Tempat ini sangat ringkih. berhati hatilah"
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Bawel"
    hide a_talk

    show k_laugh at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Pintar juga ya sekarang ngomong nya, jadi mirip manusia (sambil tertawa)"
    hide k_laugh

    # ── Encounter data roh ────────────────────────────────────
    scene bg_ch2_sebelum_puzzle with dissolve
    play music "audio/backsound/Chapter 2/onetent-samurai-flutes-ethereal-fantasy-flute-relaxing-meditation-music-248255.mp3" fadein 2.0
    play sound "audio/sfx/chapter 2/8.suara ghost static.mp3"

    centered "Sebuah data roh muncul di hadapan mereka berdua."
    centered "Kreswara harus mengalahkan data-data roh itu, agar data itu bisa as-leen gunakan untuk melawan Dursasana."

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Data-data roh….wara kamu harus mengalahkan mereka."
    a "Agar aku bisa menggunakan data-data itu untuk melawan boss berikutnya!"
    hide a_talk

    show k_normal at Position(xalign=0.5, yalign=0.3), napas_berat with dissolve
    k "(mengangguk)"
    k "Baiklah…..akan ku kalahkan mereka semua!"
    hide k_normal

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Tunggu wara, kamu jangan langsung menyerang begitu saja."
    hide a_talk

    # ── PUPILS layar menyala ──────────────────────────────────
    scene bg_ch2_pupils_nyala with dissolve
    play sound "audio/sfx/chapter 2/9.suara hud activation.mp3"

    centered "Layar kecil di PUPILS milik wara tiba tiba menyala. Beberapa tulisan muncul cepat di depannya."

    play sound "audio/sfx/chapter 2/9.suara cyber analysis sound.mp3"

    centered "( PUPILS )\nUNKNOWN DATA\nMENCARI TIPE DATA..."

    scene bg_ch2_asleen_error with dissolve

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Hah?.....maksudnya apa ini? apakah sistem nya error??"
    hide k_think

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Bukan, itu adalah fitur yang akan membantumu untuk mencari dan mengetahui tipe data roh itu."
    hide a_talk

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Jadi aku harus tau dulu tipe data mereka?"
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Iya betul. Jadi, kalau kamu asal menyerang lalu menyerap datanya, mentalmu bisa terganggu."
    hide a_talk

    centered "mendengar itu wara menjadi kebingungan."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Memang kenapa?"
    hide k_think

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Karena kamu manusia, otak manusia tidak dibuat untuk menampung terlalu banyak data asing seperti ini."
    a "Kalau data yang rusak dipaksa masuk, pikiranmu bisa kacau sedikit demi sedikit."
    hide a_talk

    scene bg_ch2_pupils_nyala with dissolve

    play sound "audio/sfx/chapter 2/8.suara Whispering voices.mp3"

    centered "Wara terdiam sebentar. Belum sempat dia menjawab, suara aneh mulai terdengar samar."
    centered "Di kepalanya seperti bisikan orang menangis dan suara marah yang bercampur jadi satu."

    scene bg_ch2_asleen_error with dissolve

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Ughh……kenapa dengan kepalaku??"
    hide k_think

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Itu efek dari data roh tersebut. Kamu harus menjinakkannya dulu sebelum menyerapnya."
    hide a_talk

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Bagaimana cara menjinakannya?"
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Perhatikan gerakannya dan pahami emosinya."
    a "Lalu saat datanya mulai stabil, baru kamu bisa menghancurkan wujudnya lalu menyerapnya."
    hide a_talk

    scene bg_ch2_pupils_nyala with dissolve

    play sound "audio/sfx/chapter 2/9.suara scanner beep.mp3"

    centered "Wara menarik napas pelan lalu mulai fokus melihat roh itu."
    centered "Gerakannya terlihat tidak karuan, kadang roh itu mundur sendiri, kadang tubuh nya gemetaran, dan glitch di badannya tidak stabil."
    centered "Tapi lama lama wara sadar kalau roh itu sebenarnya terlihat ketakutan."
    centered "Perlahan tulisan di layar PUPILS berubah."

    play sound "audio/sfx/chapter 2/7.suara ui beep.mp3"

    centered "() PUPILS )\nTYPE DATA : TAKUT\nSTATUS : TIDAK STABIL"

    scene bg_ch2_asleen_error with dissolve

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Ohhhh, jadi mereka takut?"
    hide k_think

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Iya betull, jadi kamu jangan lawan dengan emosi."
    a "Jinakan datanya dulu. Jika sudah tenang maka kamu boleh menyerapnya"
    hide a_talk

    scene bg_ch2_pupils_nyala with dissolve

    play sound "audio/sfx/chapter 2/7.suara data processing.mp3"

    centered "Wara mulai bergerak pelan. Dia tidak langsung menyerang."
    centered "Dia mencoba membaca pola gerakan roh itu sambil menghindari serangannya."
    centered "Semakin lama… cahaya glitch di tubuh roh itu mulai melemah."
    centered "Suara bisikan di kepala wara perlahan hilang."

    scene bg_ch2_asleen_error with dissolve

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Bagus wara!! sekarang datanya sudah stabil."
    hide a_talk

    scene bg_ch2_pupils_nyala with dissolve

    centered "Wara langsung memasang senyum kecil, lalu berlari cepat ke arah roh tersebut."

    scene bg_ch2_asleen_error with dissolve

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Sekarang, aku akan selesaikan semua nya"
    hide k_smile

    scene bg_ch2_pupils_nyala with dissolve

    centered "Wara meluncurkan serangan tepat ke bagian inti tubuh roh itu."

    play sound "audio/sfx/chapter 2/4.suara stone collapse.mp3"

    centered "Tubuh roh tersebut langsung pecah menjadi serpihan cahaya kecil yang beterbangan di udara."
    centered "PUPILS milik wara langsung mengeluarkan cahaya yang sangat terang lalu menyerap semua serpihan itu."

    play sound "audio/sfx/chapter 2/6.suara energy shield pass.mp3"

    centered "Wara memegang kepalanya perlahan."
    centered "Sesaat setelah data itu terserap, pikirannya dipenuhi perasaan asing yang bukan miliknya."
    centered "Ada rasa takut, kesepian, dan kebingungan yang muncul tiba tiba sampai membuat dadanya terasa sesak."
    centered "Namun perlahan semua itu mulai mereda, seolah data roh tersebut akhirnya menerima wara tanpa perlawanan lagi."

    scene bg_ch2_asleen_error with dissolve

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Hufft……jadi gini rasanya setelah menyerap data mereka."
    hide k_think

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Yap, itu yang kamu rasakan tapi kamu berhasil menyerap mereka."
    hide a_talk

    # ── Pintu biner ───────────────────────────────────────────
    scene bg_ch2_sebelum_puzzle with dissolve

    centered "Setelah semua data roh berhasil dikalahkan, jalan di depan mereka perlahan terbuka."
    centered "Di ujung ruangan terlihat sebuah pintu besar yang hampir hancur."
    centered "Seluruh permukaannya dipenuhi tulisan coding dan angka biner yang terus bergerak."

    scene bg_ch2_pintu_biner with dissolve
    play music "audio/backsound/Chapter 2/nastelbom-soundtrack-443631.mp3" fadein 2.0
    play sound "audio/sfx/chapter 2/2.suara buzz listrik.mp3"

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "O-oke…….jangan bilang ini puzzle lagi."
    hide k_think

    centered "Wara berjalan mendekat sambil memperhatikan pintu itu dengan bingung."
    centered "Angka-angka di permukaannya terus berubah cepat tanpa berhenti."
    centered "Sesekali muncul cahaya merah kecil dari sela sela retakan pintu."

    play sound "audio/sfx/chapter 2/7.suara ketikan keyboard.wav"

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Aku yakin pasti ini menyuruhku mengoding lagi."
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Sepertinya pintu ini menggunakan sistem data untuk membukanya."
    hide a_talk

    centered "Wara menghela nafas pelan lalu mulai memperhatikan susunan angka yang muncul di tengah pintu."
    centered "Awalnya semua terlihat acak, tapi lama lama dia sadar ada beberapa angka yang terus berulang."

    # --- PUZZLE PINTU BINER ---
    play sound "audio/sfx/chapter 2/9.suara cyber analysis sound.mp3"

    centered "01001101"
    centered "01000001"
    centered "01010011"
    centered "01010101"
    centered "01001011"

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Hehh?? bentar bentar.."
    hide k_think

    centered "Wara menyipitkan matanya sambil mencoba mengingat sesuatu."
    centered "Beberapa detik kemudian ekspresinya langsung berubah seperti baru sadar."

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Ohhh sekarang aku tau ini kode apa"
    hide k_smile

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Kode apa?"
    hide a_talk

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Ini kode adalah biner"
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Angka biner? apakah kamu mengerti maksud dari kode nya?"
    hide a_talk

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Iyaa aku tahu"
    hide k_talk

    play sound "audio/sfx/chapter 2/7.suara data processing.mp3"

    centered "wara mulai membaca kode itu pelan pelan sambil menerjemahkannya di kepalanya."
    centered "01001101 = M"
    centered "01000001 = A"
    centered "01010011 = S"
    centered "01010101 = U"
    centered "01001011 = K"

    show k_angrytalk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "\"MASUK\"."
    hide k_angrytalk

    play sound "audio/sfx/chapter 2/1.suara static electronic noise.mp3"

    centered "Sesaat setelah wara mengucapkan kata itu, seluruh angka di pintu tiba tiba bergerak lebih cepat."
    centered "Cahaya merahnya berkedip makin terang sebelum akhirnya muncul susunan angka baru."

    play sound "audio/sfx/chapter 2/9.suara cyber analysis sound.mp3"

    centered "01010111"
    centered "01000001"
    centered "01010010"
    centered "01000001"

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Kode ini seperti familiar, tapi apa?"
    hide k_think

    centered "Wara kembali membaca susunan angka itu perlahan."
    centered "W — A — R — A"

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
    k "Hah?? ini nama aku, kenapa sistem ini tau nama aku?"
    hide k_angrytalk

    centered "Suasana tiba tiba terasa jauh lebih sunyi."
    centered "Wara menatap pintu itu beberapa detik tanpa bicara."
    centered "Rasanya aneh melihat sistem di tempat ini bisa mengenali dirinya."

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Sepertinya pintu ini memang menunggumu."
    hide a_talk

    centered "Belum sempat wara menjawab, seluruh angka di pintu langsung berhenti bergerak."
    centered "Lalu perlahan muncul sebuah tulisan besar tepat di tengah pintu."
    centered "WELCOME, KRESWARA"

    # ── Pintu terbuka ─────────────────────────────────────────
    scene bg_ch2_pintu_terbuka with dissolve
    play sound "audio/sfx/chapter 2/6.suara portal whoosh1.mp3"

    centered "Cahaya merah di sela sela retakan pintu perlahan berubah jadi biru terang."
    centered "Suara besi bergeser mulai terdengar pelan sebelum akhirnya pintu besar itu terbuka sedikit demi sedikit."
    centered "Udara dingin langsung keluar dari dalam ruangan gelap di baliknya."
    centered "Tepat di tengah ruangan itu ada seseorang sudah berdiri menunggu mereka."

    scene bg_ch2_pintu_biner with dissolve

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Tenangin diri kamu waraa. Kamu pasti kuat, kamu pasti bisa menyelesaikan ini semua."
    hide k_talk

    scene bg_ch2_pintu_terbuka with dissolve

    centered "Wara berjalan mendekat lalu mencoba mendorong pintu tersebut."
    centered "Berat sekali sampai tubuhnya ikut gemetar menahannya."
    centered "Melihat itu as-leen pun membantu mendorong pintu tersebut."
    centered "Wara menggertakkan giginya lalu mendorong lebih kuat."

    scene bg_ch2_pintu_biner with dissolve

    play sound "audio/sfx/chapter 2/6.suara warp transition.mp3"

    show k_angrytalk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "NGGHHH… AYO TERBUKALAH…"
    hide k_angrytalk

    scene bg_ch2_pintu_terbuka with dissolve

    play sound "audio/sfx/chapter 2/6.suara portal whoosh2.mp3"

    centered "Perlahan pintu besar itu akhirnya terbuka sepenuhnya."
    centered "Suara besi yang bergesekan menggema ke seluruh ruangan."
    centered "Udara dingin langsung menyambut wara dan as-leen dari dalam."
    centered "Wara sempat menarik napas pelan sebelum akhirnya mereka berdua berjalan masuk."

    # ── Bertemu Dursasana ─────────────────────────────────────
    scene bg_ch2_sebelum_ds with dissolve
    play music "audio/backsound/Chapter 2/surprising_media-spatial-fantasy-455240.mp3" fadein 2.0
    play sound "audio/sfx/chapter 2/2.suara angin dalam ruangan besar.mp3"

    centered "Ruangan di baliknya sangat luas dan gelap."
    centered "Lantainya dipenuhi retakan bercahaya ungu yang bergerak pelan seperti aliran data hidup."
    centered "Beberapa bagian dinding bahkan terlihat hancur dan bergoyang tidak stabil,"
    centered "seolah tempat itu bisa runtuh kapan saja."

    centered "Langkah wara perlahan melambat saat di tengah ruangan mulai terlihat sebuah sosok berdiri membelakangi mereka."
    centered "Awalnya hanya bayangan hitam namun, sedikit demi sedikit wujudnya mulai terlihat jelas."
    centered "Tubuhnya tinggi besar dengan armor hitam penuh retakan cahaya ungu yang menyala dari sela sela tubuhnya."
    centered "Tatapannya tajam lurus ke arah wara seolah sejak awal memang sudah menunggu kedatangan mereka."

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Dursasana..."
    hide a_talk

label boss_dursasana_start:
    play music "audio/backsound/Chapter 2/alexguz-the-wild-tribal-war_full_vocal_version-ethnic-east-african-386467.mp3" fadein 1.0
    $ boss_hp       = 3
    $ boss_attempts += 1
    $ fase1_benar   = 0
    $ fase2_benar   = 0
    $ fase3_benar   = 0

    scene bg_ch2_bertemu_ds with dissolve
    play sound "audio/sfx/chapter 2/8.suara corrupted audio.mp3"

    $ _skipping = False
    show screen radar_roh_screen(level=2)
    $ renpy.pause(2.0, hard=True)
    $ _skipping = True

    $ _skipping = False
    show screen state_roh_screen("WASPADA")
    $ renpy.pause(2.0, hard=True)
    $ _skipping = True

    centered "Dursasana tersenyum kecil sambil berjalan mendekat perlahan."

    scene bg_ch2_sebelum_ds with dissolve

    show ds_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    ds "Jadii… manusia ini yang sudah membuat keributan di arenaku."
    hide ds_talk

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Dan kau adalah boss kedua nya?"
    hide k_talk

    show ds_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    ds "Aku sudah melihat semua yang kau lakukan sejak awal masuk ke dunia ini."
    ds "Cara bertarungmu ceroboh, emosimu juga gampang dibaca."
    ds "Manusia seperti dirimu tidak akan bertahan lama disini."
    hide ds_talk

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Yeahh, itulah alasan mereka menyebutku manusia."
    hide k_smile

    show ds_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    ds "HAHAHAHA… apakah segampang itu ya mancing emosi manusia?"
    ds "Pantas saja gerakan kau jadi berantakan."
    ds "Dasar daging bodoh bertulang yang bahkan tanah pun najis memberi sentuhan suci yang dibaluti"
    ds "nirwana kesucian yang menjadi bernoda menjijikan karena makhluk rendahan yang tak pantas menghirup anugrah kehidupan sepertiku,"
    ds "dan kau bangga dengan semua itu?!."
    ds "Kau bahkan tidak pantas berada di dunia ini, kau adalah makhluk hina yang tercipta dari tanah. "
    hide ds_talk

    centered "Wara mulai kesal mendengar ucapan itu."

    scene bg_ch2_sebelum_ds with dissolve

    show ds_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    ds "Atau mungkin… kau mulai lemah karena terlalu memikirkan AI itu?"
    hide ds_talk

    centered "Dursasana melirik ke arah As-leen sambil tersenyum tipis."
    centered "Dan tanpa sadar wara langsung terpancing."

    scene bg_ch2_lawan_ds with dissolve

    k "Tutup mulutmu dan jangan pernah kau membawa-bawa As-leen."
    k "Aku peringatkan kau sekali lagi!"

    ds "HAHAHAHAHA baru sedikit aku memancing emosimu. dan kau langsung terbawa?"
    ds "Kalau pikiranmu sudah kacau begini, jadi harus darimana aku menyerangmu?"

    play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"

    scene bg_ch2_lawan_ds with dissolve

    centered "Tiba tiba Dursasana langsung menyerang cepat."
    centered "Wara nyaris terkena pukulan itu dan buru buru mundur."
    centered "Pertarungan pun dimulai."
    centered "Dursasana terus menyerang sambil terus memancing emosi wara."

    scene bg_ch2_sebelum_ds with dissolve

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Wara, dia melempar data serangan langsung ke pikiranmu!"
    a "Kamu harus jawab dengan benar, itu satu-satunya cara menyerangnya balik."
    a "Kalau salah, serangannya akan menghantammu lebih keras!"
    hide a_talk

    centered "── FASE 1: Kenali Pola Serangan ──"

label ds_soal_1:
    show screen soal_panel(
        nomor="1",
        tema="Python – Kondisional",
        kode="nilai = 50\nif nilai >= 60:\n    print('Lulus')\nelse:\n    print('Tidak Lulus')",
        pertanyaan="Apa output dari program tersebut?"
    )

    menu:
        "Lulus":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "AUGH— Bukan Lulus! 50 tidak memenuhi syarat >= 60!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Nilai 50 tidak memenuhi kondisi >= 60. Coba soal lebih mudah dulu!"
            hide a_talk
            jump ds_cadangan_1

        "Tidak Lulus":
            hide screen soal_panel
            $ fase1_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "TIDAK LULUS! 50 tidak >= 60, jadi masuk ke blok else!"
            k "SERANG BALIK SEKARANG!"
            hide k_angrytalk
            play sound "audio/sfx/chapter 2/4.suara earthquake.mp3"
            show ds_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            ds "GUH—! Tidak mungkin kau tahu itu...!"
            hide ds_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Bagus! Serangan pertama mengenai. Dia mulai goyah!"
            hide a_talk

        "Lulus dan Tidak Lulus (dua baris)":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Dua baris?! if/else tidak pernah menjalankan keduanya sekaligus!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "if/else hanya menjalankan SALAH SATU blok. Coba soal lebih mudah dulu!"
            hide a_talk
            jump ds_cadangan_1

        "Program tidak menghasilkan output":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Tidak ada output?! Pasti ada output—else pasti dijalankan!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Selama kondisi if False, blok else PASTI jalan. Coba soal lebih mudah!"
            hide a_talk
            jump ds_cadangan_1


label ds_soal_2:
    show screen soal_panel(
        nomor="2",
        tema="Sejarah – Orde Baru",
        kode="",
        pertanyaan="Program KB (Keluarga Berencana) yang gencar\ndijalankan Orde Baru bertujuan untuk..."
    )

    menu:
        "Meningkatkan jumlah penduduk agar tenaga kerja melimpah":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Salah! KB justru MENEKAN pertumbuhan, bukan menambah!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Slogan 'Dua Anak Cukup' — itu petunjuknya! Coba soal lebih mudah!"
            hide a_talk
            jump ds_cadangan_2

        "Mengendalikan laju pertumbuhan penduduk yang terlalu cepat":
            hide screen soal_panel
            $ fase1_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "MENGENDALIKAN PERTUMBUHAN PENDUDUK!"
            k "'Dua Anak Cukup'—slogan yang berhasil turunkan angka kelahiran!"
            k "Ini untuk kamu, Dursasana!"
            hide k_angrytalk
            play sound "audio/sfx/chapter 2/4.suara earthquake.mp3"
            show ds_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            ds "NGHH— Kau tahu sejarah juga?!"
            hide ds_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Dua serangan mengenai! Dursasana mulai kewalahan!"
            hide a_talk

        "Memindahkan penduduk dari Jawa ke luar Jawa":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Itu Transmigrasi, bukan KB!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Transmigrasi itu program berbeda. Coba soal lebih mudah dulu!"
            hide a_talk
            jump ds_cadangan_2

        "Meningkatkan angka kelahiran di daerah terpencil":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Meningkatkan kelahiran?! Justru sebaliknya!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "KB = MENEKAN kelahiran, bukan menambah! Coba soal lebih mudah!"
            hide a_talk
            jump ds_cadangan_2

    if fase1_benar >= 2:
        show k_angrytalk at Position(xalign=0.5, yalign=0.3) with dissolve
        k "Aku mulai bisa membaca gerakanmu, Dursasana."
        k "Setiap serangan datamu… aku akan patahkan satu per satu."
        hide k_angrytalk

    jump boss_dursasana_fase2

label ds_cadangan_1:
    show screen soal_panel(
        nomor="1C",
        tema="Python – Kondisional elif",
        kode="nilai = 75\nif nilai >= 85:\n    print('A')\nelif nilai >= 70:\n    print('B')\nelse:\n    print('C')",
        pertanyaan="Apa output dari program tersebut?"
    )

    menu:
        "A":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "A?! 75 tidak memenuhi >= 85!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "75 bukan >= 85. Cek kondisi elif-nya dulu!"
            hide a_talk
            jump ds_cadangan_1

        "B":
            hide screen soal_panel
            $ fase1_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "B! 75 tidak >= 85, tapi 75 >= 70—masuk elif!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Sekarang lanjut ke soal berikutnya!"
            hide a_talk
            jump ds_soal_2

        "C":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "C?! Masih ada elif yang terpenuhi sebelum else!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "75 >= 70 adalah True! elif terpenuhi, jadi bukan else!"
            hide a_talk
            jump ds_cadangan_1

        "AB":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "if/elif/else hanya jalankan SATU blok!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tidak mungkin dua output sekaligus dari if/elif/else!"
            hide a_talk
            jump ds_cadangan_1


label ds_cadangan_2:
    show screen soal_panel(
        nomor="2C",
        tema="Sejarah – Orde Baru",
        kode="",
        pertanyaan="Penerapan Asas Tunggal Pancasila pada\nmasa Orde Baru mewajibkan..."
    )

    menu:
        "Semua warga negara menghafal seluruh pasal UUD 1945":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Hafal UUD?! Bukan itu tujuan Asas Tunggal!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Asas Tunggal soal ORGANISASI, bukan hafalan UUD!"
            hide a_talk
            jump ds_cadangan_2

        "Semua organisasi masyarakat dan partai politik berasaskan Pancasila":
            hide screen soal_panel
            $ fase1_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "Semua ormas dan parpol WAJIB berasaskan Pancasila!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Sekarang lanjut ke soal berikutnya!"
            hide a_talk
            jump ds_soal_3

        "Semua pegawai negeri menjadi anggota partai Golkar":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Itu monoloyalitas PNS, bukan Asas Tunggal!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Asas Tunggal berbeda dengan kebijakan PNS ke Golkar!"
            hide a_talk
            jump ds_cadangan_2

        "Semua sekolah mengajarkan P4 sebagai mata pelajaran wajib":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "P4 itu program penataran, bukan Asas Tunggal!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "P4 dan Asas Tunggal itu kebijakan berbeda!"
            hide a_talk
            jump ds_cadangan_2

label boss_dursasana_fase2:
    play music "audio/backsound/Chapter 2/solarflex-film-film-movie-soundtrack-music-504963.mp3" fadein 1.0
    hide screen state_roh_screen

    show effect_8 at truecenter with dissolve
    pause 3.0
    scene bg_ch2_sebelum_ds with dissolve

    centered "── FASE 2: RAGE STATE — Dursasana Mengamuk! ──"

    show ds_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    ds "CUKUP!!"
    ds "Aku tidak akan main-main lagi!"
    ds "Rasakan kekuatan sebenarnya dariku, manusia rendahan!"
    hide ds_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Wara, hati-hati! Rage State aktif—serangannya makin brutal sekarang!"
    hide a_talk

    show k_angrytalk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Semakin brutal?"
    k "Bagus. Aku juga tidak akan menahan diri."
    hide k_angrytalk


label ds_soal_3:
    show screen soal_panel(
        nomor="3",
        tema="Python – Perulangan for",
        kode="for i in range(1, 5):\n    print(i, end=' ')",
        pertanyaan="Apa output dari program tersebut?"
    )

    menu:
        "1 2 3 4":
            hide screen soal_panel
            $ fase2_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "1 2 3 4! range(1,5) mulai dari 1 sampai 4—tidak termasuk 5!"
            k "end=' ' bikin semua nempel di satu baris!"
            k "INI UNTUK KAMU DURSASANA!"
            hide k_angrytalk
            play sound "audio/sfx/chapter 2/4.suara earthquake.mp3"
            show ds_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            ds "GRAAAAHHH— Tidak mungkin kau tahu range!!"
            hide ds_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat sasaran! Fase 2 dimulai dengan kuat!"
            hide a_talk

        "1 2 3 4 5":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "ADUHH— range(1,5) tidak termasuk angka 5!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "range berhenti di stop-1. Coba soal lebih mudah dulu!"
            hide a_talk
            jump ds_cadangan_3

        "0 1 2 3":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Mulai dari 0?! range(1,5) mulai dari 1, bukan 0!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "range(1,5) mulai dari 1! Coba soal lebih mudah dulu!"
            hide a_talk
            jump ds_cadangan_3

        "1 2 3":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Hanya 3 angka?! range(1,5) menghasilkan 4 angka!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Ada 4 angka: 1,2,3,4. Coba soal lebih mudah dulu!"
            hide a_talk
            jump ds_cadangan_3


label ds_soal_4:
    show screen soal_panel(
        nomor="4",
        tema="Sejarah – Orde Baru",
        kode="",
        pertanyaan="Salah satu dampak positif program Repelita\npada masa Orde Baru adalah..."
    )

    menu:
        "Kebebasan pers yang semakin luas":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "BUKAN! Orde Baru justru MEMBATASI kebebasan pers!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Orde Baru represif terhadap media. Coba soal lebih mudah!"
            hide a_talk
            jump ds_cadangan_4

        "Tercapainya swasembada beras pada tahun 1984":
            hide screen soal_panel
            $ fase2_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "SWASEMBADA BERAS 1984!"
            k "Indonesia bahkan dapat penghargaan FAO karena keberhasilan ini!"
            k "Sekarang aku tidak akan beri kau waktu bernapas, Dursasana!"
            hide k_angrytalk
            play sound "audio/sfx/chapter 2/4.suara earthquake.mp3"
            show ds_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            ds "NGGHH— MUSTAHIL! Kau benar-benar tahu sejarah?!"
            hide ds_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Fase 2 selesai! Dursasana tersudut. Satu fase lagi!"
            hide a_talk

        "Penghapusan kesenjangan ekonomi kota dan desa":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Aduh! Kesenjangan justru masih jadi masalah besar!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Ingat penghargaan FAO! Coba soal lebih mudah dulu!"
            hide a_talk
            jump ds_cadangan_4

        "Terbukanya sistem multipartai yang bebas":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Multipartai bebas?! Orde Baru sangat MEMBATASI partai politik!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Orde Baru hanya izinkan 3 partai! Coba soal lebih mudah!"
            hide a_talk
            jump ds_cadangan_4

    if fase2_benar >= 1:
        show k_angrytalk at Position(xalign=0.5, yalign=0.3) with dissolve
        k "Aku tidak punya waktu untuk lemah di sini."
        k "Ini bukan hanya soal kemenangan, ini soal kembalinya wayang bapakku."
        hide k_angrytalk

    jump boss_dursasana_fase3


label ds_cadangan_3:
    show screen soal_panel(
        nomor="3C",
        tema="Python – Perulangan while",
        kode="n = 1\nwhile n <= 4:\n    print(n, end=' ')\n    n += 1",
        pertanyaan="Apa output dari program tersebut?"
    )

    menu:
        "1 2 3 4 5":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "5?! Saat n=5, kondisi n<=4 sudah False—loop berhenti!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "while berhenti saat kondisi False. n=5 tidak memenuhi n<=4!"
            hide a_talk
            jump ds_cadangan_3

        "1 2 3 4":
            hide screen soal_panel
            $ fase2_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "1 2 3 4! while berhenti saat n=5 karena 5 > 4!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Sekarang lanjut ke soal berikutnya!"
            hide a_talk
            jump ds_soal_4

        "0 1 2 3 4":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Mulai dari 0?! n dimulai dari 1, bukan 0!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Perhatikan: n = 1 di awal. Bukan 0!"
            hide a_talk
            jump ds_cadangan_3

        "2 3 4 5":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Mulai dari 2?! n dimulai dari 1!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "n = 1 di awal! Loop dimulai dari 1, dan 5 tidak masuk!"
            hide a_talk
            jump ds_cadangan_3


label ds_cadangan_4:
    show screen soal_panel(
        nomor="4C",
        tema="Sejarah – Orde Baru",
        kode="",
        pertanyaan="Program Transmigrasi yang digalakkan pada\nmasa Orde Baru bertujuan utama untuk..."
    )

    menu:
        "Meratakan persebaran penduduk yang terkonsentrasi di Pulau Jawa":
            hide screen soal_panel
            $ fase2_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "Pemerataan penduduk! Jawa terlalu padat, dipindah ke luar Jawa!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Sekarang lanjut ke soal berikutnya!"
            hide a_talk
            jump ds_soal_5

        "Memperluas wilayah Indonesia ke pulau-pulau terpencil":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Memperluas wilayah?! Indonesia tidak perlu memperluas!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Transmigrasi soal PEMERATAAN penduduk, bukan perluasan wilayah!"
            hide a_talk
            jump ds_cadangan_4

        "Mengembangkan sektor pariwisata di daerah tujuan":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Pariwisata?! Transmigrasi itu soal PENDUDUK bukan wisata!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Fokus Transmigrasi adalah memindahkan penduduk dan membuka lahan!"
            hide a_talk
            jump ds_cadangan_4

        "Menciptakan pusat-pusat industri baru di luar Jawa":
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Industri baru?! Tujuan utamanya bukan itu!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Transmigrasi = pemerataan penduduk + membuka lahan pertanian!"
            hide a_talk
            jump ds_cadangan_4

label boss_dursasana_fase3_retry:
    $ fase3_benar = 0
    hide screen timer_screen
    hide screen radar_roh_screen
    hide screen state_roh_screen
    hide screen soal_panel

    scene bg_ch2_sebelum_ds with dissolve

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Kita masih bisa, Wara! Dursasana sudah lemah—tinggal serangan terakhir!"
    hide a_talk


label boss_dursasana_fase3:
    play music "audio/backsound/Chapter 2/sidikdibyo-gamelan-sound-362886.mp3" fadein 1.0
    hide screen state_roh_screen
    show screen state_roh_screen("marah")
    pause 1.0

    show effect_3 at truecenter with dissolve
    pause 3.0
    scene bg_ch2_sebelum_ds with dissolve

    centered "── FASE 3: ENRAGED MODE — Chaos Pressure! ──"

    show ds_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    ds "TIDAK... TIDAK TIDAK TIDAK!"
    ds "KALAU BEGITU AKU AKAN MENGHANCURKAN SEMUANYA BERSAMAMU!"
    hide ds_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Wara! Enraged Mode ini yang paling berbahaya!"
    a "Tapi kita sudah sejauh ini. Jangan mundur sekarang!"
    hide a_talk

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "Mundur?"
    k "Aku tidak datang ke sini untuk mundur."
    k "Ini pertarungan terakhir, Dursasana. Bersiaplah."
    hide k_angrytalk


label ds_soal_5:
    show screen timer_screen(length=25.0, on_timeout="waktu_habis_boss_ds")
    show screen soal_panel(
        nomor="5 – TERAKHIR",
        tema="Python – Perulangan & Kondisional",
        kode="for i in range(1, 6):\n    if i %% 2 == 0:\n        print(i, end=' ')",
        pertanyaan="Apa output dari program tersebut?"
    )

    menu:
        "1 3 5":
            hide screen timer_screen
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "BUKAN! i %% 2 == 0 itu kondisi GENAP, bukan ganjil!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "%% 2 == 0 artinya GENAP. Coba soal serupa dulu!"
            hide a_talk
            jump ds_cadangan_5

        "2 4":
            hide screen timer_screen
            hide screen soal_panel
            $ fase3_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "2 DAN 4!"
            k "range(1,6) hasilkan 1-5. Yang habis dibagi 2 cuma 2 dan 4!"
            k "INI SERANGANKU YANG TERAKHIR UNTUKMU, DURSASANA!!!"
            hide k_angrytalk
            play sound "audio/sfx/chapter 2/4.suara earthquake.mp3"
            jump boss_dursasana_menang

        "2 4 6":
            hide scree
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "6?! range(1,6) berhenti di 5—angka 6 tidak ada!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "range(1,6) = 1 s/d 5. Coba soal serupa dulu!"
            hide a_talk
            jump ds_cadangan_5

        "1 2 3 4 5":
            hide scree
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Semua angka?! Ada kondisi if-nya—tidak semua angka lolos!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "i %% 2 == 0 menyaring hanya bilangan genap. Coba soal serupa!"
            hide a_talk
            jump ds_cadangan_5


label ds_cadangan_5:
    show scree(length=25.0, on_timeout="waktu_habis_boss_ds")
    show screen soal_panel(
        nomor="5C",
        tema="Python – Kondisional Bersarang",
        kode="x = 10\nif x > 5:\n    if x > 15:\n        print('Besar')\n    else:\n        print('Sedang')\nelse:\n    print('Kecil')",
        pertanyaan="Apa output dari program tersebut?"
    )

    menu:
        "Besar":
            hide scree
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Besar?! 10 > 15 adalah False!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "x=10, bukan > 15. Jadi masuk else dalam—bukan Besar!"
            hide a_talk
            jump ds_cadangan_5

        "Sedang":
            hide scree
            hide screen soal_panel
            $ fase3_benar += 1
            $ quiz_score  += 1
            show screen feedback_screen("berhasil")
            pause 1.6
            hide screen feedback_screen
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            k "SEDANG! 10 > 5 True, tapi 10 > 15 False—masuk else dalam!"
            hide k_angrytalk
            play sound "audio/sfx/chapter 2/4.suara earthquake.mp3"
            show ds_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
            ds "GRAAAHHHH— Tidak mungkin... tidak... MUNGKIN!"
            hide ds_talk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tepat! Sekarang HABISI DIA dengan serangan terakhirmu!"
            hide a_talk
            jump boss_dursasana_menang

        "Kecil":
            hide scree
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Kecil?! 10 > 5 adalah True, jadi tidak masuk else luar!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "10 > 5 = True! Masuk if luar dulu, baru cek if dalam!"
            hide a_talk
            jump ds_cadangan_5

        "Besar Sedang":
            hide scree
            hide screen soal_panel
            show screen feedback_screen("salah")
            pause 1.6
            hide screen feedback_screen
            play sound "audio/sfx/chapter 2/4.suara digital distortion crack.mp3"
            show k_angrytalk at Position(xalign=0.5, yalign=0.3), lompat_kaget with dissolve
            k "Dua output sekaligus?! if/else hanya jalankan SATU blok!"
            hide k_angrytalk
            show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
            a "Tidak mungkin dua output dari if/else bersarang!"
            hide a_talk
            jump ds_cadangan_5

label boss_dursasana_menang:
    hide screen radar_roh_screen
    hide scree
    stop music fadeout 0.5

    play sound "audio/sfx/chapter 2/6.suara energy shield pass.mp3"

    show k_angrytalk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    k "SELESAIKAN!!"
    hide k_angrytalk

    show ds_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    ds "AGHHH!!! tidak... MUNGKIN!"
    ds "AKU... DURSASANA..."
    hide ds_talk

    show ds_talk at Position(xalign=0.5, yalign=0.3), getar with dissolve
    ds "TIDAK MUNGKIN KALAH DARI MANUSIA SEPERTIMU!!!"
    hide ds_talk

    show effect_3 at truecenter with dissolve
    pause 3.0

    scene bg_ch2_menang_ds with dissolve
    play music "audio/backsound/Chapter 2/nala_subrada-moonlit-reverie-2026-digital-rain-wellness-ritual-454059.mp3" fadein 2.0

    centered "Retakan besar langsung menyebar ke seluruh tubuh Dursasana."
    centered "sebelum akhirnya tubuhnya pecah menjadi serpihan cahaya dan perlahan menghilang."
    centered "Arena akhirnya kembali sunyi."
    centered "Retakan cahaya ungu di sekitar ruangan perlahan mulai meredup."

    scene bg_ch2_sebelum_ds with dissolve

    play sound "audio/sfx/chapter 2/5.suara fast breathing 2.mp3"

    centered "Wara yang sejak tadi memaksakan tubuhnya akhirnya langsung jatuh duduk ke lantai."
    centered "Nafasnya tidak beraturan, tangannya gemetar, dan keringat membasahi wajahnya."

    show k_think at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Hufttt…kekuatan yang luar biasa…."
    hide k_think

    centered "Tiba tiba As-leen mendekat lalu memegang pundak wara secara perlahan."

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Kemampuan bertarung mu jauh meningkat drastis dibanding sebelumnya…"
    a "Kamu mulai bisa membaca pola lawan dan mengontrol emosimu sendiri."
    hide a_talk

    centered "Wara sedikit kaget karena tak biasanya as-leen menyentuhnya secara langsung."
    centered "Meskipun wajahnya masih datar seperti biasa, wara tau kalau sebenarnya dia khawatir."

    show k_smile at Position(xalign=0.5, yalign=0.3) with dissolve
    k "(senyum kecil)"
    k "Terima kasih untuk informasinya dan terima kasih juga karena sudah mengkhawatirkan aku."
    k "Tak biasanya kau menyentuh secara langsung seperti ini…."
    K "Terima kasih"
    hide k_smile

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Aku hanya ingin memastikan kamu masih baik baik saja setelah terkena serangan berturut-turut.."
    a "Namun, harus aku akui. kamu terlihat keren saat bertarung."
    hide a_talk

    centered "Wara tersenyum kecil lalu memegang lembut tangan as-leen sambil berdiri perlahan."

    show k_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    k "Kamu sendiri bagaimana? apakah kamu baik baik saja?"
    k "tadi aku melihat kamu sempet kena efek serangannya Dursasana."
    k "Jangan bilang tiba tiba error lagi?"
    hide k_talk

    show a_talk at Position(xalign=0.5, yalign=0.3) with dissolve
    a "Tenang aja… aku masih baik baik saja. sistemku juga masih normal."
    a "Namun saja…. navigasiku masih sedikit bermasalah sejak tadi."
    hide a_talk

    play sound "audio/sfx/chapter 2/10.suara distant echo voice.mp3"

    centered "Wara mengangguk pelan sambil menatap as-leen beberapa detik lebih lama dari biasanya."
    centered "Dan untuk pertama kalinya Wara mulai sadar kalau as-leen bukan cuma sekedar ai yang menemaninya di perjalanan ini."

    play sound "audio/sfx/chapter 2/7.suara ui beep.mp3"
    centered "── DATA ROH DURSASANA TERSIMPAN ──"
    centered "Radar Roh meningkat. Dua entitas berhasil dijinakkan."

    jump chapter2_ending


label waktu_habis_boss_ds:
    hide scree
    hide screen radar_roh_screen
    hide screen state_roh_screen
    hide screen soal_panel
    $ renpy.block_rollback()

    call screen kalah_boss_screen()

    if _return == "restart":
        jump boss_dursasana_fase3_retry
    else:
       $ renpy.full_restart()


label chapter2_ending:
    stop music fadeout 1.5

    scene bg_ch2_sebelum_ds with dissolve
    play music "audio/backsound/Chapter 2/onetent-samurai-flutes-ethereal-fantasy-flute-relaxing-meditation-music-248255.mp3" fadein 2.0

    centered "── CHAPTER 2 SELESAI ──"
    centered "\"Perburuan Fajar\""

    centered "Perjalanan Kreswara masih panjang."
    centered "Boss berikutnya: Sengkuni — Tema Jebakan & Manipulasi."
    centered "Sampai jumpa di Chapter 3: Jebakan di Balik Ketenangan."

    pause 1.5
    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    pause 1.0

    $ persistent.chapter3_unlocked = True
    $ renpy.full_restart()