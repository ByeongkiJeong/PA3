import os
import asyncio

from dotenv import load_dotenv

from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

import inspect
import wrapped_builtins
from wrapped_builtins import *

def get_wrapped_function_names(module):
    """
    모듈에서 데코레이터가 붙어있는 함수들의 이름만 반환합니다.
    """
    decorated_functions = []
    
    # 모듈의 모든 속성 가져오기
    for name in dir(module):
        # '_'로 시작하는 속성들은 무시 (private 속성들)
        if name.startswith('_'):
            continue
            
        # 속성 값 가져오기
        obj = getattr(module, name)
        
        # 함수이고 __wrapped__ 속성이 있으면 (데코레이터가 붙은 함수)
        if inspect.isfunction(obj) and hasattr(obj, '__wrapped__'):
            decorated_functions.append(name)
    
    return decorated_functions


load_dotenv()

agent = ChatAgent(
    chat_client=OpenAIChatClient(
        model_id=os.environ['OPENAI_MODEL_NAME'],
        api_key=os.environ['OPENAI_API_KEY'],
        base_url=os.environ['OPENAI_ENDPOINT']
    ),
    instructions=("You are a python interpreter itself,"
                  "you can only use given built-in functions to answer user questions."
                  "Return only the printed output of the code execution."
                  "Even if the code has errors, return only the printed output."),
    tools=get_wrapped_function_names(wrapped_builtins), 
)

async def run(query: str) -> str:
    return await agent.run(query)

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Run the ChatAgent with a query.")
    # Support both an optional --query/-q flag and an optional positional query for backward compatibility.
    parser.add_argument('-q', '--query', dest='opt_query', help='Query string to execute (preferred).')
    parser.add_argument('pos_query', nargs='?', help='Positional query string (used if --query not provided).')
    args = parser.parse_args()

    # Determine query: from CLI arg, or interactive prompt
    # Precedence: --query/-q (opt_query) > positional (pos_query) > piped stdin > interactive prompt
    if args.opt_query:
        query = args.opt_query
    elif args.pos_query:
        query = args.pos_query
    else:
        try:
            # If input is piped, read from stdin first
            if not sys.stdin.isatty():
                piped = sys.stdin.read().strip()
                if piped:
                    query = piped
                else:
                    query = input("Query: ")
            else:
                query = input("Query: ")
        except (EOFError, KeyboardInterrupt):
            print("No query provided. Exiting.")
            sys.exit(0)

    response = asyncio.run(run(query))
    print("Response:", response)