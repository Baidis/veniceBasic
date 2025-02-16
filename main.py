import streamlit as st
import os
from dotenv import load_dotenv
import utils
import pages


def setup_environment():
    """
    Initialize environment variables and API configurations.
    
    Loads environment variables from .env file and sets up necessary API keys
    for various services including OpenAI and Supabase.
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Debug: Print environment variables to verify loading (disabled by default)
    DEBUG = False
    if DEBUG:
        print("Debug: Environment variables loaded")
        print(f"Debug: OPENAI_API_KEY length: {len(os.getenv('OPENAI_API_KEY', '')) if os.getenv('OPENAI_API_KEY') else 'Not set'}")
        print(f"Debug: OPENAI_API_BASE: {os.getenv('OPENAI_API_BASE', 'Not set')}")

def main():
    """
    Main application function.
    
    Handles the primary application flow including:
    - Setting up the environment
    - Initializing the session state
    - Loading agents
    - Managing navigation
    - Routing to appropriate pages
    """
    # Initialize environment
    setup_environment()
    
    # Set up main application title
    st.title("veniceBasic")

    # Load existing agents from storage
    agents = utils.load_agents()

    # Setup sidebar navigation
    page = st.sidebar.selectbox(
        "Select Page",
        ["Chat with Agents", "Create New Agent"],
        help="Choose which page to navigate to"
    )

    # Route to appropriate page function based on selection
    if page == "Chat with Agents":
        pages.chat_with_agents_page(agents)
    elif page == "Create New Agent":
        pages.create_agent_page(agents)

if __name__ == "__main__":
    main()
