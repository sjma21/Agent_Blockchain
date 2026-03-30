from agent import parse_command
from blockchain import send_eth, get_balance, ACCOUNT
from web3 import Web3

def handle_action(data):
    if data["action"] == "send_eth":
        amount = float(data["amount"])
        address = data["address"]

        # safety
        if amount > 0.01:
            return " Amount too large"

        if not address.startswith("0x"):
            return " Invalid address"

        print(f"⚠️ You are about to send {amount} ETH to {address}")

        confirm = input("Type 'yes' to confirm:")

        if confirm.lower() != "yes":
            return "❌ Transaction cancelled"

        tx = send_eth(amount, address)
        return f" Transaction sent: {tx}"

    elif data["action"] == "get_balance":
        balance = get_balance(ACCOUNT.address)
        eth_balance = Web3.from_wei(balance, "ether")
        return f" Your balance is {eth_balance} ETH"

    return " Unknown action"

def run():
    while True:
        user_input = input("👉 Enter command: ")

        try:
            data = parse_command(user_input)
            print("🧠 Parsed:", data)

            result = handle_action(data)
            print(result)

        except Exception as e:
            print("❌ Error:", str(e))

if __name__ == "__main__":
    run()