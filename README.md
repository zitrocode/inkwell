# Inkwell 🖋️

Inkwell is a lightweight and user-friendly terminal-based text editor that enables users to edit text files directly within the terminal. The editor provides basic functionalities like opening files, saving changes, and navigating text. Additionally, Inkwell displays dynamic line numbers next to the text to make navigation and editing easier.

### Main Features

- Open files from the command line: `inkwell ./file.txt`
- Terminal-based text navigation and editing
- Dynamic line numbers displayed alongside text
- Keyboard commands for common actions like saving and quitting
- Modular and easily extendable code

This project is built on the Python [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) library, which provides a solid foundation for developing interactive terminal applications. By using this library, Inkwell can be easily extended and customized to meet specific user needs.

**NOTE**: This file was written entirely in the new code editor Inkwell.

This project is lovingly created by Oscar Ortiz for the community, with a focus on providing a useful and enjoyable terminal text editor experience.

### Installation

1. Clone this repository to your local machine:

```bash
> git clone https://github.com/your_username/inkwell.git
```
2. Change to the project directory:
```
> cd inkwell
```
3. Create a virtual environment and activate it:
```
> python -m venv env
> source env/bin/activate  # On Windows, use `env\Scripts\activate.ps1`
```
4. Install the required dependencies:
```
> pip install -r requirements.txt
```

### Usage
To use Inkwell, simply run the `./main.py` script with the file you want to open:
```
> python -m ./main.py ./file.txt
```

Replace ./file.txt with the path to the file you want to edit.

Use the following keyboard commands to interact with the editor:

- `CTRL+Q`: Quit the editor
- `CTRL+S`: Save changes

#### Note
This project is currently in the "0.1.0-alpha" version.
