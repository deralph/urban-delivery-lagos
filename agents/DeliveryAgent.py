from uagents import Agent, Context
from models import RoutePlan, StatusUpdate

class DeliveryAgent(Agent):
    def __init__(self, seed: str):
        super().__init__(name="DeliveryAgent", seed=seed)
        # maybe set state

    async def on_receive_plan(self, ctx: Context, sender: str, msg: RoutePlan):
        # simulate the journey:
        # if msg.mode == "motor-bike": simulate narrow street path
        # else if mode == "van": simulate van path
        # send StatusUpdate messages every N seconds to CustomerAgent
        pass

if __name__ == "__main__":
    import os
    seed = os.getenv("DELIVERY_AGENT_SEED")
    agent = DeliveryAgent(seed=seed)
    agent.run()
    