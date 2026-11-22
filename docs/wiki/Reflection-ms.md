[English](Reflection) · [Dansk](Reflection-da) · **Bahasa Malaysia**

# Refleksi

## Bagaimana saya mendekati tugasan ini?

Saya merancang dahulu: kes perniagaan, pihak berkepentingan, pelan projek dan lima pencapaian, setiap satu disemak sebelum kod. Kemudian saya membina laman web berlapis dengan ujian untuk setiap lapisan dan mengambil tangkapan skrin dalam bekas Docker supaya tiada desktop diperlukan.

## Apa yang sukar?

API kuliah sudah tiada, jadi tugas pertama ialah mencari yang berfungsi. Semakan CI juga lebih ketat daripada semakan tempatan saya, contohnya alat analisis statik dan penghujung baris skrip shell.

## Apa yang mudah?

Flask sendiri. Laluan, templat dan pengendali ralat memerlukan sangat sedikit kod apabila klien dan domain diasingkan.

## Apa yang akan saya baiki?

Beralih kepada API PotterDB yang ada penapis asrama di pelayan dan penomboran halaman, supaya laman web tidak memuat semua watak untuk menunjukkan satu asrama. Tambah juga cache jawapan API.

## Apa pembelajaran terbesar?

Bergantung pada port, bukan pada perkhidmatan. Apabila API gagal atau berubah, hanya lapisan infrastruktur yang berubah.

## Apa yang akan saya lakukan secara berbeza?

Menyemak API calon dengan lebih teliti sebelum menulis rekod keputusan; rekod pertama saya menyatakan PotterDB tiada penapis asrama, dan itu salah.
