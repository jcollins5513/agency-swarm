"""Voice agent template."""

from agency_swarm.agents import Agent


class VoiceAgent(Agent):
    """Handles text-to-speech and speech-to-text conversion."""

    def __init__(self):
        super().__init__(
            name="VoiceAgent",
            description="Converts text to speech and back.",
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
