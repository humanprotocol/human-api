import os

GAS_PAYER = os.getenv("GAS_PAYER")
GAS_PAYER_PRIV = os.getenv("GAS_PAYER_PRIV")
FACTORY_ADDRESS = os.getenv("FACTORY_ADDRESS")
REP_ORACLE_PUB_KEY = bytes(os.getenv("REP_ORACLE_PUB_KEY"), encoding="utf-8")
RESULTS_PATH = os.getenv("RESULTS_PATH", "/work/human_api/test/dumps/test_results_file")
PAYOUTS_PATH = os.getenv("PAYOUTS_PATH", "/work/human_api/test/dumps/test_payouts_file")