# QR-Code-Generator

A simple Python project to generate QR code images from user-provided URLs or text.

## Features

- Command-line interface for input
- Generates QR code images using the `qrcode` library
- Customizable QR code size, error correction, and colors
- Saves the generated QR code as `qr_code.png`

## Usage

1. **Install dependencies**  
	Make sure you have Python installed.  
	Install the required package:
	```
	pip install qrcode[pil]
	```

2. **Run the script**  
	```
	python Src/main.py
	```
	Enter the URL or text when prompted.  
	The QR code image will be saved as `Src/qr_code.png`.

## Project Structure

```
QR-Code-Generator/
├── LICENSE
├── README.md
└── Src/
	 ├── main.py
	 └── qr_code.png
```

## License

This project is licensed under the MIT License.