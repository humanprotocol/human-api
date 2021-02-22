import os

GAS_PAYER = os.getenv("GAS_PAYER")
GAS_PAYER_PRIV = os.getenv("GAS_PAYER_PRIV")
FACTORY_ADDRESS = os.getenv("FACTORY_ADDRESS")
REP_ORACLE_PUB_KEY = bytes(os.getenv("REP_ORACLE_PUB_KEY"), encoding="utf-8")