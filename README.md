# BreachCheck - Sagittarius

## Introduction

We strongly advise users to only utilize BreachCheck for their own emails and passwords. Do not misuse this tool or exploit it for malicious purposes. Respect the privacy and security of others by refraining from attempting to check passwords that do not belong to you.

Our aim is to promote responsible and ethical use of BreachCheck to empower individuals in securing their online presence. By adhering to these principles, we can collectively contribute to a safer digital environment for everyone.

You can experience the application [https://breachcheck-sagittarius.streamlit.app/](https://breachcheck-sagittarius.streamlit.app/) which is hosted on Streamlit Sharing Cloud.

## Usage

### Prerequisites

Ensure you have Python 3.6 or later installed on your system.

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/VKrishna04/BreachCheck.git
    cd BreachCheck
    ```

2. **Create a virtual environment (not required):**
    On Linux
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

    On Windows
    ```ps1
    python -m venv venv
    source venv\Scripts\activate
    ```

    On MacOS
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

This will provide clear instructions for setting up and activating a virtual environment on both Windows and macOS.

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

This is for installing the necessary packages to run the Streamlit application and tabulate package required in cli interface.

### Running the Application

To run the Streamlit application there are two ways:
1. You can visit this site [https://breachcheck-sagittarius.streamlit.app/](https://breachcheck-sagittarius.streamlit.app/) to use the Streamlit app which is hosted on Streamlit Sharing CLoud.
2. Using the batch file, use the following command:
    ```bash
    .\run_app.bat
    ```
3. Using the shortcut file named "Sagittarius" in the root directory of the project. It is the name of the team which made this project.

Note: If you are using the batch file, make sure to run it in the root directory of the project.

3. Don't run the Streamlit app manually, it will not work as expected since it requires the environment variables to be set.

4. To modify the user theme of the Streamlit app, you can change the necessary variables [here](.streamlit/config.toml). The theme is set to "dark" by default.

### Running the CLI Interface

To run the CLI interface manually, use the following command:
```bash
python app.py --cli
```

## Contributors

### Team Leader
1. [@VKrishna04](https://github.com/VKrishna04)

### Frontend
1. [@harsha4678](https://github.com/harsha4678) <- Figma Landing Page
2. [@longhxirguy](https://github.com/longhxirguy) <- Streamlit Frontend

### APIs Integration
1. [@Karthikkkk123](https://github.com/Karthikkkk123) <- Streamlit
2. [@Saisriram-88](https://github.com/Saisriram-88) <- CLI

### Support / Error Testing
1. [@Jayanth-0703](https://github.com/Jayanth-0703)