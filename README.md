# Crypto wallet exchanger calculator using coinmarketcap.com API

### Installation
PyPI
```bash
pip install requests
```
Download the MyWallet package and add it to your project
```bash
/ProjectDirectory/MyWallet
```

Imports
```bash
from MyWallet import exchangetogiven, MyCryptoWallet
```

### Usage

```python
objectName = MyCryptoWallet('name of the cryptocurrency', *amount of the coins*)

wallet1.getcurrentprice() returns current price of given cryptocurrency multiplied by amount
exchangetogiven(yourWalletObject, 'name of the cryptocurrency') returns exchanged your cryptocurrency in given
```

### Examples
```python
wallet1 = MyCryptoWallet('bitcoin', 5)
print(wallet1.getcurrentprice())
print(exchangetogiven(wallet1, 'ethereum'))
>>>
275642.83864838997
78.51909245817964
```
