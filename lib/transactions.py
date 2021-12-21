from web3 import Web3
import config as config
import time
import lib.retrieveInfo as rinfo
import data.chainInfo as cinfo
import data.globalVar as glob

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))

# spend in WBNB
spend = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"


contract = web3.eth.contract(address=cinfo.PANCAKESWAP_ROUTER_CONTRACT_ADDRESS, abi=cinfo.PANCAKESWAP_ABI)
nonce = web3.eth.get_transaction_count(config.USER_PUBLIC_KEY)

balance = web3.eth.get_balance(config.USER_PUBLIC_KEY)
humanReadableBalance = web3.fromWei(balance, "ether")


# token address = token you are buying
def buyToken(tokenAddress, BNBAmount):

    try:

        # get conversion rate
        conversionRate = rinfo.getTokenPrice(config.TARGET_TOKEN, config.MORALIS_API_KEY, "bnb")

        # calculate how many of the target token should be recieved
        amountToRecieve = float(BNBAmount) / conversionRate

        # account for slippage
        amountToRecieve = int(amountToRecieve * (1 - (config.SLIPPAGE / 100))) * 10**18

        pancakeswap2_txn = contract.functions.swapExactETHForTokens(

            # calculate how many tokens should be recieved, then subtract slippage
            amountToRecieve, # amount to be received
            [spend, web3.toChecksumAddress(tokenAddress)],
            config.USER_PUBLIC_KEY,   # send FROM this address
            (int(time.time()) + 1000000)
            ).buildTransaction({
            'from': config.USER_PUBLIC_KEY,
            'value': web3.toWei(BNBAmount,'ether'), # This is the Token(BNB) amount you want to Swap from
            'gas': 6000000,
            'gasPrice': web3.toWei('10','gwei'),
            'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=config.USER_PRIVATE_KEY)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print("\nTransaction hash: " + web3.toHex(tx_token))

    except Exception as e:
        print(e)
        glob.token_purchased = False

    else:
        glob.token_purchased = True


def sellToken(tokenAddress, tokenAmount):
        
    try:
        # get conversion rate
        conversionRate = rinfo.getTokenPrice(config.TARGET_TOKEN, config.MORALIS_API_KEY, "bnb")

        # calculate how many of the target token should be recieved
        amountToRecieve = float(tokenAmount) * conversionRate

        # account for slippage
        amountToRecieve = int(amountToRecieve * (1 - (config.SLIPPAGE / 100)))



        sellContract = web3.eth.contract(address=config.TARGET_TOKEN, abi=cinfo.BSC_ABI_GENERIC)

        # transaction approval
        approve = sellContract.functions.approve(cinfo.PANCAKESWAP_ROUTER_CONTRACT_ADDRESS, tokenAmount).buildTransaction({
            'from': config.USER_PUBLIC_KEY,
            'gasPrice': web3.toWei('10','gwei'),
            'nonce': web3.eth.get_transaction_count(config.USER_PUBLIC_KEY),
        })

        signed_txn = web3.eth.account.sign_transaction(approve, private_key=config.USER_PRIVATE_KEY)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print("Approved: " + web3.toHex(tx_token))

        # wait for 10 seconds
        print(f"Swapping...")
        time.sleep(10)
        

        # actual transaction
        pancakeswap2_txn = contract.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(
            tokenAmount, amountToRecieve, 
            [web3.toChecksumAddress(tokenAddress), spend],
            config.USER_PUBLIC_KEY,
            (int(time.time()) + 1000000)

            ).buildTransaction({
            'from': config.USER_PUBLIC_KEY,
            'gas': 6000000,
            'gasPrice': web3.toWei('10','gwei'),
            'nonce': web3.eth.get_transaction_count(config.USER_PUBLIC_KEY),
        })

        signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=config.USER_PRIVATE_KEY)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print("\nTransaction hash: " + web3.toHex(tx_token))

    except Exception as e:
        print(e)
        glob.token_sold = False

    else:
        glob.token_sold = True