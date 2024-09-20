# Instagram Reel Views Counter Discord Bot

This project is a Discord bot that fetches the total number of views from an Instagram reel using Selenium driverless module.

## Features
- Scrapes Instagram to fetch the total number of views on a reel.
- Uses Selenium WebDriver to automate the login process and navigate Instagram.
- The bot is command-driven on Discord and responds to the `?views <Instagram Reel URL>` command with the view count.

## Prerequisites

1. **Python 3.8+** is required to run this project.
2. **Discord API Token** for creating and managing the bot.
3. **Instagram Credentials** (username and password) to log in and retrieve data.
4. **Google Chrome** must be installed for the Selenium driverless library.

### Libraries
The project uses the following key libraries:
- [discord.py](https://pypi.org/project/discord.py/): For interacting with Discord.
- [selenium-driverless](https://pypi.org/project/selenium-driverless/): For web scraping Instagram views.
- [python-dotenv](https://pypi.org/project/python-dotenv/): For securely storing and loading environment variables.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/killuazoldyckreal/Instagram-Counter.git
cd Instagram-Counter
```

### 2. Install dependencies
You can install the necessary Python libraries using the following command:
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory and add your Instagram credentials and Discord bot token:
```
USER=<your_instagram_username>
PASS=<your_instagram_password>
TOKEN=<your_discord_bot_token>
```

### 4. Run the Bot
To start the bot, run the following command:
```bash
python main.py
```

## Usage

1. Invite the bot to your Discord server.
2. In a text channel, type `?views <Instagram Reel URL>`.
3. The bot will respond with the total number of views for that reel.

Example:
```
?views https://www.instagram.com/woodsbetzz/reels/
```

## Known Issues

- The bot may encounter Instagram's rate-limiting restrictions, which can temporarily block requests.
- This bot uses basic Instagram scraping, which can break if Instagram changes its layout or structure.

## Contribution

Feel free to open issues or submit pull requests to improve the bot or fix bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
