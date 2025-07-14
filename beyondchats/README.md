# Reddit User Persona Extractor

This project extracts a user persona from any public Reddit profile using only free tools (no API keys or paid services required).

## Features
- Scrapes public posts and comments from a Reddit user profile URL
- Builds a user persona based on their activity
- Cites posts/comments as evidence for each persona trait
- Outputs the persona to a text file

## Setup
1. Ensure you have Python 3.8 or higher installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script with a Reddit profile URL:
   ```bash
   python main.py https://www.reddit.com/user/koijed/
   ```
2. The output persona will be saved in the `output/` directory.

## Notes
- Only public Reddit data is used (no login or API keys required).
- The script is for educational and assignment purposes.

## Example
See `output/sample_persona_koijed.txt` for a sample output. 