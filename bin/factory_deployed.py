import os
from hmt_escrow.eth_bridge import deploy_factory

GAS_PAYER = os.getenv("GAS_PAYER")
GAS_PAYER_PRIV = os.getenv("GAS_PAYER_PRIV")

print(deploy_factory(gas_payer=GAS_PAYER, gas_payer_priv=GAS_PAYER_PRIV))