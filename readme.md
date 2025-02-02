# Venice API Integration

## Overview
This project integrates with the Venice API, allowing users to interact with AI agents through a web interface built with Streamlit. Users can chat with existing agents or create new ones, customizing their roles and goals.

## Features
- **Chat with Agents**: Engage in conversations with pre-defined AI agents.
- **Create New Agent**: Define new agents with specific roles, goals, and parameters.
- **Environment Configuration**: Load API keys and configurations from a `.env` file.

## Requirements
To run this project, you need to have Python 3.12 or higher installed. The required packages are listed in `requirements.txt`.

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Environment Variables
Create a `.env` file in the root directory of the project with the following content:

```
# Venice API Configuration 
OPENAI_API_KEY=your_venice_ai_api_key_here
OPENAI_API_BASE=https://api.venice.ai/api/v1
```

or copy .envExample to .env and just add your API key.

Replace `your_venice_ai_api_key_here` with your actual Venice.ai API key.

## Running the Application
To start the application, run the following command:

```bash
streamlit run main.py
```


## Directory Structure
```
.
├── .gitignore
├── .envExample
├── requirements.txt
├── readme.md
├── main.py
├── pages.py
├── utils.py
└── config.py
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
