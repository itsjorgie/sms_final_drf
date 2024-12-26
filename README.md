Django REST Framework (DRF) Secure Message Applications
🌟Welcome to our MessagePro project! FAST. SECURE. RELIABLE.🚀 This is a secure, real-time, two-server messaging system built using Django REST Framework (DRF) and MySQL (via Laragon). It enables encrypted communication between two servers: System 1 (running on port 8001) and System 2 (running on port 8002). The project focuses on ensuring secure, dynamic, and real-time communication through custom middleware for encryption and decryption.

🛠️ Features
🔐 User Authentication
Secure login and registration for both applications.
Role-based access control (if needed).

✉️ Message Transmission
Real-time messaging between the two systems.
Messages are encrypted before transmission and decrypted upon receipt to ensure confidentiality.
Dynamic Communication: Messages are transmitted and processed seamlessly without delay.

🛡️ Security Features
Default (Django) Middleware and Cryptography for:
Encrypting outgoing data.
Decrypting incoming messages.
Hashing sensitive information and validating requests.

📊 Dashboard
A user-friendly dashboard to:
Monitor sent and received messages.

🧑‍💻 Real-time Updates
Instant reflection of messages on the receiving server, ensuring a smooth user experience.

🚀 Installation Guide
Prerequisites
Python 3.10+
MySQL (via Laragon)
Django
Django REST Framework
cryptography library
decouple library for managing environment variables
Step 1: Clone the Repository
# Clone the repository
$ git clone <repository_url>
$ cd MessagePro
Step 2: Create a Virtual Environment
# Create and activate a virtual environment
$ python -m venv venv
$ source venv/bin/activate  - For Linux/Mac
$ venv\Scripts\activate  - For Windows
Step 3: Install Dependencies
# Install required Python packages
$ pip install -r requirements.txt
Step 4: Configure the Database
Set up two MySQL databases for System 1 and System 2 using Laragon.
Update the DATABASES settings in the settings.py file of each system.
Step 5: Generate Fernet Encryption Key
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
Copy the generated key and store it securely in the environment variables of both systems as FERNET_SECRET_KEY.
Step 6: Apply Migrations
# Apply migrations
$ python manage.py makemigrations
$ python manage.py migrate
Step 7: Run the Servers
For System 1:
$ python manage.py runserver 8001
For System 2:
$ python manage.py runserver 8002

🌟 Usage Guide
Register and Login
Use the /api/register/ endpoint to create a new user.
Login with the /api/login/ endpoint to receive an authentication token.
Send and Receive Messages
Use the /dashboard/send_message/ endpoint to send encrypted messages.
Retrieve messages using the /dashboard/inbox/ endpoint, where decryption happens automatically.
Access the Servers
Server 1: http://127.0.0.1:8001
Server 2: http://127.0.0.1:8002

🔒 Security Considerations
FERNET_SECRET_KEY: Ensure this key is stored securely in environment variables and not hard-coded in the repository.
HTTPS: Use HTTPS for all communication in production to ensure data integrity and confidentiality.
Regular Updates: Keep dependencies up to date to address any security vulnerabilities.

👥 Contributors
Leader: Shaira Micompal
Team Members: Althea Loraine Buna
              Ushyne Esclamado
              Jorgie Escol

Thank you for using MessagePro! We hope this system serves as a secure and efficient messaging solution. 🛡️📨

