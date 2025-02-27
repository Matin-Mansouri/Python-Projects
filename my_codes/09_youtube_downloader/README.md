# YouTube Video Downloader

A Python-based command-line tool for downloading YouTube videos with customizable quality settings and progress tracking.

## Features

- Download YouTube videos in various quality settings
- Progress bar showing download status
- Customizable output directory
- Support for highest quality automatic selection
- Error handling for unavailable videos


## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To download a YouTube video, run the following command:

```bash
python src/main.py <YouTube_URL> [-q <quality>] [-o <output_path>]
```

- `<YouTube_URL>`: The URL of the YouTube video to download.
- `-q <quality>`: The desired video quality (e.g., 720p, 1080p, highest). Defaults to `highest`.
- `-o <output_path>`: The output directory to save the video. Defaults to the current directory.

Example:

```bash
python src/main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ -q 720p -o /path/to/save
```

## Project Structure

- `src/main.py`: The main script containing the YouTube video downloader logic.
- `requirements.txt`: The file containing the required Python packages.

## Error Handling

The program handles various error cases:

- Unavailable videos
- Invalid quality selections (displays available qualities)
- Network errors
- Invalid URLs

## License

This project is licensed under the MIT License.
