[English](Step-5-When-the-API-fails) · [Dansk](Step-5-When-the-API-fails-da) · **Bahasa Malaysia**

# Langkah 5: Apabila API gagal

## Apa langkah ini

Pengunjung patut mendapat mesej yang jelas apabila API tidak berfungsi, bukan stack trace.

## Apa yang dilakukan

Ralat rangkaian, tamat masa dan JSON tidak sah semuanya menjadi satu `ApiUnavailableError`. Laman web memaparkan halaman mesra dengan status 503.

## Apa yang dipelajari

Satu ralat domain untuk semua kegagalan memudahkan lapisan pembentangan. Kegagalan ialah kes biasa untuk diuji, bukan pengecualian untuk diabaikan.

## Tangkapan skrin

![Langkah 5: Apabila API gagal](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/raw/branch/main/docs/images/step-5-api-unavailable.png)
