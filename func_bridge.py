# Example of how to configure endpoints for Ethereum and Binance Smart Chain
layer_zero_endpoints = {
    'Ethereum': {
        'endpointId': 30101,
        'endpoint': '0x1a44076050125825900e736c501f859c50fe728c'
    },
    'BNB_Chain': {
        'endpointId': 30102,
        'endpoint': '0x1a44076050125825900e736c501f859c50fe728c'
    }
}

# Function to get the endpoint for a specific chain
def get_endpoint(chain_name):
    return layer_zero_endpoints.get(chain_name)