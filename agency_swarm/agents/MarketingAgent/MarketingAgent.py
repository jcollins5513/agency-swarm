"""Marketing campaign planning agent template."""

from agency_swarm.agents import Agent


class MarketingAgent(Agent):
    """Plans marketing campaigns and tracks metrics."""

    def __init__(self):
        super().__init__(
            name="MarketingAgent",
            description="Plans campaigns and monitors performance metrics.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        return message
