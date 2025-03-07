import streamlit as st
from web3 import Web3
import json

# Alchemy RPC URL
ALCHEMY_RPC_URL = "https://eth-sepolia.g.alchemy.com/v2/rsNBFgv_CpQwomiKKnFGwqqgj-vf3g6F"

# Connect to Ethereum via Alchemy
w3 = Web3(Web3.HTTPProvider(ALCHEMY_RPC_URL))

# Check if connected
if w3.is_connected():
    st.success("✅ Connected to Ethereum Sepolia Testnet via Alchemy!")
    st.write(f"Latest Block: {w3.eth.block_number}")
else:
    st.error("❌ Connection failed. Check your API key and RPC URL.")
    st.stop()

# Smart contract details
contract_address = "0x3215520baeeAf4fEC69b419fAf308551567EF08D"  # Replace with your contract address
contract_abi = json.loads('''
[
    {
        "inputs": [
            {
                "internalType": "string[]",
                "name": "candidateNames",
                "type": "string[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "candidateIndex",
                "type": "uint256"
            }
        ],
        "name": "vote",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "candidates",
        "outputs": [
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "voteCount",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getResults",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "string",
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "internalType": "uint256",
                        "name": "voteCount",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct Voting.Candidate[]",
                "name": "",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "voters",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
''')

# Load contract
try:
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    st.write("✅ Smart Contract Loaded!")
except Exception as e:
    st.error(f"❌ Failed to load contract: {e}")
    st.stop()

# Streamlit UI
st.title("🗳️ Blockchain Voting System")

# Candidate selection
candidates = ["Alice", "Bob", "Charlie"]
vote = st.selectbox("Choose a candidate:", candidates)

# User wallet address input
wallet_address = st.text_input("Enter your Ethereum Wallet Address (Sepolia)")

# Submit Vote
if st.button("Vote Now"):
    if w3.is_address(wallet_address):
        try:
            # Get the index of the selected candidate
            candidate_index = candidates.index(vote)
            # Send the transaction
            tx_hash = contract.functions.vote(candidate_index).transact({'from': wallet_address})
            st.success(f"✅ Vote submitted! Transaction Hash: {tx_hash.hex()}")
        except Exception as e:
            st.error(f"❌ Failed to submit vote: {e}")
    else:
        st.error("❌ Invalid Ethereum address.")

# Display results (Dummy data for now)
st.subheader("📊 Voting Results")
st.write("Alice: 10 votes")
st.write("Bob: 7 votes")
st.write("Charlie: 5 votes")