// Show section
function showSection(sectionId) {
    const sections = document.querySelectorAll("main > div");
    sections.forEach(section => section.style.display = "none");

    const selectedSection = document.getElementById(sectionId);
    if (selectedSection) {
        selectedSection.style.display = "block";
    }
}

// Determine the current system based on the URL
function getCurrentSystem() {
    const currentUrl = window.location.href;
    if (currentUrl.includes("8001")) {
        return "system1";
    } else if (currentUrl.includes("8002")) {
        return "system2";
    }
    return null;
}

// Show inbox and fetch messages based on the current system
function showInbox() {
    const system = getCurrentSystem();
    if (!system) {
        alert("Unable to determine the system.");
        return;
    }
    fetchReceivedMessages(system);
    showSection("receivedMessagesForm");
}

// Fetch received messages
function fetchReceivedMessages(system) {
    const token = localStorage.getItem("access_token");
    if (!token) {
        alert("You need to log in first.");
        window.location.href = "/inbox"; // Redirect to login page
        return;
    }

    const receiveUrl = system === "system1"
        ? "http://127.0.0.1:8001/api/system1/received/"
        : "http://127.0.0.1:8002/api/system2/received/";

    fetch(receiveUrl, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Failed to fetch messages: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        const messageList = document.getElementById("receivedMessagesList");
        messageList.innerHTML = ""; // Clear any previous messages

        if (Array.isArray(data) && data.length === 0) {
            const noMessagesItem = document.createElement("li");
            noMessagesItem.textContent = "No messages received yet.";
            messageList.appendChild(noMessagesItem);
        } else {
            data.forEach(msg => {
                const listItem = document.createElement("li");
                listItem.textContent = msg.message;
                messageList.appendChild(listItem);
            });
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while fetching received messages.");
    });
}

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
