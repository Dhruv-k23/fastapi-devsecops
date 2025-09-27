# app/main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI DevSecOps Live</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f4f7f9;
        }

        .welcome-message {
            font-size: 3em;
            color: #1e40af; /* Deep Blue */
            opacity: 0;
            transform: translateY(20px);
            /* Apply the animation */
            animation: fadeInSlideUp 1.5s ease-out forwards;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
            padding: 20px;
            border-bottom: 3px solid #3b82f6;
        }

        .link-text {
            position: absolute;
            bottom: 20px;
            color: #555;
            font-size: 0.9em;
        }

        /* Keyframe definition for the smooth animation */
        @keyframes fadeInSlideUp {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <div class="welcome-message">
        Hello, DevSecOps Deployed!
    </div>
    <div class="link-text">
        <p>Check API Docs: <a href="/docs" style="color: #3b82f6; text-decoration: none;">/docs</a></p>
    </div>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def root():
    """
    Returns an HTML response with an animated welcome message.
    """
    return HTML_CONTENT
