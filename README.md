# GrundlagenProgrammierenGruppeA
This program is intended to become a personal movie manager. Movies should be able to be rated and filtered and displayed according to specific criteria.

# Rate my movies

This Python console application provides an easy way to manage a list of movies that you want to watch or have watched and want to rate. A dedicated search and filter mechanism allows you to get an overview of the films you need. You will also have the possibility to share your lists with others.

## Authors
- Leonit Kaup
- Jonathan Engel
- Léon Albert


## Organisation of User Stories
We have created and organized our user stories as GitHub Issues and added a dedicated label and a uniform template to use GitHub as our centralized project organization platform.

### Labels
In addition to the "User Story" label, we created a "Setup Init" label to identify and assign work that differs from the user stories:
![alt text](image.png)

### Template
Our user story template follows the pattern "As a …, I want to …, so that …" and includes clearly defined acceptance criteria.

### User Stories 
#### [Filter and Sort Movies](https://github.com/leonidkaup/GrundlagenProgrammierenGruppeA/issues/13)
*Explanation:* As a user, I should not only be able to print my entire movie list, as this can become difficult to navigate when it contains many entries. Filtering and sorting help me identify the highest and lowest rated movies or find a specific movie when deciding whether to recommend it to a friend.
#### [Rate a Movie](https://github.com/leonidkaup/GrundlagenProgrammierenGruppeA/issues/12)
*Explanation:*
#### [Read a Movie](https://github.com/leonidkaup/GrundlagenProgrammierenGruppeA/issues/11)
*Explanation:*
#### [Update a Movie](https://github.com/leonidkaup/GrundlagenProgrammierenGruppeA/issues/10)
*Explanation:*
#### [Delete a Movie](https://github.com/leonidkaup/GrundlagenProgrammierenGruppeA/issues/9)
*Explanation:*
#### [Create a Movie](https://github.com/leonidkaup/GrundlagenProgrammierenGruppeA/issues/8)
*Explanation:*
#### [Export a Movie List](https://github.com/leonidkaup/GrundlagenProgrammierenGruppeA/issues/7)
*Explanation:* This feature allows users to share their current movie list with a friend, eliminating the need to enter every movie manually. It can also be used to provide a friend with a ready-made watchlist or print the list as a PDF, allowing users to share it in a readable format or keep it as a semi-structured personal record. also you can print it as a pdf in order shre it in a way another person can actually read it or yourself wiith beeing in a semi structured format.
#### [Persist the Current Movie List](https://github.com/leonidkaup/GrundlagenProgrammierenGruppeA/issues/6)
Explenation:
#### [Import a Movie List](https://github.com/leonidkaup/GrundlagenProgrammierenGruppeA/issues/5)
Explenation: 
#### [Movie List Gets Imported](https://github.com/leonidkaup/GrundlagenProgrammierenGruppeA/issues/4)
Explanation: Importing lists from friends or the internet allows users to add movies without entering every title manually and helps build a comprehensive movie library.
## Implementation Documentation
### Data Model and Film Object
### Data Validation
### Error Handling
### File Processing

## Team & Contributions


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
