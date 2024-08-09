# YouTube Summarizer Web App

This project is a web-based application that summarizes YouTube videos using the Google Generative AI (Gemini) API. The app is designed to provide concise summaries of video content through an easy-to-use web interface.

## Features

- Extracts transcripts from YouTube videos.
- Generates AI-powered summaries using the Gemini API.
- Built with Streamlit for a simple and interactive web interface.
- Easy to configure and run locally.

## Requirements

Ensure you have Python 3.7+, Streamlit, and access to the Gemini API and YouTube Data API.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/youtube-summarizer.git
    cd youtube-summarizer
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the `.env` file:**
    Create a `.env` file in the root directory with your Google API key:
    ```plaintext
    GOOGLE_API_KEY=your_google_api_key
    ```

4. **Run the Streamlit web app:**
    Start the web app by executing:
    ```bash
    streamlit run app.py
    ```

## Usage

Open your web browser and navigate to `http://localhost:8501`. Enter a YouTube video URL, and click the "Summarize" button to get a concise summary of the video.

## Customization

You can modify the summarization process by editing the `app.py` file. For example, you can adjust the summarization settings, change the UI layout, or integrate additional features.

## Troubleshooting

If you encounter any issues:
- Verify that all dependencies are installed correctly.
- Ensure your Google API key is correctly set in the `.env` file.
- Check that the Gemini API and YouTube Data API are accessible.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
