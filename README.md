# Telegram Bot

This is a Python-based Telegram bot built using the `pyTelegramBotAPI` library. The bot performs various tasks such as responding to commands, echoing messages, handling images, and providing interactive inline buttons (e.g., deleting photos, editing text, or opening a website).

---

### Table of Contents
1. [Features](#features)
2. [Setup Instructions](#setup-instructions)
3. [Commands](#commands)
4. [Contributing](#contributing)
5. [License](#license)

---

## Features

- **Respond to Commands**:
  - `/start`: Sends a greeting message to the user.
  - `/help`: Lists all bot commands.
  - `/echo`: Echoes back the message the user sent.

- **Inline Buttons**: Supports inline buttons for images:
  - Open a website.
  - Delete a specific message/photo.
  - Edit the text of the message.

- **Dynamic Reply to Unsupported Commands**:  
  - If the user enters an unsupported command or sends unclear input, the bot responds to notify them.

---

## Setup Instructions

To use this bot, follow the instructions below.

### Prerequisites
1. Python installed (`>=3.8`).
2. The `pyTelegramBotAPI` library installed (`telebot`).

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Install dependencies:
   ```bash
   pip install pyTelegramBotAPI
   ```

3. Create and configure a bot through Telegram's [BotFather](https://t.me/botfather):
   - Get a bot token.
   - Replace the `<YOUR_TOKEN_HERE>` placeholder in the Python script with your bot token.

4. Run the bot:
   ```bash
   python Bot1.py
   ```

---

## Commands

Here are the commands supported by the Telegram bot:

| Command         | Description                                                   |
|------------------|---------------------------------------------------------------|
| `/start`        | Sends a welcome message to the user.                           |
| `/help`         | Lists all available commands.                                  |
| `/echo`         | Waits for a message and echoes the input back to the user.     |
| `/site` or `/website` | Sends a predefined link to users (example: YouTube).           |

The bot also detects and processes images, responding with inline buttons for interaction.

---

## Contributing

Contributions to improve this bot are always welcome.  
Feel free to fork this project, create a feature branch, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
