from woke.testing import *
from pytypes.contracts.interfaces.IERC20 import IERC20


@default_chain.connect()
# or attach to already running anvil
# @default_chain("ws://localhost:8545")
def test_default():
    default_chain.set_default_accounts(default_chain.accounts[0])

    USDC = IERC20("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")
    print(f"USDC balance: {USDC.balanceOf(default_chain.accounts[0])}")
