from web3 import Web3
import json

# Load the Stargate Router contract ABI
with open("abi/stargate_router.json") as f:
    router_abi = json.load(f)

# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Load the Stargate Router contract ABI and address
router_address = "0x8731d54E9D02c286767d56ac03e8037C07e01e98" # Mainnet address

# Create a contract instance
router_contract = w3.eth.contract(address=router_address, abi=router_abi)

def stargate_swap(dst_chain_id, src_pool_id, dst_pool_id, amount_ld, wallet_address, private_key):
    # Define the swap parameters
    refund_address = wallet_address
    min_amount_ld = 0
    lz_tx_params = {"dstGasForCall": 0, "dstNativeAmount": 0, "dstNativeAddr": "0x0"}
    to_address = "DESTINATION_CONTRACT_ADDRESS"
    payload = b""

    # Call the swap function
    tx = router_contract.functions.swap(
        dst_chain_id,
        src_pool_id,
        dst_pool_id,
        refund_address,
        amount_ld,
        min_amount_ld,
        lz_tx_params,
        to_address,
        payload
    ).buildTransaction({
        'from': wallet_address,
        'value': w3.toWei(0.01, 'ether'),  # Gas fee for the cross-chain message
        'gas': 500000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'nonce': w3.eth.getTransactionCount(wallet_address)
    })

    # Sign and send the transaction
    signed_tx = w3.eth.account.signTransaction(tx, private_key=private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Transaction hash: {w3.toHex(tx_hash)}")

if __name__ == "__main__":
    dst_chain_id = 102  # BNB Chain ID
    src_pool_id = 1  # Assuming USDC as the source token
    dst_pool_id = 1  # Assuming USDC as the destination token
    amount_ld = w3.toWei(1, 'ether')  # Amount to swap in local decimals
    wallet_address = "YOUR_WALLET_ADDRESS"
    private_key = "YOUR_PRIVATE_KEY"

    stargate_swap(dst_chain_id, src_pool_id, dst_pool_id, amount_ld, wallet_address, private_key)