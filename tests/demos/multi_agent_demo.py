from agency_swarm.agency.agency import Agency
from agency_swarm.agents import (
    ContentCreator,
    LeadResponseAgent,
    MarketingAgent,
    SchedulerAgent,
    VoiceAgent,
)

content_creator = ContentCreator()
scheduler = SchedulerAgent()
voice = VoiceAgent()
lead_responder = LeadResponseAgent()
marketing = MarketingAgent()


agency = Agency(
    [
        marketing,
        [marketing, content_creator],
        [marketing, scheduler],
        [marketing, voice],
        [marketing, lead_responder],
    ]
)

if __name__ == "__main__":
    agency.run_demo()
