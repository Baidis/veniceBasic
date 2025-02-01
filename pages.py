import streamlit as st
import utils
import config

def chat_with_agents_page(agents):
    """Function for the chat interface page"""
    st.header("Chat with Agents")
    agent_names = [agent['name'] for agent in agents]
    selected_agent = st.selectbox("Select an Agent", agent_names)

    if selected_agent:
        agent = next((a for a in agents if a['name'] == selected_agent), None)
        if agent:
            st.write(f"Chatting with {agent['name']} (Role: {agent['role']})")
            
            response_mode = st.radio("Response Mode", ("Simulated", "Actual"))

            if 'chat_history' not in st.session_state:
                st.session_state.chat_history = []

            # Display chat history
            for user_msg, agent_msg in st.session_state.chat_history:
                st.write(f"You: {user_msg}")
                st.write(f"{agent['name']}: {agent_msg}")

            # User input
            user_input = st.text_input("You: ")
            if st.button("Send"):
                if user_input:
                    st.session_state.chat_history.append((user_input, ""))

                    # Simulate or get actual response
                    if response_mode == "Simulated":
                        agent_response = f"[Simulated response to '{user_input}']"
                    else:
                        agent_response = utils.get_agent_response(agent, user_input)

                    st.session_state.chat_history[-1] = (user_input, agent_response)
                    st.rerun()

def create_agent_page(agents):
    """Function for the agent creation page"""
    st.header("Create New Agent")
    agent_name = st.text_input("Agent Name")
    agent_role = st.text_input("Agent Role")
    agent_goal = st.text_area("Agent Goal")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)

    if st.button("Create Agent"):
        if agent_name and agent_role and agent_goal:
            new_agent = {
                "name": agent_name,
                "role": agent_role,
                "goal": agent_goal,
                "temperature": temperature,
                "model": config.DEFAULT_MODEL  # Default model
            }
            agents.append(new_agent)
            utils.save_agents(agents)
            st.success(f"Agent '{agent_name}' created successfully!")
        else:
            st.error("Please fill in all fields.")