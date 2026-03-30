# Agent Blockchain

An intelligent AI-powered CLI application that enables natural language control of Ethereum blockchain operations. Leveraging Claude AI, this project allows users to send ETH and check balances using conversational commands.

## Overview

Agent Blockchain bridges the gap between natural language and blockchain interactions. Instead of writing complex transaction code or understanding blockchain details, users can simply type natural commands like "Send 0.005 ETH to 0x742d35Cc6634C0532925a3b844Bc9e7595f9c5b0" and the AI agent parses and executes the command safely.

## Features

- **Natural Language Command Parsing**: Uses Claude AI to convert user commands into blockchain actions
- **Safe Transaction Handling**: Built-in safety checks for transaction amounts and address validation
- **User Confirmation**: Requires explicit "yes" confirmation before executing any transaction
- **Balance Checking**: Query your Ethereum account balance in human-readable format
- **Error Handling**: Robust error handling and validation throughout the application
- **Interactive CLI**: User-friendly command-line interface with status indicators and feedback

## Tech Stack

- **Python 3.x**: Core programming language
- **Claude AI (Anthropic)**: Natural language processing for command parsing
- **Web3.py**: Ethereum blockchain interaction library
- **python-dotenv**: Environment variable management
- **Ethereum Sepolia Testnet**: Target blockchain network (configurable)

## Installation

### Prerequisites

- Python 3.8 or higher
- Git
- Anthropic API key
- Ethereum Sepolia Testnet RPC endpoint URL
- A funded Ethereum private key (with test ETH)

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sjma21/Agent_Blockchain.git
   cd Agent_Blockchain
   ```

2. **Install Dependencies**
   ```bash
   pip install anthropic web3 python-dotenv
   ```

3. **Create Environment File**
   Create a `.env` file in the project root with the following variables:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   RPC_URL=https://sepolia.infura.io/v3/your_infura_project_id
   PRIVATE_KEY=your_ethereum_private_key_here
   ```

   **Important Security Note**:
   - Never commit `.env` to version control
   - Keep your private key secure and confidential
   - Use testnet accounts for development/testing

4. **Verify Installation**
   ```bash
   python main.py
   ```

## Usage

### Running the Application

```bash
python main.py
```

You'll see a prompt:
```
👉 Enter command:
```

### Example Commands

**Check Your Balance**
```
👉 Enter command: What's my current balance?
```

**Send ETH**
```
👉 Enter command: Send 0.005 ETH to 0x742d35Cc6634C0532925a3b844Bc9e7595f9c5b0
```

### Command Flow

1. User enters a natural language command
2. Claude AI parses the command into a JSON action
3. Application validates the action (amount limits, address format)
4. User is prompted to confirm the transaction
5. Transaction is executed on the blockchain
6. Result is displayed to the user

### Safety Features

- **Amount Limit**: Transactions are limited to 0.01 ETH maximum
- **Address Validation**: Addresses must start with "0x"
- **User Confirmation**: All transactions require explicit "yes" confirmation
- **Input Validation**: Strict validation of parsed commands

## Project Structure

```
Agent_Blockchain/
├── agent.py          # AI command parsing using Claude
├── blockchain.py     # Ethereum interaction functions
├── main.py          # CLI interface and transaction handling
└── README.md        # This file
```

### Module Descriptions

**agent.py**
- `parse_command(command)`: Converts natural language to structured JSON
- `clean_json(text)`: Extracts and cleans JSON from Claude's response
- Uses Claude Haiku model for fast, efficient parsing

**blockchain.py**
- `send_eth(amount, to_address)`: Signs and broadcasts an Ethereum transaction
- `get_balance(address)`: Retrieves the ETH balance of an address
- Handles transaction nonce management and signing

**main.py**
- `handle_action(data)`: Routes parsed actions to appropriate blockchain functions
- `run()`: Main REPL loop for user interaction
- Implements safety checks and confirmation prompts

## Configuration

### Environment Variables

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key for Claude access |
| `RPC_URL` | Ethereum RPC endpoint (Sepolia testnet recommended) |
| `PRIVATE_KEY` | Your Ethereum account private key (use testnet only) |

### Customization

- **Transaction Limit**: Edit the amount check in `main.py` line 11
- **Gas Price**: Modify the `gasPrice` in `blockchain.py` line 20
- **Chain ID**: Update `chainId` in `blockchain.py` line 21 for different networks
- **AI Model**: Change model in `agent.py` line 54

## Supported Actions

Currently supported blockchain operations:

1. **send_eth**: Send Ethereum to another address
   - Parameters: `amount` (float), `address` (hex string)

2. **get_balance**: Check account balance
   - Parameters: None (uses authenticated account)

## Error Handling

The application handles various error scenarios:
- Invalid JSON parsing from Claude
- Malformed blockchain addresses
- Transaction amount exceeding limits
- Network/RPC connection issues
- Insufficient gas or balance
- User cancellation of transactions

## Network Configuration

This project defaults to Ethereum Sepolia Testnet. To use:
- **Sepolia**: Recommended for testing (set RPC URL to Sepolia endpoint)
- **Mainnet**: Change `chainId` to 1 and update RPC URL (use caution with real funds)

## Security Considerations

⚠️ **Important**: This is a development/testing application.

- **Never use mainnet private keys** in this application
- **Never share your `.env` file** containing private keys
- **Always use testnet accounts** when experimenting
- **Keep API keys confidential** and rotate them regularly
- Consider implementing additional security measures for production use

## Limitations

- Maximum transaction amount capped at 0.01 ETH (configurable)
- Only supports ETH transfers (not ERC-20 tokens or complex contracts)
- Requires manual "yes" confirmation for all transactions
- Single account operation (doesn't support multiple accounts)
- Gas price is hardcoded (not dynamic)

## Future Enhancements

Potential features for future development:
- Support for multiple blockchain networks
- ERC-20 token transfers
- Transaction history logging
- Dynamic gas price estimation
- Multi-signature transaction support
- Transaction scheduling
- Batch operations
- Web UI interface

## Troubleshooting

**Issue**: "Invalid RPC URL"
- Verify your RPC_URL is correct and the service is accessible

**Issue**: "Insufficient funds"
- Ensure your account has enough test ETH on Sepolia
- Get free test ETH from Sepolia faucets

**Issue**: "No valid JSON found from Claude"
- Check your ANTHROPIC_API_KEY is valid
- Verify API key has appropriate permissions

**Issue**: "Transaction failed"
- Check account nonce consistency
- Verify gas price and limits are appropriate
- Ensure sufficient balance for gas fees

## Contributing

Contributions are welcome! Please feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is provided as-is for educational and development purposes.

## Resources

- [Anthropic Claude Documentation](https://docs.anthropic.com)
- [Web3.py Documentation](https://web3py.readthedocs.io)
- [Ethereum Sepolia Testnet](https://sepolia.dev/)
- [Ethereum JSON-RPC Specification](https://ethereum.org/en/developers/docs/apis/json-rpc/)

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Disclaimer**: This application is provided for educational purposes. Always use testnet accounts and never expose private keys. The developers are not responsible for lost funds or security breaches resulting from misuse.
