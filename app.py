
import os
import time
import socket
import logging
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Application configuration
APP_NAME = "AI Service Deployment Platform"
APP_VERSION = "1.0.0"
START_TIME = time.time()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": APP_NAME,
        "version": APP_VERSION
    }), 200


@app.route("/api/info")
def application_info():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": os.getenv("APP_ENV", "local"),
        "hostname": socket.gethostname(),
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "platform": "Docker-ready Flask application"
    })


@app.route("/api/inference", methods=["POST"])
def inference():
    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    logging.info("Inference request received")

    return jsonify({
        "service": "AI Inference Simulator",
        "status": "success",
        "input": prompt,
        "result": f"Simulated inference completed for: {prompt}",
        "model": "demo-model-v1"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
