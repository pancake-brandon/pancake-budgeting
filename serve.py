#!/usr/bin/env python3
"""
Simple HTTP server for testing the Pancake landing page locally.
This server properly handles CORS and allows the form to communicate with the backend.

Usage:
    python3 serve.py

Then open: http://localhost:3000
"""

import http.server
import socketserver
import os
import sys
from urllib.parse import urlparse

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler with CORS headers."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        """Add CORS headers to every response."""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

    def do_OPTIONS(self):
        """Handle preflight OPTIONS request."""
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        """Log HTTP requests."""
        sys.stderr.write(f"[{self.log_date_time_string()}] {format%args}\n")

def main():
    """Start the local web server."""
    os.chdir(DIRECTORY)

    print(f"""
╔══════════════════════════════════════════════════════════════╗
║                   Pancake Landing Page Server                ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Server starting on: http://localhost:{PORT}                    ║
║                                                              ║
║  Make sure the backend is also running:                     ║
║  cd ../pancake-backend                                      ║
║  source venv/bin/activate                                   ║
║  uvicorn app.main:app --reload --port 8000                  ║
║                                                              ║
║  Press Ctrl+C to stop the server                            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)

    try:
        with socketserver.TCPServer(("", PORT), CORSHTTPRequestHandler) as httpd:
            print(f"Server running at http://localhost:{PORT}/")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✓ Server stopped")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Port already in use
            print(f"\n❌ Error: Port {PORT} is already in use.")
            print(f"   Try closing other applications or use a different port.\n")
        else:
            print(f"\n❌ Error: {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
