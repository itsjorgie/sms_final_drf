// Send message
function sendMessage(event) {
    event.preventDefault();

    const formData = new FormData(document.getElementById("sendMessageFormElement"));
    const data = {
        user_id: formData.get("user_id"),
        message: formData.get("message")
    };

    const token = localStorage.getItem("access_token");
    if (!token) {
        alert("You need to log in first.");
        window.location.href = "/login"; // Redirect to login page
        return;
    }

    const system = getCurrentSystem();
    const sendUrl = system === "system1"
        ? "http://127.0.0.1:8001/api/system1/send/"
        : "http://127.0.0.1:8002/api/system2/send/";

    fetch(sendUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Failed to send message: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.message) {
            alert("Message sent successfully!");
            document.getElementById("sendMessageFormElement").reset(); // Clear form after successful send
        } else {
            alert("Failed to send message.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while sending the message.");
    });
}
