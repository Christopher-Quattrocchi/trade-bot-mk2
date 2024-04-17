import requests
from web3 import Web3
from constants import STARGATE_CONTRACTS
from abi.stargate_composer import STARGATE_COMPOSER_ABI
from abi.stargate_router import STARGATE_ROUTER_ABI

def bridge_tokens(from_chain, to_chain, token, amount):
  try:
    # Init Web3 provider for source chain
    web3_from = Web3(Web3.HTTPProvider(f"https://{from_chain}.infura.io/v3/YOUR_INFURA_PROJECT_ID"))
    
    # Init Web3 provider for destination chain
    web3_to = Web3(Web3.HTTPProvider(f"https://{to_chain}.infura.io/v3/YOUR_INFURA_PROJECT_ID"))
    
    # Get Startgate contract addresses for the source and destination chains
    stargate_contracts_from = STARGATE_CONTRACTS[from_chain]
    stargate_contracts_to = STARGATE_CONTRACTS[to_chain]
    
    # Init StargateComposer contract instance for the source chain
    composer_from = web3_from.eth.contract(
      address=stargate_contracts_from["Composer"],
      abi=STARGATE_COMPOSER_ABI
    )
    
    # Initialize the StargateRouter contract instance for the destination chain
    router_to = web3_to.eth.contract(
      address=stargate_contracts_to["Router"],
      abi=STARGATE_ROUTER_ABI
    )
    
  except Exception as e:
    print(f"Error initialize contracts {e}")
    
    #Approve the StargateComposer contract to spend the tokens
    token_contract = web3_from.eth.contract(address=token["address"], abi=TOKEN_ABI)
    approve_tx = token_contract.functions.approve(
      stargate_contracts_from["Composer"],
      amount
    ).buildTransaction({
      "from": "YOUR_WALLET_ADDRESS",
      "gas": 100000,
      "gasPrice": web3_from.eth.gas_price,
      "nonce": web3_from.eth.getTransactionCount("YOUR_WALLET_ADDRESS")
    })
    
    # Sign and send the approve transaction
    signed_tx = web3_from.eth.account.signTransaction(approve_tx, private_key="YOUR_WALLET_PRIVATE_KEY")
    approve_tx_hash = web3_from.eth.sendRawTransaction(signed_tx.rawTransaction)
    approve_receipt = web3_from.eth.waitForTransactionReceipt(approve_tx_hash)
    
    # Get the source and destination pool IDs
    src_pool_id = stargate_contracts_from["PoolUSDC"]  # Assuming USDC as the source token
    dst_pool_id = stargate_contracts_to["PoolUSDC"]    # Assuming USDC as the destination token
    
    # Prepare payload for destination contract
    payload = web3_to.eth.contract(address="DESTINATION_CONTRACT_ADDRESS", abi=DESTINATION_CONTRACT_ABI)
    payload_data = payload.encodeABI(fn_name="sgReceive", args=[])
    
    # Call the swap() function on the StargateComposer contract
    swap_tx = composer_from.functions.swap(
        int(stargate_contracts_to["chainId"]),  # Destination chain ID
        src_pool_id,                            # Source pool ID
        dst_pool_id,                            # Destination pool ID
        "YOUR_WALLET_ADDRESS",                  # Refund address
        amount,                                 # Amount to swap
        0,                                      # Min amount to receive
        [0, 0, "0x"],                           # Stargate swap parameters
        "DESTINATION_CONTRACT_ADDRESS",         # Destination contract address
        payload_data                            # Payload data
    ).buildTransaction({
        "from": "YOUR_WALLET_ADDRESS",
        "value": web3_from.toWei(0.01, "ether"),  # Assuming 0.01 ETH as the bridge fee
        "gas": 500000,
        "gasPrice": web3_from.eth.gas_price,
        "nonce": web3_from.eth.getTransactionCount("YOUR_WALLET_ADDRESS")
    })
    
    # Sign and send the swap transaction
    signed_swap_tx = web3_from.eth.account.signTransaction(swap_tx, private_key="YOUR_WALLET_PRIVATE_KEY")
    swap_tx_hash = web3_from.eth.sendRawTransaction(signed_swap_tx.rawTransaction)
    swap_receipt = web3_from.eth.waitForTransactionReceipt(swap_tx_hash)
    
    print(f"Token bridging initiated. Transaction: {swap_receipt['transactionHash'].hex()}")
    
  except Exception as e:
    print(f"Error bridging tokens: {e}") 
    
