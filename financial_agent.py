from phi.agent import Agent
from phi.model.groq import Groq 
import phi.api
#from phi.tools.yfinance import YFinance
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import os
import dotenv

dotenv.load_dotenv()
import os
import openai



web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions="Always include the source of the information in the notes.",
    show_tool_calls=True,
    markdown=True
)


finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True),
    ],
    instructions=["Use tables to organize the information."],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions=["Always include sources","Use tables to organize the information."],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarize analyst reccomenation and latesr news for NVDA",stream=True)