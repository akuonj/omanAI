# omanAI - Intelligent Object Detection System

omanAI is a state-of-the-art object detection system powered by YOLOv8, providing real-time analysis with detailed classification results and annotated output images.


## Features

- 🚀 Instant image analysis with YOLOv8 model
- 🔍 Object detection with confidence percentages
- 📥 Download annotated images with bounding boxes
- 🌈 Modern web interface with animations
- 📱 Fully responsive design
- ⚡ Fast processing (<5 seconds average)

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup

#### Clone repository
```bash
git clone https://github.com/akuonj/omanAI.git
cd omanAI
```
#### Create virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate
```
```bash
# Ubuntu
python3 -m venv venv
source venv/bin/activate
```
#### Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Start Server

**Production (Linux):**
```bash
gunicorn --bind 127.0.0.1:8007 object_detection_ui.wsgi:application --daemon
```

**Development (All OS):**
```bash
python manage.py runserver
```

Access the application at:  
🌐 [http://127.0.0.1:8007](http://127.0.0.1:8007) (Production)  
🌐 [http://127.0.0.1:8000](http://127.0.0.1:8000) (Development)

### How to Use

1. **Upload Image**  
   Click "Choose File" and select any JPG/PNG image

2. **Analyze**  
   Click the "Analyze" button

3. **View Results**  
   See detected objects with confidence percentages

4. **Download**  
   Click "Download" for annotated image

## Technical Details

- **Model**: YOLOv8 (Ultralytics implementation)
- **Classes**: 80 common object categories
- **Framework**: Django
- **Interface**: Tailwind CSS + Anime.js

## Support

For support or feature requests:  
📧 Joshua Otieno  
🐛 [Issue Tracker](https://github.com/akuonj/omanAI/issues)  
👨💻 [GitHub Profile](https://github.com/akuonj)
