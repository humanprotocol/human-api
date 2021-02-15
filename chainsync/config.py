import os
from dotenv import load_dotenv
load_dotenv()

ETH_SERVER = os.getenv('ETH_SERVER')
EXCHANGE_URI = os.getenv('EXCHANGE_URI')
HMTOKEN_ADDR = os.getenv('HMTOKEN_ADDR')
FACTORY_ADDR = os.getenv('FACTORY_ADDR')
GAS_PAYER = os.getenv('GAS_PAYER')
REQUESTER_PRIV = os.getenv('REQUESTER_PRIV')

CONTRACT_URLS = [
    'https://raw.githubusercontent.com/hCaptcha/hmt-escrow/master/contracts/Escrow.sol',
    'https://raw.githubusercontent.com/hCaptcha/hmt-escrow/master/contracts/EscrowFactory.sol',
    'https://raw.githubusercontent.com/hCaptcha/hmt-escrow/master/contracts/HMToken.sol',
    'https://raw.githubusercontent.com/hCaptcha/hmt-escrow/master/contracts/HMTokenInterface.sol',
    'https://raw.githubusercontent.com/hCaptcha/hmt-escrow/master/contracts/SafeMath.sol',
]
