[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://app-emoji-kitchen-0eyi2v5fax9e.streamlit.app/)

# Streamlit Emoji randomizer


# Emoji Display Streamlit App

This Streamlit application allows users to randomly display emojis from a predefined set. Users can specify how many emojis they want to see (up to 10), and the app ensures that no emoji is repeated within a session.

## Features

- Randomly display emojis from a JSON file
- User can specify the number of emojis to display (1-10)
- No duplicate emojis within a session
- Clear button to reset the display
- Sidebar showing session information

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.7 or later
- You have installed Streamlit. If not, you can install it using pip:
  ```
  pip install streamlit
  ```

## Installation

1. Clone this repository or download the `emoji_display_app.py` file.
2. Ensure you have a `points.json` file in the same directory as the script. This file should contain a JSON array of emoji code points.

Example `points.json` content:
```json
["1f600", "1f601", "1f602", "1f603", "1f604", "1f605"]
```

## Usage

To run the Emoji Display app:

1. Open a terminal or command prompt
2. Navigate to the directory containing `emoji_display_app.py`
3. Run the following command:
   ```
   streamlit run streamlit_app.py
   ```
4. The app will open in your default web browser

## How to Use the App

1. Enter the number of emojis you want to display (1-10) in the input field
2. Click the "Generate Emojis" button to display random emojis
3. Use the "Clear Emojis" button to reset the display and start over
4. Check the sidebar for information about your current session

## Troubleshooting

If you encounter any issues:

- Ensure your `points.json` file is properly formatted and contains valid emoji code points
- Check that you have the latest version of Streamlit installed
- If you see warnings about invalid code points, double-check the format in your JSON file

## Contributing

Contributions to improve the Emoji Display app are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).