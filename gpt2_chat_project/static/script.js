async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    const chatBox = document.getElementById("chat-box");

    // Display user message
    const userMessage = document.createElement("div");
    userMessage.classList.add("message", "user-message");
    userMessage.textContent = userInput;
    chatBox.appendChild(userMessage);

    // Send user input to the backend
    const response = await fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
    });
    const data = await response.json();

    // Display GPT-2 response
    const botMessage = document.createElement("div");
    botMessage.classList.add("message", "bot-message");
    botMessage.textContent = data.response;
    chatBox.appendChild(botMessage);

    // Clear user input
    document.getElementById("user-input").value = "";

    // Scroll to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}
