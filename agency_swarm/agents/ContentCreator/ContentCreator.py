"""Content Creator agent template."""

from agency_swarm.agents import Agent


class ContentCreator(Agent):
    """Generates marketing copy and other written materials."""

    def __init__(self):
        super().__init__(
            name="ContentCreator",
            description="Generates copy for blogs and social media.",
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
