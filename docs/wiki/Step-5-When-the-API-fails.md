**English** · [Dansk](Step-5-When-the-API-fails-da) · [Bahasa Malaysia](Step-5-When-the-API-fails-ms)

# Step 5: When the API fails

## What this step is

A visitor should get a clear message when the API is down, not a stack trace.

## What was done

Network errors, timeouts and bad JSON all become one `ApiUnavailableError`. The website maps it to a friendly page with status 503.

## What was gained

One domain error for every failure keeps the presentation layer simple. Failure is a normal case to test, not an exception to ignore.

## Screenshot

![Step 5: When the API fails](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/raw/branch/main/docs/images/step-5-api-unavailable.png)
