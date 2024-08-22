Certainly! Here's the full `README.md` content in its markup format:


# QR Code Generator

A simple Python application using Tkinter that generates and saves QR codes from a given website URL.

## Features

- Generate a QR code for a provided website URL.
- Display the QR code in the application window.
- Save the QR code as a PNG file.

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- [qrcode](https://pypi.org/project/qrcode/) library
- [Pillow](https://pypi.org/project/Pillow/) library (for image processing)

## Installation

1. **Install Python**: Ensure you have Python 3.x installed on your machine. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **Install Required Libraries**: Install the required libraries using pip. Open a terminal or command prompt and run the following commands:

   ```bash
   pip install qrcode[pil]
   pip install Pillow
   ```

   - [qrcode](https://pypi.org/project/qrcode/) is used for generating QR codes.
   - [Pillow](https://pypi.org/project/Pillow/) is used for handling and manipulating images.

## Usage

1. **Run the Application**: Save the provided code into a file named `qr_code_generator.py` and run it with Python or run it through the exe:

   ```bash
   python qr_code_generator.py
   ```

2. **Generate QR Code**:
   - Enter a website URL in the text entry box.
   - Click the "Generate QR Code" button to create the QR code.

3. **Save QR Code**:
   - Once the QR code is generated, click the "Save QR Code" button.
   - Choose the location and filename to save the QR code as a PNG file.

## Code Explanation

- **`generate_qr_code()`**: This function reads the URL from the entry box, generates a QR code using the `qrcode` library, resizes it, and updates the display label with the QR code image. It also enables the "Save QR Code" button.

- **`save_qr_code()`**: This function opens a file dialog to choose where to save the QR code image and saves it as a PNG file.

- **GUI Layout**: The application uses Tkinter to create a simple GUI with a title, entry box for the URL, buttons for generating and saving QR codes, and a label to display the generated QR code.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The [qrcode](https://pypi.org/project/qrcode/) library used for generating QR codes.
- The [Pillow](https://pypi.org/project/Pillow/) library used for image processing.
- Tkinter, which is a standard GUI library for Python.


This Markdown-formatted text is ready to be used as a `README.md` file for your project.