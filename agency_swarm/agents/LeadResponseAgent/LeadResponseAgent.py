"""Lead response agent template."""

from agency_swarm.agents import Agent


class LeadResponseAgent(Agent):
    """Drafts replies for inbound leads and updates the CRM."""

    def __init__(self):
        super().__init__(
            name="LeadResponseAgent",
            description="Creates replies for inbound leads and updates the CRM.",
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
