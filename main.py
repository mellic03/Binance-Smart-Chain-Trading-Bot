from logging import exception
import threading

import config as config
import lib.transactions as tran
import lib.retrieveInfo as rinfo
import data.globalVar as glob


def main():

    print("Please select mode (buy/sell/auto/balance): ")
    mode = input()


    if (mode == "auto"):
        auto_thread = threading.Thread(name = "auto mode", target = autoMode, daemon = True)
        auto_thread.start()
        while True:
            if input().lower() == "stop":
                print("stopping")
                exit()


    elif (mode == "buy"):
        buyMode()


    elif (mode == "sell"):
        sellMode()


    elif (mode == "balance"):
        balanceMode()


    else:
        print("brrr")


def autoMode():

    # user inputs amount of token to buy in BNB
    purchaseAmount = input("Amount to purchase (BNB): ")


    while (glob.token_purchased == False):

        # retrieve token price
        glob.token_price_initial = rinfo.getTokenPrice(config.TARGET_TOKEN, config.MORALIS_API_KEY, "bnb")

        # purchase token
        tran.buyToken(config.TARGET_TOKEN, purchaseAmount)


    # monitor price and sell at 2x
    while (glob.token_purchased == True and glob.token_sold == False):

        # retrieve token price and compare to token price at purchase
        glob.token_price_now = rinfo.getTokenPrice(config.TARGET_TOKEN, config.MORALIS_API_KEY, "bnb")

        # display return as a percentage
        print("\nCurrent return: " + str(((glob.token_price_now - glob.token_price_initial) * glob.token_price_now / glob.token_price_initial) * 100) + "%")

        # if the gain (as a multiplier) is greater than the config stop limit, sell the tokens
        if (glob.token_price_now >= (config.STOP_LIMIT * glob.token_price_initial) or glob.token_price_now <= (config.STOP_LOSS * glob.token_price_initial)):
            
            # get the account balance of the current token
            TOKEN_BALANCE = rinfo.getAccountBalanceInToken(config.TARGET_TOKEN, config.USER_PUBLIC_KEY, config.USER_API_KEY)

            # sell that amount
            try:
                tran.sellToken(config.TARGET_TOKEN, TOKEN_BALANCE)
            except Exception as e:
                print(e)


def buyMode():
    # user inputs amount of token to buy in BNB
    purchaseAmount = input("Amount to purchase (BNB): ")
    # purchase token
    tran.buyToken(config.TARGET_TOKEN, purchaseAmount)
    main()

def sellMode():
    # get the account balance of the current token
    TOKEN_BALANCE = rinfo.getAccountBalanceInToken(config.TARGET_TOKEN, config.USER_PUBLIC_KEY, config.USER_API_KEY)
    # sell that amount
    tran.sellToken(config.TARGET_TOKEN, TOKEN_BALANCE)
    main()

def balanceMode():
    # get the account balance of the current token
    print("Retrieving account balance ")
    TOKEN_BALANCE = rinfo.getAccountBalanceInBNB(config.USER_PUBLIC_KEY, config.USER_API_KEY)
    print(str(TOKEN_BALANCE * (10**-18)) + " BNB\n")
    main()

main()
