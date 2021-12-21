import json
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")
tradeInfo = config_object["TRADEINFO"]
walletInfo = config_object["WALLETINFO"]
apiInfo = config_object["APIINFO"]


# contract address of token to purchase
TARGET_TOKEN = tradeInfo["TARGET_TOKEN"] # hokk

# stop limit as a multiplier. Eg. set to 1.5 to sell token at 1.5x the value it was purchased
STOP_LIMIT = float(tradeInfo["STOP_LIMIT"])

# stop loss as a multiplier, Eg. set to 0.8 to sell token if 20% loss is reached
STOP_LOSS = float(tradeInfo["STOP_LOSS"])

# slippage as a percentage, Eg. set to 2 for 2% slippage, I reccommend leaving this at around 8 (sounds high),
# but it's to prevent failed transactions from costing you more gas
SLIPPAGE = float(tradeInfo["SLIPPAGE"])

# user public key
USER_PUBLIC_KEY = walletInfo["USER_PUBLIC_KEY"]

# user private key
USER_PRIVATE_KEY = walletInfo["USER_PRIVATE_KEY"]

# user bscscan api key
USER_API_KEY = apiInfo["BSC_API_KEY"]

# user moralis api key
MORALIS_API_KEY = apiInfo["MORALIS_API_KEY"]
