# Telegram Poll Bot

This bot allows you to automatically send polls to your Telegram channel or group on a schedule (weekly or as you configure).

## Getting Started
Create a bot using @BotFather on Telegram and get your BOT_TOKEN.
Add the bot to your channel or group and grant it permission to post messages.
Obtain your CHAT_ID: Use any get id bot in your channel (or group) to retrieve the ID (it starts with -100...).

## Local Deployment (Docker Compose)
Configure your environment variables.
Run a poll immediately: `docker-compose run --rm pollbot`

## GitHub Actions Setup
Create a workflow file.
Add your bot configuration as GitHub Secrets (BOT_TOKEN, CHAT_ID, POLL_QUESTION, POLL_OPTIONS, POLL_ANONYMOUS, POLL_MULTIPLE).
Define Variables for CRON_DAYS, CRON_HOUR, and CRON_MIN in Settings.
Customize the on.schedule.cron expression in your workflow to run at your preferred times.

Now GitHub Actions will automatically trigger (python send_poll.py) according to your schedule or on manual dispatch.
