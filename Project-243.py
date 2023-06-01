#import the Web3 module from Web3 library
from web3 import Web3

url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))

latest_block = web3.eth.get_block('latest')
print('Latest Block Of Ethereum BLockchain : ', latest_block)

block_transaction_count = web3.eth.get_block_transaction_count(13042315)
print('Number Of Transactions Happened In The Block : ', block_transaction_count)

transaction_fee = web3.eth.fee_history(4,'latest', None)
print('Transaction Fee History : ', transaction_fee)