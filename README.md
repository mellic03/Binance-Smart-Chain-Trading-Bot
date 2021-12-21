# Binance-Smart-Chain-Trading-Bot

This is a python bot which uses web3 to interact with the Binance Smart Chain.



## Install dependencies (Windows)

Run install_dependencies.bat for easy installation of dependencies. Alternatively, you could download/install all dependencies yourself.



## Install dependencies (Linux)
Assuming python and pip are already installed, use [pip](https://pip.pypa.io/en/stable/) to install dependencies/requirements.txt.

```bash
pip install -r dependencies/requirements.txt
```

## Configuration (Universal)
1. Create an account and generate API keys for both [bscscan](https://bscscan.com/) and [Moralis](https://moralis.io/).
2. Open config.py and enter the token you wish to trade as well as your wallet public/private keys, stop loss/limit and API keys.
3. Run main.py.

## Usage

```basg
auto
# Asks for a BNB amount of the specified token to purchase, the program then monitors the tokens change in price and sells at your stop loss/limit.

stop
# Only usable in auto mode, stops auto mode and kills the program, useful if the user wants to sell the token before the stop loss/limit is reached.

buy
# Asks for a BNB amount of the specified token to purchase.

sell
# Sells all of the specified token for BNB.

balance
# returns the user's wallet balance in BNB.

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
