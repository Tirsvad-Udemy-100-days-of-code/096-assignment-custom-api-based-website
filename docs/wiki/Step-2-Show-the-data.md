**English** · [Dansk](Step-2-Show-the-data-da) · [Bahasa Malaysia](Step-2-Show-the-data-ms)

# Step 2: Show the data

## What this step is

The home page makes the first request and lists every character.

## What was done

A small HTTP client fetches the JSON and turns each entry into a `Character` object. The Flask view only receives characters and renders a template.

## What was gained

Keeping the network call out of the view makes the page testable with a fake client, so the tests never call the internet.

## Screenshot

![Step 2: Show the data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/raw/branch/main/docs/images/step-2-all-characters.png)
