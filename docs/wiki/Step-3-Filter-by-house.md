**English** · [Dansk](Step-3-Filter-by-house-da) · [Bahasa Malaysia](Step-3-Filter-by-house-ms)

# Step 3: Filter by house

## What this step is

The route `/house/<name>` lists the characters of one house, for example `/house/gryffindor`.

## What was done

The filter is a parameter of the client port. The API has no server-side filter, so the client filters the list and an unknown house gives a clean 404 page.

## What was gained

Validating input against a known list (the four houses in `constants.py`) is simpler and safer than trusting the URL.

## Screenshot

![Step 3: Filter by house](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/raw/branch/main/docs/images/step-3-house-filter.png)
