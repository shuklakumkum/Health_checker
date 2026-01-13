import ssl
import socket
from datetime import datetime
from urllib.parse import urlparse

# Check SSL certificate of a website
def check_ssl(url):
    try:
        host = urlparse(url).hostname
        context = ssl.create_default_context()
        conn = socket.create_connection((host, 443))
        secure_socket = context.wrap_socket(conn, server_hostname=host)
        cert = secure_socket.getpeercert()
        secure_socket.close()
        conn.close()

        issuer = cert['issuer'][0][0][1] if cert.get("issuer") else None

        expiry = cert['notAfter']
        expiry = expiry.replace(" GMT", "")  # Remove timezone if present
        expiry_date = datetime.strptime(expiry, "%b %d %H:%M:%S %Y")
        days_left = (expiry_date - datetime.utcnow()).days

        return {
            "valid": days_left > 0,
            "expires_in_days": days_left,
            "expires_on": expiry_date.strftime("%Y-%m-%d"),
            "issuer": issuer,
            "error": None
        }

    except Exception as error:
        return {
            "valid": False,
            "expires_in_days": None,
            "expires_on": None,
            "issuer": None,
            "error": str(error)
        }
