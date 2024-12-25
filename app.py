from flask import Flask
from redis import Redis

app = Flask(__name__)
# Connect to Redis with hostname 'redis' and port 6379
redis = Redis(host='redis', port=6379)
# redis = Redis(host='localhost', port=6379)

@app.route('/')
def hello_geek():
    try:
        # Increment the Redis counter
        redis.incr('hits')
        counter = redis.get('hits').decode('utf-8')
        
        # Custom messages based on the visit count
        if int(counter) == 1:
            message = "Welcome! This is your first visit!"
        elif int(counter) % 10 == 0:
            message = f"Wow, you've hit {counter} visits! Keep it up!"
        else:
            message = "Thanks for stopping by!"

        # HTML Response
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
    except Exception as e:
        # Return error message in case of Redis issues
        return f"<h1>Error connecting to Redis: {str(e)}</h1>"

if __name__ == "__main__":
    # Run Flask app in debug mode and bind to all IPs
    app.run(debug=True, host="0.0.0.0")
