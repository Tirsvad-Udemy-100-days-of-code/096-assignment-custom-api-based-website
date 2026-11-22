[English](Step-3-Filter-by-house) · **Dansk** · [Bahasa Malaysia](Step-3-Filter-by-house-ms)

# Trin 3: Filtrér efter hus

## Hvad trinnet er

Ruten `/house/<name>` viser figurerne i ét hus.

## Hvad jeg gjorde

Filteret er en parameter på klientens port. API'et har intet filter på serveren, så klienten filtrerer listen, og et ukendt hus giver en ren 404-side.

## Hvad jeg lærte

At validere input mod en kendt liste (de fire huse i `constants.py`) er enklere og sikrere end at stole på URL'en.

## Skærmbillede

![Trin 3: Filtrér efter hus](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/raw/branch/main/docs/images/step-3-house-filter.png)
