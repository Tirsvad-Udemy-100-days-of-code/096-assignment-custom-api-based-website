[English](Step-5-When-the-API-fails) · **Dansk** · [Bahasa Malaysia](Step-5-When-the-API-fails-ms)

# Trin 5: Når API'et fejler

## Hvad trinnet er

En besøgende skal have en tydelig besked, når API'et er nede, ikke en stack trace.

## Hvad jeg gjorde

Netværksfejl, timeout og ugyldig JSON bliver alle til én `ApiUnavailableError`. Websitet viser en venlig side med status 503.

## Hvad jeg lærte

Én domænefejl for alle fejl holder præsentationslaget enkelt. Fejl er et normalt tilfælde, der skal testes, ikke en undtagelse, man ignorerer.

## Skærmbillede

![Trin 5: Når API'et fejler](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/raw/branch/main/docs/images/step-5-api-unavailable.png)
