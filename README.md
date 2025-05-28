# Freebie Tracker

A Python app using SQLAlchemy to track freebies collected by developers from various companies.

## Requirements

* Python 3.8+
* Pipenv
* SQLite 
## Setup

1. Install dependencies:

2. Create the database directory:

3. Run the migration to create tables:

## Seeding Data

Populate the database with sample Companies, Devs, and Freebies:


## Debug & Inspect

Use the interactive debugger to explore your ORM models:


At the `(Pdb)` prompt, try commands like:

```
p all_companies
p all_devs
p all_freebies
```

## Model Overview

* **Company**: `id`, `name`, `founding_year`, relationships to `Freebie` and `Dev`.
* **Dev**: `id`, `name`, relationships to `Freebie` and `Company`.
* **Freebie**: `id`, `item_name`, `value`, foreign keys to `Dev` and `Company`.

