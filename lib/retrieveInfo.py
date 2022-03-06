import requests
import data.chainInfo as cinfo


def getTokenPrice(target, moralisApiKey, PAIR):

    headers = {
        "accept": "application/json",
        "X-API-Key": moralisApiKey,
    }

    params = (
        ("chain", "bsc"),
        ("exchange", cinfo.PANCAKESWAP_FACTORY_V2_ADDRESS),
    )

    response = requests.get("https://deep-index.moralis.io/api/v2/erc20/" + target + "/price", headers=headers, params=params).json()

    if (PAIR == "bnb"):
        return(float(response["nativePrice"]["value"]) * 10**-(float(response["nativePrice"]["decimals"])))
    elif (PAIR == "usd"):
     return(float(response["usdPrice"]))


# retrieves the account balance of a specified token
def getAccountBalanceInToken(target, publicKey, bscApiKey):
    TOKEN_BALANCE = requests.get("https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=" + target + "&address=" + publicKey + "&tag=latest&apikey=" + bscApiKey).json()
    return(int(TOKEN_BALANCE["result"]))

# retrieves the account balance in BNB
def getAccountBalanceInBNB(publicKey, bscApiKey):
    TOKEN_BALANCE = requests.get("https://api.bscscan.com/api?module=account&action=balance&address=" + publicKey + "&tag=latest&apikey=" + bscApiKey).json()
    return(int(TOKEN_BALANCE["result"]))
