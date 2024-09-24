import streamlit as st
import json
import random
from pathlib import Path

# Set page configuration
st.set_page_config(page_title="Emoji Display", page_icon="🎭", layout="wide")

# Load emoji data from points.json
@st.cache_data
def load_emoji_data():
    try:
        with open("points.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("Error: points.json file not found. Please make sure it's in the same directory as this script.")
        return []
    except json.JSONDecodeError:
        st.error("Error: Invalid JSON in points.json file.")
        return []

# Convert code point to emoji
def code_point_to_emoji(code_point):
    try:
        # Remove any 'U+' prefixes and split by spaces or hyphens
        parts = code_point.replace('U+', '').replace('-', ' ').split()
        # Convert each part to an integer and then to a character
        return ''.join(chr(int(part, 16)) for part in parts)
    except ValueError:
        st.warning(f"Invalid code point: {code_point}")
        return "�"

# Initialize session state
if 'displayed_emojis' not in st.session_state:
    st.session_state.displayed_emojis = []

# Main app
def main():
    st.title("🎭 Emoji Display")

    emoji_data = load_emoji_data()
    if not emoji_data:
        st.stop()

    # User input for number of emojis
    num_emojis = st.number_input("How many emojis would you like to display?", 
                                 min_value=1, max_value=10, value=5, step=1)

    # Button to generate emojis
    if st.button("Generate Emojis"):
        available_emojis = list(set(emoji_data) - set(st.session_state.displayed_emojis))
        
        if len(available_emojis) < num_emojis:
            st.warning("Not enough unique emojis available. Displaying all remaining unique emojis.")
            num_emojis = len(available_emojis)
        
        if available_emojis:
            selected_emojis = random.sample(available_emojis, num_emojis)
            st.session_state.displayed_emojis.extend(selected_emojis)

            # Display emojis
            emoji_display = "".join([code_point_to_emoji(cp) for cp in selected_emojis])
            st.markdown(f"<h1 style='font-size: 50px; text-align: center;'>{emoji_display}</h1>", unsafe_allow_html=True)
        else:
            st.info("All unique emojis have been displayed. Click 'Clear Emojis' to start over.")

    # Clear button
    if st.button("Clear Emojis"):
        st.session_state.displayed_emojis = []
        st.experimental_rerun()

    # Display current session info
    st.sidebar.title("Session Info")
    st.sidebar.write(f"Emojis displayed this session: {len(st.session_state.displayed_emojis)}")
    st.sidebar.write(f"Unique emojis remaining: {len(emoji_data) - len(st.session_state.displayed_emojis)}")

if __name__ == "__main__":
    main()