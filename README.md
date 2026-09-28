# Rate my movies

TODO: Description

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

## Project Structure

```text
project/
├── main.py
├── requirements.txt
├── README.md
├── src/
│   ├── ...
│   └── ...
├── data/
│   └── ...
└── tests/
    └── ...
```

The exact structure may change during development.

## Data

Movie data is stored persistently so that the collection is available again after restarting the application.

The application also supports importing and exporting movie data.

## Validation & Error Handling

User input and data loaded from files are validated before being processed. Invalid input is handled without unexpectedly terminating the application.

## Testing

Automated tests are used to verify important application functionality.

Tests can be executed with:

```bash
pytest
```

## Development

The project is developed collaboratively using Git and GitHub. Features and requirements are tracked using GitHub Issues and User Stories with Acceptance Criteria.

## Authors
# GrundlagenProgrammierenGruppeA
Diese Programm soll am Schluss ein persönlicher Verwalter für Filmdaten sein.
-  Filme sollen Bewertet werden können und nach spezifischen Kriterien gefiltert und Ausgegeben werden
