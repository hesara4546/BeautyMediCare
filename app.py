from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# YOUR GOOGLE REVIEW LINK
GOOGLE_MAPS_URL = "https://g.page/r/CQMs8wCYWABIEBM/review"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beauty Medi Care | Dr. Dileepa</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #00d2ff;
            --secondary: #92fe9d;
            --glass: rgba(255, 255, 255, 0.1);
            --border: rgba(255, 255, 255, 0.15);
        }

        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Inter', sans-serif;
            background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #1a2a6c);
            background-size: 400% 400%;
            animation: gradientMove 12s ease infinite;
            color: white;
            overflow: hidden;
        }

        @keyframes gradientMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .container {
            background: var(--glass);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            border-radius: 40px;
            padding: 60px 40px;
            text-align: center;
            width: 85%;
            max-width: 420px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.5);
            animation: cardEntrance 1.2s cubic-bezier(0.23, 1, 0.32, 1);
        }

        @keyframes cardEntrance {
            from { opacity: 0; transform: scale(0.9) translateY(30px); }
            to { opacity: 1; transform: scale(1) translateY(0); }
        }

        .welcome-text {
            font-family: 'Playfair Display', serif;
            font-size: 32px;
            line-height: 1.2;
            margin-bottom: 5px;
            background: linear-gradient(to right, #fff, var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: textGlow 3s ease-in-out infinite alternate;
        }

        @keyframes textGlow {
            from { filter: drop-shadow(0 0 2px rgba(255,255,255,0.2)); }
            to { filter: drop-shadow(0 0 10px var(--primary)); }
        }

        .dr-subtext {
            font-size: 14px;
            letter-spacing: 4px;
            text-transform: uppercase;
            opacity: 0.7;
            margin-bottom: 30px;
            font-weight: 600;
        }

        .stars { margin: 40px 0; display: flex; justify-content: center; gap: 10px; }
        .star {
            font-size: 50px;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            color: rgba(255,255,255,0.15);
        }

        .star:hover {
            color: #ffca28;
            transform: scale(1.3);
            filter: drop-shadow(0 0 15px #ffca28);
        }

        .input-box { display: none; }
        
        textarea {
            width: 100%;
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--border);
            border-radius: 20px;
            color: white;
            padding: 15px;
            outline: none;
            resize: none;
            box-sizing: border-box;
            margin-bottom: 20px;
            font-size: 16px;
        }

        button {
            background: white;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            color: #1a2a6c;
            font-weight: 800;
            cursor: pointer;
            transition: 0.3s;
            text-transform: uppercase;
        }

        button:hover { 
            background: var(--primary); 
            color: white; 
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0,210,255,0.4);
        }

        .hidden { display: none; }
        .fade-in { animation: fadeIn 0.8s forwards; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

    </style>
</head>
<body>
    <div class="container">
        <div id="welcome-section">
            <div class="welcome-text">Welcome To<br>Beauty Medi Care</div>
            <div class="dr-subtext">By Dr. Dileepa</div>
            
            <div id="rating-step">
                <p style="margin-top: 40px; opacity: 0.6;">How would you rate your experience?</p>
                <div class="stars">
                    <span class="star" onclick="rate(1)">★</span>
                    <span class="star" onclick="rate(2)">★</span>
                    <span class="star" onclick="rate(3)">★</span>
                    <span class="star" onclick="rate(4)">★</span>
                    <span class="star" onclick="rate(5)">★</span>
                </div>
            </div>
        </div>

        <div id="feedback-step" class="input-box">
            <p>Help us improve your next visit:</p>
            <textarea rows="4" placeholder="Tell us more..."></textarea>
            <br>
            <button onclick="finish()">Send Feedback</button>
        </div>

        <div id="thanks-step" class="hidden">
            <h2 style="color: var(--secondary); font-size: 40px;">✔</h2>
            <h3 style="font-family: 'Playfair Display';">Thank You</h3>
            <p>Your response has been sent to our team.</p>
        </div>
    </div>

    <script>
        function rate(n) {
            if (n >= 4) {
                document.body.style.background = "white";
                setTimeout(() => {
                    window.location.href = "{{ google_url }}";
                }, 200);
            } else {
                document.getElementById('rating-step').classList.add('hidden');
                document.getElementById('feedback-step').style.display = 'block';
                document.getElementById('feedback-step').classList.add('fade-in');
            }
        }

        function finish() {
            document.getElementById('feedback-step').style.display = 'none';
            document.getElementById('thanks-step').classList.remove('hidden');
            document.getElementById('thanks-step').classList.add('fade-in');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, google_url=GOOGLE_MAPS_URL)

if __name__ == '__main__':
    # Render provides a PORT environment variable, we must use it
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
