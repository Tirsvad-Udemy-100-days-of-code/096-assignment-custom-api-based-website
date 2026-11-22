[English](Reflection) · **Dansk** · [Bahasa Malaysia](Reflection-ms)

# Refleksion

## Hvordan greb jeg opgaven an?

Jeg planlagde først: en business case, interessenter, en projektplan og fem milepæle, hver gennemgået før kode. Derefter byggede jeg websitet i lag med tests for hvert lag og tog skærmbillederne i Docker-containere, så ingen skærm var nødvendig.

## Hvad var svært?

Lektionens API findes ikke mere, så første opgave var at finde et, der virker. CI-kontrollerne var også strengere end mine lokale kontroller, for eksempel værktøjet til statisk analyse og linjeskift i shell-scripts.

## Hvad var let?

Selve Flask. Ruter, skabeloner og fejlhåndtering krævede meget lidt kode, da klienten og domænet var adskilt.

## Hvad vil jeg forbedre?

Skifte til PotterDB-API'et, som har serverfilter på hus og sideinddeling, så websitet ikke henter alle figurer for at vise ét hus. Desuden cache af API-svar.

## Hvad var den største læring?

Afhæng af en port, ikke af en tjeneste. Når API'et fejler eller ændres, ændres kun infrastrukturlaget.

## Hvad vil jeg gøre anderledes?

Undersøge kandidat-API'erne grundigere, før jeg skriver beslutningen; min første beslutning sagde, at PotterDB ikke havde et husfilter, og det var forkert.
