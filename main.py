import asyncio
import sys
from langchain_core.messages import HumanMessage
from graph.builder import debate_graph
from utils.io_handler import save_debate_to_markdown
from utils.logger import logger

async def main() -> None:
    logger.info("Initializing Multi-Agent Socratic Debate Ecosystem...")
    for handler in logger.handlers:
        handler.flush()

    print("\n" + "="*60)
    print("WELCOME TO THE MULTI-AGENT SOCRATIC DEBATE ECOSYSTEM")
    print("Submit an engineering code snippet or an academic draft to the panel.")
    print("Type 'exit' at any time to shut down the program.")
    print("="*60 + "\n")
    sys.stdout.flush()

    while True:
        try:
            user_input = input("Enter your technical or academic submission: \n>")

            if user_input.strip().lower() == "exit":
                logger.info("User requested system shutdown. Goodbye!")
                print("\nShutting down the ecosystem. Keep learning actively!")
                break

            if not user_input.strip():
                print("Input cannot be empty. Please try again.\n")
                continue

            print("\n" + "-"*50)
            print("The Supervisor is analyzing the context and assembling the panel...")
            print("-"*50 + "\n")

            initial_state = {
                "messages": [HumanMessage(content=user_input)]
            }

            final_state = await debate_graph.ainvoke(initial_state)

            report_path = save_debate_to_markdown(final_state)
            print(f"Detailed report successfully generated at:\n{report_path}\n")
            sys.stdout.flush()

        except Exception as e:
            logger.critical(f"A fatal unexpected error disrupted the interface loop: {str(e)}")
            for handler in logger.handlers:
                handler.flush()
            print(f"An unexpected system error occurred. Details saved to the technical log.\n")
            sys.stdout.flush()

if __name__ == "__main__":
    asyncio.run(main())