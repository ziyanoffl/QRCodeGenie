# QR Code Generator
This project is a web application built using Flask, a lightweight web framework in Python. It allows users to generate QR codes from provided links.

## Technologies Used
- Flask
- qrcode
- Pillow (PIL)
- HTML, CSS, Bootstrap

## How to Run Locally
1. Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the Flask application:
    ```bash
    python app.py
    ```
3. The application will start locally at http://localhost:5000.

## How to Deploy on Vercel
1. Create a Vercel Account.
2. Install the Vercel CLI:
    ```bash
    npm install -g vercel
    ```
3. Log in to your Vercel account using:
    ```bash
    vercel login
    ```
4. Deploy the application:
    ```bash
    vercel
    ```
5. Follow the prompts to deploy the application. Vercel will provide you with a unique URL for your deployed app.

## Learnings
- Flask: Learned how to use Flask to create a basic web application, handle routes, and render HTML templates.
- qrcode Library: Gained experience in using the qrcode library to generate QR codes in Python.
- Image Handling: Learned how to save and encode images using the PIL library.
- Deployment with Vercel: Explored deploying a Python web application on Vercel.
