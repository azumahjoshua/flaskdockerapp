from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
@app.route('/')
@app.route('/')
def hello_geek():
    redis.incr('hits')
    counter = redis.get('hits').decode('utf-8')
    
    # Add custom messages based on visit count
    if int(counter) == 1:
        message = "Welcome! This is your first visit!"
    elif int(counter) % 10 == 0:
        message = f"Wow, you've hit {counter} visits! Keep it up!"
    else:
        message = "Thanks for stopping by!"

    return f"""
        <html>
        <head>
            <style>
                body {{
                    background-color: #f0f8ff; /* Light blue background */
                    text-align: center;
                    font-family: Arial, sans-serif;
                }}
                h1 {{
                    color: #333; /* Darker text for contrast */
                }}
                h2 {{
                    color: #555; /* Secondary text color */
                }}
            </style>
        </head>
        <body>
            <h1>This webpage has been viewed {counter} time(s)</h1>
            <h2>{message}</h2>
        </body>
        </html>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
