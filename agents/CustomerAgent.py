from uagents import Agent, Context, Protocol
from uagents_core.contrib.protocols.chat import ChatMessage, chat_protocol_spec

class CustomerAgent(Agent):
    def __init__(self, seed: str):
        super().__init__(name="CustomerAgent", seed=seed)
        self.include(Protocol(spec=chat_protocol_spec, on_message=self.on_chat_message), publish_manifest=True)

    async def on_chat_message(self, ctx: Context, sender: str, msg: ChatMessage):
        # parse user text (source, destination, deadline)
        # send RouteRequest to RoutePlannerAgent
        # respond to user: “Okay, we’re planning your delivery…”
        pass

if __name__ == "__main__":
    import os
    seed = os.getenv("CUSTOMER_AGENT_SEED")
    agent = CustomerAgent(seed=seed)
    agent.run()
