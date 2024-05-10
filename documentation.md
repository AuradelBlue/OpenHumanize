# Text Manipulation Application Documentation

## Overview
This application uses the spaCy NLP library to process text input by tokenizing it. It is designed to run entirely on-device, with configurations easily managed through environment variables.

## Detailed Features
- **Tokenization:** Converts text input into a list of tokens.
- **Web Interface:** A simple web form to submit text and view tokenized results.
- **API Endpoints:** 
  - `GET /`: Renders the homepage with a form for text submission.
  - `POST /process`: Accepts text and returns the tokenized form both as JSON and in the web interface.

## Configuration
- **`.env` File:** Manages settings such as the spaCy model.
  - `SPACY_MODEL=en_core_web_sm`: Defines which spaCy model is used for processing text.

## Installation and Setup
### Prerequisites
- Python 3.8 or higher
- pip for managing Python packages

### Steps
1. **Clone Repository**: Download the code from the repository link.
2. **Environment Setup**:
   - Windows: Run `start.bat` to set up the environment and install dependencies.
   - Linux/macOS: Refer to the section on setting up in non-Windows environments.
3. **Model Installation**: The spaCy model specified in `.env` is automatically installed if not already present.

## Using the Application
- **Starting the Application**: Execute `start.bat` on Windows or the equivalent script on other systems.
- **Web Interface**: Access the web interface by navigating to `http://localhost:5000` in your web browser after starting the application.
- **API Usage**:
  - Send a GET request to `/` to retrieve the form.
  - Send a POST request with `text="your sample text"` to `/process` to get the tokenized text.

## Security and Best Practices
- **Debug Mode**: It's enabled by default for development purposes. Ensure to disable it in production by setting `app.run(debug=False)`.
- **Environment Variables**: Store sensitive configurations like API keys or database credentials securely.

## Cross-Platform Usage
- **Non-Windows Setup**:
  - Ensure Python and pip are installed.
  - Use `chmod +x setup.sh` to make the setup script executable.
  - Run `./setup.sh` to create a virtual environment and install dependencies.

## Example
```bash
curl -X POST -F 'text=Hello, world!' http://localhost:5000/process
```
Response:
```json
{
  "tokens": ["Hello", ",", "world", "!"]
}
```

## Troubleshooting
- **Python Not Found**: Ensure Python is installed and in your PATH.
- **Dependency Errors**: Check if the virtual environment is activated and all packages are installed as listed in `requirements.txt`.

## API Reference
- **GET `/`**: Renders the homepage.
- **POST `/process`**: Accepts a `text` field and returns the tokenized result.

## Contributing
- **Guidelines**: Please follow the coding standards and submit pull requests for any improvements or bug fixes.

## Version History
- **v1.0**: Initial release with basic tokenization features.

## Maintenance and Updates
- **Update Procedures**: Regular updates will be provided to improve functionality and security.

