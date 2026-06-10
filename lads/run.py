import subprocess

print("Starting WayZe Lads Cyber Defense OS...")

subprocess.run([
    "uvicorn",
    "gateway.app:app",
    "--host", "0.0.0.0",
    "--port", "8000"
])