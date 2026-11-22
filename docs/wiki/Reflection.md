**English** · [Dansk](Reflection-da) · [Bahasa Malaysia](Reflection-ms)

# Reflection

## How did I approach the assignment?

I planned first: a business case, stakeholders, a project plan and five milestones, each reviewed before code. Then I built the site in layers, with tests for each layer, and took the screenshots in Docker containers so no desktop was needed.

## What was hard?

The lecture's API no longer exists, so the first job was finding a working one. The continuous-integration checks were also stricter than my local checks, for example the static analysis tool and the line endings of shell scripts.

## What was easy?

Flask itself. Routes, templates and error handlers needed very little code once the client and the domain were separate.

## What would I improve?

Switch to the PotterDB API, which offers a server-side house filter and pagination, so the site does not load every character to show one house. Also add caching of API answers.

## What was the biggest learning?

Depend on a port, not on a service. When the API fails or changes, only the infrastructure layer changes.

## What would I do differently?

Check the candidate APIs more carefully before writing the decision record; my first record said PotterDB had no house filter, which was wrong.
