
async function loadDashboard() {
    try {
        const response = await fetch("/api/info");
        const data = await response.json();

        document.getElementById("app-name").textContent = data.application;
        document.getElementById("environment").textContent = data.environment;
        document.getElementById("hostname").textContent = data.hostname;
        document.getElementById("version").textContent = data.version;

        document.getElementById("status").textContent = "● SERVICE HEALTHY";

    } catch (error) {
        document.getElementById("status").textContent = "● SERVICE UNAVAILABLE";
        console.error("Dashboard loading failed:", error);
    }
}

async function runInference() {
    const prompt = document.getElementById("prompt").value.trim();
    const result = document.getElementById("result");

    if (!prompt) {
        result.textContent = "Please enter a prompt.";
        return;
    }

    result.textContent = "Processing request...";

    try {
        const response = await fetch("/api/inference", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();

        result.textContent = JSON.stringify(data, null, 2);

    } catch (error) {
        result.textContent = "Inference request failed.";
        console.error(error);
    }
}

loadDashboard();
