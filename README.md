# Blockchain Voting System 🗳️

A decentralized voting system built on Ethereum's Sepolia testnet. This project allows users to vote for their preferred candidate using smart contracts, ensuring transparency and security in the voting process.

## Features
- **Decentralized Voting**: Votes are recorded on the Ethereum blockchain.
- **Transparency**: All votes are publicly verifiable.
- **Security**: Smart contracts ensure that each address can vote only once.
- **User-Friendly Interface**: Built with Streamlit for an intuitive user experience.

## Technologies Used
- **Ethereum**: For blockchain and smart contracts.
- **Web3.py**: To interact with the Ethereum blockchain.
- **Streamlit**: For the web interface.
- **Alchemy**: As the Ethereum node provider.

## Prerequisites
- Python 3.8 or higher
- Streamlit (`pip install streamlit`)
- Web3.py (`pip install web3`)
- An Ethereum wallet (e.g., MetaMask) with Sepolia testnet ETH.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blockchain-voting-system.git


Navigate to the project directory:

bash
cd blockchain-voting-system
Install the required dependencies:

bash
pip install -r requirements.txt
Run the Streamlit app:

bash
streamlit run app.py
How to Use
Connect Your Wallet:

Enter your Ethereum wallet address (Sepolia testnet) in the app.

Choose a Candidate:

Select your preferred candidate from the dropdown menu.

Submit Your Vote:

Click the "Vote Now" button to submit your vote.

View Results:

Check the voting results displayed in the app.

Smart Contract Details
Contract Address: 0xYourContractAddress (Replace with your deployed contract address)

ABI: Included in the contract_abi.json file.

Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.
