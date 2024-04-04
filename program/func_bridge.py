import requests

def bridge_tokens(from_chain, to_chain, token, amount):
  try:
    # Set up the multichain api endpoint and parameters
    endpoint = "https://api.multichain.org/v1/anyswap/bridge"
    headers = {
      "Content-Type": "application/json"
    }
    data = {
      "fromChainId": from_chain,
      "toChainId": to_chain,
      "tokenAddress": token["address"],
      "amount": amount,
      "receiverAddress": "YOUR_RECEIVER_ADDRESS" # REPLACE WITH MY OWN
    }
    
    #Make API request to init the token bridging
    response = requests.post(endpoint, headers=headers, json=data)
    
    # Check response status
    if response.status_code == 200:
      result = response.json()
      print(f"Token bridging initiated. Transaction: {result['transactionHash']}")
    else:
      print(f"Error bridging tokens: {response.text}")
    
  except Exception as e:
    print(f"Error bridging tokens: {e}")