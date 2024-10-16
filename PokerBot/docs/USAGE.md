# Usage Guide

## Running the Bot
To start the bot, run:
```bash
python main.py
```

## Command-Line Options
You can specify options for the game type and buy-in amount:
```bash
python main.py --game_type TexasHoldem --buy_in 50.0
```

## Configuration
- **Platform Credentials**: Store credentials in `config/platform_credentials.json`.
- **Bot Settings**: Adjust bot behavior in `config/bot_settings.yaml`.
- **Payout Methods**: Define cashout methods in `config/payout_methods.json`.

## Monitoring
Use the `monitor_bot.sh` script to keep the bot running and automatically restart it if needed.
```
