const chatArea = document.getElementById('chat-area');
const chatInput = document.getElementById('chat-input');

let conversationId = '';  // Stores the current conversation_id

function sendMessage() {
    const message = chatInput.value.trim();
    if (!message) return;

    // Add user message to chat area
    const userMessage = document.createElement('div');
    userMessage.className = 'message user-message';
    userMessage.innerHTML = `
        <div class="message-bubble">${message}</div>
        <div class="message-time">${new Date().toLocaleTimeString()}</div>
    `;
    chatArea.appendChild(userMessage);
    chatInput.value = '';

    // Show typing indicator
    const typing = document.createElement('div');
    typing.className = 'message bot-message';
    typing.innerHTML = '<div class="message-bubble typing">Typing...</div>';
    chatArea.appendChild(typing);
    chatArea.scrollTop = chatArea.scrollHeight;

    // AJAX call to backend
    $.ajax({
        url: baseUrl + 'chatbot/chat/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ message, conversation_id: conversationId }),
        success: function(data) {
            typing.remove();

            const botMessage = document.createElement('div');
            botMessage.className = 'message bot-message';
            botMessage.innerHTML = `
                <div class="message-bubble">${data.response}</div>
                <div class="message-time">${new Date().toLocaleTimeString()}</div>
            `;
            chatArea.appendChild(botMessage);
            chatArea.scrollTop = chatArea.scrollHeight;

            // Update conversation ID from backend response
            if (data.conversation_id) {
                conversationId = data.conversation_id;
            }
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
            typing.remove();

            const errorMessage = document.createElement('div');
            errorMessage.className = 'message bot-message';
            errorMessage.innerHTML = `
                <div class="message-bubble">Sorry, something went wrong!</div>
                <div class="message-time">${new Date().toLocaleTimeString()}</div>
            `;
            chatArea.appendChild(errorMessage);
        }
    });
}

// Send message on Enter key
chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});
