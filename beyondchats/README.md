# Reddit User Persona Extractor

A Python tool to analyze any public Reddit user's activity and generate a concise, evidence-based user persona. This project is designed for anyone interested in social media analysis, digital anthropology, or simply exploring Reddit user behavior.

## Features
- Scrapes public posts and comments from a given Reddit profile URL (no login or API keys required)
- Analyzes content to infer interests, activity level, and writing style
- Cites specific posts or comments as evidence for each persona trait
- Outputs a clear, readable persona profile in a text file

## Installation
1. Make sure you have Python 3.8 or higher installed.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script from your terminal, providing a Reddit profile URL:
   ```bash
   python main.py https://www.reddit.com/user/example_username/
   ```
2. The generated persona profile will be saved in the `output/` directory as a `.txt` file named after the Reddit user.

## Example Output
The output file will include:
- A summary of the user's top interests, activity level, and writing style
- A "Citations" section linking each trait to the relevant post or comment

## Notes
- This tool only uses publicly available Reddit data.
- No authentication or paid services are required.
- For best results, use with active Reddit users who have public posts and comments.

## Contributing
Contributions, suggestions, and feedback are welcome! Feel free to open an issue or submit a pull request.

## License
This project is open source and available under the MIT License.

## Contact
Created by Ankit (GitHub: [ankitgpt18](https://github.com/ankitgpt18)). 