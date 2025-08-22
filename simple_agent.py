# simple_agent.py
# UOMI Agent - Dani (Reward Agent)
# A simple reward agent with placeholder logic for UOMI integration

import time

class RewardAgent:
    def __init__(self, name, description, wallet, reward_token="UOMI"):
        self.name = name
        self.description = description
        self.wallet = wallet
        self.reward_token = reward_token
        self.running = False

    def on_start(self):
        print(f"🚀 Reward Agent {self.name} is starting...")
        print(f"📝 {self.description}")
        print(f"💳 Wallet: {self.wallet}")
        print(f"🎁 Ready to reward in {self.reward_token}")
        self.running = True

    def check_condition(self, event):
        """
        Placeholder for reward conditions.
        In real integration, this would check user stats or actions.
        """
        if event == "first_faucet_claim":
            return True, f"Rewarding user for their first faucet claim!"
        elif event == "daily_active":
            return True, f"Rewarding user for being active today!"
        return False, None

    def handle_event(self, event):
        """
        Handles events and decides whether to give a reward.
        """
        reward, message = self.check_condition(event)
        if reward:
            print(f"✅ Condition met: {message}")
            print(f"💸 Sending 10 {self.reward_token} from {self.wallet}")
        else:
            print(f"ℹ️ No reward for event: {event}")

    def run(self):
        """
        Simulates event loop.
        Replace with UOMI SDK or API in real deployment.
        """
        self.on_start()
        events = ["first_faucet_claim", "random_event", "daily_active"]

        for e in events:
            time.sleep(1)
            self.handle_event(e)


# --- Agent Setup ---
AGENT_NAME = "Dani"
AGENT_DESCRIPTION = "A Reward Agent that gives UOMI for specific milestones"
AGENT_WALLET = "0x5da08546bff22a41b596424d454eb4191add0035"

# --- Run the Agent ---
if __name__ == "__main__":
    agent = RewardAgent(AGENT_NAME, AGENT_DESCRIPTION, AGENT_WALLET)
    agent.run()
