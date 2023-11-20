# Unite180 Service

## Overview

The Unite180 Service is a Python-based application that interfaces with Telegram to send messages for various purposes, such as birthday notifications and general messages to designated chat groups.

## Table of Contents

- [Features](#features)
- [File Structure](#file-structure)
- [Telegram Bot Integration](#telegram-bot-integration)
- [Getting Chat ID](#getting-chat-id)
- [Setup and Configuration](#setup-and-configuration)
  - [Running Locally](#running-locally)
  - [Building Docker Image](#building-docker-image)

## Features

- Sends birthday notifications to specified Telegram chat groups.
- Customizable message sending for different events or notifications.
- Integration with Telegram Bot API.

## File Structure

The application's file structure is organized as follows:

- `unite180_service.py`: Main application file containing the service logic and scheduling of messages.
- `telegram_bot.py`: Module handling Telegram Bot integration and message sending functionality.
- `config.ini`: Configuration file for storing tokens and chat IDs for the Telegram Bot.

## Telegram Bot Integration

The application utilizes the Python `python-telegram-bot` library to integrate with the Telegram Bot API. The `telegram_bot.py` module handles the interaction with the Telegram API and message sending to specified chat groups.

## Getting Chat ID

To obtain the chat ID for a specific chat group:

1. Start a chat with your Telegram Bot.
2. Navigate to the following URL in your web browser:

    ```
    https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
    ```

    Replace `<YOUR_BOT_TOKEN>` with your actual Telegram Bot token.

3. Look for the chat object in the JSON response. The `id` field within the `chat` object corresponds to the chat ID of that specific chat group.

## Setup and Configuration

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Morne-Coetzee/Unite180Scheduler
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Update Configuration:**
    - Obtain a Telegram Bot token by creating a new bot via [BotFather](https://t.me/BotFather) on Telegram.
    - Update the `config.ini` file:
        ```ini
        [Bot]
        token=<YOUR_BOT_TOKEN>

        [ChatIds]
        GroupChat=<YOUR_GROUP_CHAT_ID>
        ```
        Replace `<YOUR_BOT_TOKEN>` with the obtained Telegram Bot token and `<YOUR_GROUP_CHAT_ID>` with the chat ID of the desired chat group.

4. **Run the Application Locally:**
    ```bash
    python unite180_service.py
    ```

### Building Docker Image

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Morne-Coetzee/Unite180Scheduler
    ```

2. **Build Docker Image:**
    ```bash
    docker build -t unite180_service .
    ```

3. **Run Docker Container:**
    ```bash
    docker run -p 8080:8080 unite180_service
    ```
