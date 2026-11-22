[English](Step-3-Filter-by-house) · [Dansk](Step-3-Filter-by-house-da) · **Bahasa Malaysia**

# Langkah 3: Tapis mengikut asrama

## Apa langkah ini

Laluan `/house/<name>` menyenaraikan watak satu asrama.

## Apa yang dilakukan

Penapis ialah parameter pada port klien. API tiada penapis di pelayan, jadi klien menapis senarai dan asrama yang tidak dikenali memberi halaman 404 yang kemas.

## Apa yang dipelajari

Mengesahkan input terhadap senarai yang diketahui (empat asrama dalam `constants.py`) lebih mudah dan selamat daripada mempercayai URL.

## Tangkapan skrin

![Langkah 3: Tapis mengikut asrama](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/raw/branch/main/docs/images/step-3-house-filter.png)
