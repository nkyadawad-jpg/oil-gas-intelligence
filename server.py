"""
Qatar O&G Opportunity Radar - Local Launch Server
Detect Early. Approach First. Convert Faster.
"""
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print("=" * 70)
        print(" QATAR O&G OPPORTUNITY RADAR - SALES COMMAND CENTER")
        print(" Detect Early • Approach First • Convert Faster")
        print("=" * 70)
        print(f" Serving live at: {url}")
        print(" Press Ctrl+C to stop the server.")
        print("=" * 70)
        
        # Try to open the default browser
        try:
            webbrowser.open(url)
        except Exception:
            pass

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down Qatar O&G Opportunity Radar server.")
            httpd.server_close()
            sys.exit(0)

if __name__ == "__main__":
    run()
