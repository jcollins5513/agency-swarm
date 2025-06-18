"""Scheduler agent template."""

from agency_swarm.agents import Agent


class SchedulerAgent(Agent):
    """Manages calendar events and tasks."""

    def __init__(self):
        super().__init__(
            name="SchedulerAgent",
            description="Handles calendar events and task scheduling.",
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
