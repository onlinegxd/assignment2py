from MyWallet import exchangetogiven, MyCryptoWallet

wallet1 = MyCryptoWallet('bitcoin', 5)
wallet2 = MyCryptoWallet('cardano', 10)
print(wallet1.getcurrentprice())
print(exchangetogiven(wallet2, 'ethereum'))
