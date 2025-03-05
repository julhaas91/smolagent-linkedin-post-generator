from agents import create_agent

def main():
    agent = create_agent(model_id="openai/gpt-4o-mini")
    agent.run("""
            Can you find out the most relevant AI news today and give me a LinkedIn post about it? 
            Use your team members. Call them by their names and specify a task: 'name' with arguments {'task': your task}. 
            """)


if __name__ == "__main__":
    main()
