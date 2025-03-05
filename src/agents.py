from smolagents import CodeAgent

from models import get_model
from tools import fetch_ai_news_rss
from prompts import WEB_AGENT_TASK, LINKEDIN_WRITER_AGENT_TASK


def create_agent(model_id="openai/gpt-4o-mini"):
    """
    Returns the manager agent.
    """
    ai_news_summarizer_agent = CodeAgent(
        tools=[fetch_ai_news_rss], 
        model=get_model(model=model_id),
        max_steps=10,
        verbosity_level=0,
        name="ai_news_summarizer_agent",
        description="""
        A team member that will search for today's most relevant artificial intelligence (AI) news. 
        The team member will provide you with the most relevant AI news headline and a detailed summary.
        """,
        provide_run_summary=False
    )
    ai_news_summarizer_agent.prompt_templates["managed_agent"]["task"] += WEB_AGENT_TASK

    linkedin_writer_agent = CodeAgent(
        tools=[], 
        model=get_model(model=model_id),
        max_steps=10,
        verbosity_level=0,
        name="linkedin_writer_agent",
        description="""
        A team member that will generate a LinkedIn post based on the information that you provide him with.
        Please provide the team member with a dictionary with: 
            {
                "headline": your_headline,
                "summary": your_summary
            }
        """,
        provide_run_summary=False
    )
    linkedin_writer_agent.prompt_templates["managed_agent"]["task"] += LINKEDIN_WRITER_AGENT_TASK

    manager_agent = CodeAgent(
        model=get_model(model=model_id),
        tools=[],
        max_steps=10,
        verbosity_level=4,
        # planning_interval=4,
        managed_agents=[ai_news_summarizer_agent, linkedin_writer_agent],
    )

    return manager_agent
