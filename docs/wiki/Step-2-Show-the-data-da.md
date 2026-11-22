[English](Step-2-Show-the-data) · **Dansk** · [Bahasa Malaysia](Step-2-Show-the-data-ms)

# Trin 2: Vis data

## Hvad trinnet er

Forsiden laver det første kald og viser alle figurer.

## Hvad jeg gjorde

En lille HTTP-klient henter JSON og laver hver post om til et `Character`-objekt. Flask-viewet modtager kun figurer og tegner en skabelon.

## Hvad jeg lærte

Når netværkskaldet ligger uden for viewet, kan siden testes med en falsk klient, så testene aldrig kalder internettet.

## Skærmbillede

![Trin 2: Vis data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/raw/branch/main/docs/images/step-2-all-characters.png)
