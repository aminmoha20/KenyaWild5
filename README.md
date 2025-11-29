# ProjectBig5 – Group 3 Meta Web Big5 Project

## Overview
This is a Django web project showcasing Kenya’s **Big Five wildlife** (Lion, Leopard, Elephant, Rhino, and Buffalo).  
It includes a homepage with navigation, search functionality, and styled sections for **Home**, **About**, and **Contact Us**.

## Features
- **Homepage Layout**: Built with a base template (`index.html`) and extended by `main.html`.
- **Navigation Bar**: Links to Home, About, and Contact Us, plus a search bar.
- **Footer**: Consistent footer across pages.
- **Static Files**: Custom CSS (`style.css`) located in `firstApp/static/firstApp/`.
- **Templates**:
  - `index.html` – Base layout with navbar, footer, and content block.
  - `main.html` – Homepage content (Big Five intro, About, Contact Us).
  - `nav.html` – Navigation bar included in base template.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/projectBig5.git
   cd projectBig5

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
3. Install dependencies:
```bash
pip install django
```

4. Run the development server:
```bash
python manage.py runserver
```
5. Open the site at:
```bash
http://127.0.0.1:8000/
```

## Licences
MIT License
Copyright (c) 2025 Group 3 Meta Web Big5 Project
