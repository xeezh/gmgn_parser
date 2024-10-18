import os
from art import text2art
import threading
from helius import Helius
from gmgn import GmGnApi
from time import sleep
import loguru
import config


def intro():
    print(text2art("Melancholy", "tarty1"))
    sleep(1.5)
    os.system("cls")

    print(text2art("Software", "tarty1"))
    sleep(1.5)
    os.system("cls")


def collect_user_data():
    contract = input('Input your token contract >> ')
    os.system('cls')
    profit = int(input('30d Profit ($) >> '))
    os.system('cls')
    pnl = int(input('30d PnL (%) >> ')) / 100
    os.system('cls')
    winrate = int(input('30d Win Rate (%) >> ')) / 100
    os.system('cls')
    avg_tradesize = int(input('AVG trade size ($) >> '))
    os.system('cls')
    return {
        'contract': contract,
        'profit': profit,
        'pnl': pnl,
        'winrate': winrate,
        'tradesize': avg_tradesize
    }


def main():
    data = collect_user_data()
    helius = Helius(
        api_key=config.helius_token
    )
    gmgn = GmGnApi()
    i = 0
    while True:
        i += 1
        holders = helius.get_holders(i, data['contract'])
        for holder in holders:
            holder_stats = gmgn.get_wallet_data(
                address=holder['owner']
            )
            if holder_stats['profit'] >= data['profit'] and \
                    holder_stats['pnl'] >= data['pnl'] and \
                    holder_stats['winrate'] >= data['winrate'] and \
                    holder_stats['tradesize'] >= data['tradesize']:
                with open('result/good.txt', 'a', encoding='utf-8') as f:
                    logger.success(holder['owner'])
                    f.write(holder['owner'] + '\n')
            else:
                logger.debug(holder['owner'])


if __name__ == '__main__':
    logger = loguru.logger
    intro()
    main()
