# Pembukaan

Guide Book ini memuat beberapa informasi-informasi utama yang akan disampaikan oleh mentor di program AI Career Bootcamp yang bisa dijadikan pegangan para students untuk mempersiapkan diri sebelum sesi Live Class berlangsung.

# Deskripsi

Deep Learning pada Natural Language Processing (NLP) adalah cabang ilmu kecerdasan buatan yang menggunakan algoritma pembelajaran mesin berbasis jaringan saraf tiruan (neural networks) untuk memproses dan memahami bahasa manusia secara alami. Tujuan utamanya adalah untuk mengenali, menerjemahkan, dan menghasilkan teks manusia dengan cara yang mirip dengan kemampuan manusia.

Deep Learning dalam NLP memungkinkan komputer untuk memahami teks dalam konteks dan memperoleh representasi yang lebih kaya dari kata-kata dan frasa. Ini memungkinkan model NLP untuk menangani tugas-tugas kompleks seperti pemahaman bahasa, analisis sentimen, penerjemahan mesin, pengenalan entitas bernama, dan lainnya.

Penting untuk memahami bahwa NLP dengan Deep Learning membutuhkan sejumlah besar data latihan untuk melatih model agar bisa mengenali pola dan fitur bahasa yang kompleks. Selain itu, perkembangan besar dalam kekuatan komputasi, terutama GPU, telah memainkan peran penting dalam kemajuan dan keberhasilan metode deep learning di bidang NLP. Dengan terus berkembangnya teknologi ini, diharapkan kemampuan komputer untuk berinteraksi dan memahami bahasa manusia semakin meningkat di masa depan.

Beberapa algoritma Deep Learning yang populer untuk NLP yaitu Recurrent Neural Networks (RNN), Long Short-Term Memory (LSTM), Transformer, BERT (Bidirectional Encoder Representations from Transformers), GPT (Generative Pre-trained Transformer).

# Sequence to Sequence Model

Sequence-to-Sequence (Seq2Seq) model adalah arsitektur deep learning yang dirancang untuk menangani tugas-tugas berbasis urutan atau tugas-tugas "sequence-to-sequence" dalam pemrosesan bahasa alami dan bidang lainnya. Arsitektur ini memungkinkan model untuk menerima urutan data masukan dan menghasilkan urutan data keluaran yang sesuai.

Contoh umum penerapan Sequence-to-Sequence model adalah dalam terjemahan mesin (machine translation), generasi teks, ringkasan dokumen, dan pertanyaan-jawaban. Prosesnya melibatkan dua komponen utama:

1. Encoder: Komponen ini bertugas untuk mengambil urutan data masukan dan mengenali pola atau informasi penting di dalamnya. Biasanya, bagian ini menggunakan RNN (seperti LSTM atau GRU) atau Transformer untuk mengkodekan urutan data masukan ke dalam representasi numerik yang kaya dan kompak.

2. Decoder: Setelah data masukan dikodekan, komponen decoder akan menerjemahkan representasi numerik tersebut menjadi urutan data keluaran yang sesuai. Dalam kasus terjemahan mesin, decoder akan menggunakan urutan representasi untuk menghasilkan urutan teks yang merupakan terjemahan dari teks masukan.

Proses utama dalam Sequence-to-Sequence model melibatkan melatih model dengan menggunakan data pasangan urutan masukan dan keluaran yang sesuai. Selama pelatihan, model belajar menemukan hubungan antara teks masukan dan keluaran yang benar, sehingga saat diberikan masukan yang belum pernah dilihat sebelumnya, model dapat menghasilkan keluaran yang relevan.

Beberapa variasi dan pengembangan dari Seq2Seq model termasuk penggunaan attention mechanism untuk memberikan perhatian lebih pada bagian penting dari urutan masukan saat melakukan dekoding, serta metode enkode-dekode berbasis Transformer seperti yang digunakan dalam BERT dan GPT yang telah mencatat kemajuan besar dalam pemrosesan bahasa alami.

Dengan keberhasilannya dalam tugas-tugas berbasis urutan, Sequence-to-Sequence model telah menjadi salah satu arsitektur yang sangat penting dalam bidang pemrosesan bahasa alami dan berbagai aplikasi yang melibatkan data berurutan.

# Transformer Model

Transformer adalah seperti otak buatan untuk memahami dan menghasilkan teks. Bayangkan Anda memberikan teks dalam bahasa Inggris kepada Transformer dan bertanya padanya untuk menerjemahkannya ke bahasa Spanyol. Transformer akan belajar dari contoh-contoh terjemahan sebelumnya dan mencoba mencari pola dalam bahasa tersebut.

Salah satu hal unik tentang Transformer adalah kemampuannya untuk fokus pada kata-kata penting dalam teks. Jika Anda memberikan kalimat panjang, Transformer tidak harus membacanya secara berurutan seperti manusia. Sebaliknya, ia menggunakan "attention" atau "perhatian" untuk mengetahui hubungan antara kata-kata, sehingga dapat menangkap makna secara lebih baik.

Selain itu, Transformer juga bisa digunakan untuk membuat teks baru. Misalnya, jika Anda memberikan beberapa kalimat tentang bunga, Transformer dapat menggunakannya sebagai dasar untuk menulis paragraf lengkap tentang bunga.

Transformer telah mengubah cara komputer memahami bahasa manusia dan telah menjadi alat penting dalam banyak aplikasi, seperti terjemahan mesin, analisis teks, dan banyak lagi.
