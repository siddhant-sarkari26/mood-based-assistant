# Mood, Entertainment & Games Assistant

## Overview

Mood, Entertainment & Games Assistant is a simple Python-based command-line application that provides users with different suggestions based on their mood and interests.

The project contains three main features: mood-based responses, entertainment/movie suggestions, and game suggestions. The application uses a menu-driven approach to allow the user to select the required option.

## Features

* **Mood**

  * Select your current mood.
  * Get a suitable response or suggestion.
  * Includes options for Happy, Sad, Quote of the Day, Bored, and Angry.

* **Entertainment**

  * Choose whether you want to watch a movie.
  * Select a movie genre such as Funny, Horror, or Thrilling.
  * Receive movie suggestions based on the selected genre.

* **Games**

  * Choose between indoor and outdoor games.
  * For indoor games, choose between online and offline games.
  * Receive game suggestions based on your selection.

## Technologies / Tools Used

* Python 3
* Git
* GitHub
* Command Line Interface (CLI)

## How to Install & Run

### 1. Clone the Repository

Paste your GitHub repository link in the command below:

```bash
git clone (https://github.com/siddhant-sarkari26/mood-based-assistant.git)
```

**Repository Link:**
`PASTE YOUR GITHUB REPOSITORY LINK HERE`

### 2. Open the Project Folder

```bash
cd YOUR_PROJECT_FOLDER_NAME
```

### 3. Run the Program

```bash
python main.py
```

The main menu will be displayed. Select the required option by entering the corresponding number.

## Testing

The project can be tested manually through the command line.

### Mood Testing

Run the program and select:

```text
1. MOOD
```

Test all available options:

```text
1 - Happy
2 - Sad
3 - Quote for the Day
4 - Bored
5 - Angry
```

Check that the program provides the corresponding response.

### Entertainment Testing

Select:

```text
2. ENTERTAINMENT
```

Test the movie preference:

```text
YES
NO
```

If `YES` is selected, test the available genres:

```text
FUNNY
HORROR
THRILLING
```

Check that the appropriate movie suggestions are displayed.

### Games Testing

Select:

```text
3. GAMES
```

Test:

```text
1 - Indoor
2 - Outdoor
```

For indoor games, test:

```text
1 - Online
2 - Offline
```

Check that the appropriate game suggestions are displayed.

### Exit Testing

Select:

```text
4. EXIT
```

and verify that the program exits the main menu.
