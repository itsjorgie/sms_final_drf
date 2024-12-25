// Send message
function sendMessage(event) {
    event.preventDefault(); // Prevent form submission

    // Get form data
    const formData = new FormData(document.getElementById("sendMessageFormElement"));
    const data = {
        message: formData.get("message"),  // Get message content from the form
    };

    // Get the token from localStorage
    const token = localStorage.getItem("access_token");
    if (!token) {
        alert("You need to log in first.");
        window.location.href = "/login"; // Redirect to login page
        return;
    }

    // Determine the system (send message to the correct URL)
    const system = getCurrentSystem();
    const sendUrl = system === "system1"
        ? "http://127.0.0.1:8001/api/system1/send/"
        : "http://127.0.0.1:8002/api/system2/send/";

    // Send the data to the backend
    fetch(sendUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
            "X-CSRFToken": formData.get("csrfmiddlewaretoken")  // CSRF token from the form
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
            document.getElementById("sendMessageFormElement").reset(); // Clear form after sending
        } else {
            alert("Failed to send message.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while sending the message.");
    });
}

// Add event listener to form submit
document.getElementById("sendMessageFormElement").addEventListener("submit", sendMessage);
