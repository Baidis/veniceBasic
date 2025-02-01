import os
import json
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.memory import ChatMessageHistory


def load_agents():
    """Load agents from JSON file"""
    try:
        # Get the absolute path to the data directory
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Current directory of utils.py
        agents_file = os.path.join(base_dir, 'data', 'agents.json')
        
        with open(agents_file, 'r') as f:
            data = json.load(f)
            return data.get('agents', [])
    except FileNotFoundError:
        return []
    
def save_agents(agents):
    """Save agents to JSON file"""
    # Get the absolute path to the data directory
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Current directory of utils.py
    agents_file = os.path.join(base_dir, 'data', 'agents.json')
    
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(agents_file), exist_ok=True)
    
    with open(agents_file, 'w') as f:
        json.dump({"agents": agents}, f, indent=4)

def get_agent_response(agent, user_input):
    """
    Get a response from the agent using LangChain with persistent memory
    
    Args:
        agent (dict): The agent configuration
        user_input (str): The user's input message
        
    Returns:
        str: The agent's response
    """
    try:
        # Initialize the language model
        llm = ChatOpenAI(
            model_name=agent['model'],
            temperature=agent['temperature']
        )

        # Create a unique key for this agent's memory
        memory_key = f"memory_{agent['name']}"
        
        # Initialize or retrieve message history from session state
        if memory_key not in st.session_state:
            st.session_state[memory_key] = ChatMessageHistory()

        # Create a prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are {name}, acting as a {role}.\n\nYour goal: {goal}"),
            ("human", "{input}")
        ])

        # Create the chain using the new pattern
        chain = (
            {"name": RunnablePassthrough(), 
             "role": RunnablePassthrough(),
             "goal": RunnablePassthrough(),
             "input": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        # Get response
        response = chain.invoke({
            "name": agent['name'],
            "role": agent['role'],
            "goal": agent['goal'],
            "input": user_input
        })

        # Update message history
        st.session_state[memory_key].add_user_message(user_input)
        st.session_state[memory_key].add_ai_message(response)

        return response.strip()
    except Exception as e:
        return f"Error getting response: {str(e)}"