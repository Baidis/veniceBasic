
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
    
    Returns:
        tuple: Contains initialized configuration values (supabase_url)
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Initialize API configurations
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

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