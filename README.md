# Selenium Zoom Bot 

This project uses the Selenium library for Python to automate the process of joining a Zoom meeting and sending chats using multiple bots.

## Requirements

In order to run this project, you will need:

- Python 3.x
- Selenium library for Python
- ChromeDriver executable

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/downloads/).
2. Install Selenium library for Python using pip:
`pip install selenium`

3. Download the ChromeDriver executable from the [official website](https://sites.google.com/chromium.org/driver/?pli=1). Make sure to download the version that matches your installed version of Google Chrome.
4. Extract the ChromeDriver executable to a location on your computer and add the location to your system's PATH environment variable.

## Usage

1. Clone or download the project from the repository.
2. Open the `config.py` file and update the following variables with your own values:
- `ZOOM_MEETING_LINK`: the link to the Zoom meeting you want to join.
- `ZOOM_MEETING_PASSWORD`: the password for the Zoom meeting.
- `BOT_NAMES`: a list of names for the bots. The number of bots that will be used is determined by the length of this list.
- `CHAT_MESSAGES`: a list of messages that will be sent by the bots.
3. Run the `zoom_bot.py` file using Python:
`python zoom_bot.py`

4. The program will open a new instance of Google Chrome and automatically join the Zoom meeting using the provided link and password.
5. The program will then send the specified number of bots to the meeting and have them send the specified chat messages.

## Notes

- The program will only send chat messages when the bots are in the meeting. If a bot leaves the meeting, it will not send any more messages.
- The program will automatically close the Google Chrome window when it is finished running. If you want to keep the window open for debugging purposes, you can comment out the line that closes the window in the `zoom_bot.py` file.
