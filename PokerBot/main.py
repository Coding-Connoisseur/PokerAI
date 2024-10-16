
import argparse
from core.bot_controller import BotController

def main():
    parser = argparse.ArgumentParser(description='Start the PokerBot')
    parser.add_argument('--game_type', type=str, default='TexasHoldem', help='Type of poker game')
    parser.add_argument('--buy_in', type=float, default=50.0, help='Buy-in amount for the game')
    args = parser.parse_args()

    bot_controller = BotController()
    bot_controller.run_bot(game_type=args.game_type, buy_in=args.buy_in)

if __name__ == '__main__':
    main()
