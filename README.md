# GrundlagenProgrammierenGruppeA
This program is intended to become a personal movie manager. Movies should be able to be rated and filtered and displayed according to specific criteria.

# Rate my movies

This Python console application provides an easy way to manage a list of movies that you want to watch or have watched and want to rate. A dedicated search and filter mechanism allows you to get an overview of the films you need. You will also have the possibility to share your lists with others.

## Features

- Create new movies
- View the movie collection
- Update existing movies
- Delete movies
- Rate movies
- Search movies by title
- Filter movies by genre or contributor
- Sort movies by rating
- Display the top or bottom X rated movies
- Import movie data from a file
- Export movie data to a file
- Persist movie data between application runs
- Validate user input and imported data

## Installation

### Requirements

- Python 3.x
- Required Python packages are listed in `requirements.txt`

### Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Start the application with:

```bash
python main.py
```

The application is controlled through an interactive console menu.

## Syntax
- Variables and functions: lowercase_with_underscores
- Classes: CamelCase
- Constants: UPPERCASE_WITH_UNDERSCORES
- Catch the most specific exceptions possible; avoid 'except:' without type

## Project Structure

```text
project/
├── main.py
├── README.md
├── models/
│   ├── ...
│   └── ...
├── services/
│   └── ...
└── storage/
    └── ...
```

The exact structure may change during development.

## Data

Movie data is stored persistently so that the collection is available again after restarting the application.

The application also supports importing and exporting movie data.

## Validation & Error Handling

User input and data loaded from files are validated before being processed. Invalid input is handled without unexpectedly terminating the application.

## Development

The project is developed collaboratively using Git and GitHub. Features and requirements are tracked using GitHub Issues and User Stories with Acceptance Criteria.

## Authors
- Leonit Kaup
- Jonathan Engel
- Léon Albert
