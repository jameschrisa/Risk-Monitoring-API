# Phishing Detection API


# Phishing Detection API

This project implements a RESTful API for phishing detection using machine learning techniques. It analyzes URLs, emails, and messages for potential phishing attempts and provides risk assessments.

## Features

- URL analysis for phishing patterns
- Email content analysis
- Message content analysis
- Retrieval of current phishing patterns and trends
- Machine learning model for adaptive phishing detection
- Rate limiting to prevent abuse
- Caching for improved performance

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/phishing-detection-api.git
   cd phishing-detection-api
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

The project uses environment variables for configuration. You can set these in a `.env` file in the root directory of the project. Here's an example:

```
DEBUG=False
CACHE_TYPE=SimpleCache
CACHE_DEFAULT_TIMEOUT=300
RATELIMIT_DEFAULT=100 per minute
PHISHTANK_API_URL=http://data.phishtank.com/data/online-valid.json
ALEXA_TOP_SITES_URL=http://s3.amazonaws.com/alexa-static/top-1m.csv.zip
```

## Running the Application

To run the application locally:

```
python app.py
```

The API will be available at `http://localhost:5000`.

## API Endpoints

1. **Analyze URL**
   - Endpoint: `/analyze_url`
   - Method: POST
   - Payload: `{"url": "http://example.com"}`

2. **Analyze Email**
   - Endpoint: `/analyze_email`
   - Method: POST
   - Payload: `{"email_content": "Email content here"}`

3. **Analyze Message**
   - Endpoint: `/analyze_message`
   - Method: POST
   - Payload: `{"message": "Message content here"}`

4. **Get Phishing Patterns**
   - Endpoint: `/get_patterns`
   - Method: GET

## Running Tests

To run the test suite:

```
python -m unittest discover tests
```


## Configuration

The project uses environment variables for configuration. You can set these in a `.env` file in the root directory of the project. Here's an example:

```
DEBUG=False
CACHE_TYPE=SimpleCache
CACHE_DEFAULT_TIMEOUT=300
RATELIMIT_DEFAULT=100 per minute
PHISHTANK_API_URL=http://data.phishtank.com/data/
PHISHTANK_API_KEY=your_phishtank_api_key_here
ALEXA_TOP_SITES_URL=http://s3.amazonaws.com/alexa-static/top-1m.csv.zip
```

### PhishTank API Key

To use this application, you need to obtain an API key from PhishTank:

1. Go to [PhishTank's website](https://www.phishtank.com/)
2. Sign up for an account if you don't have one
3. Once logged in, go to the [Developer Information page](https://www.phishtank.com/developer_info.php)
4. Request an API key
5. Once you have your API key, add it to your `.env` file as shown in the example above

**Note:** Keep your API key confidential and do not share it publicly.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational and research purposes only. Do not use it to analyze URLs or content without proper authorization. The authors are not responsible for any misuse or damage caused by this program.




