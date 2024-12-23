$(document).ready(function () {
    // Handle Send Button Click and Enter Key Press
    $("#send-btn").click(sendMessage);
    $("#user-input").keypress(function (event) {
        if (event.which === 13) {
            event.preventDefault();
            sendMessage();
        }
    });

    // Function to handle sending a message
    function sendMessage() {
        const userMessage = $("#user-input").val().trim();
        if (userMessage) {
            addMessage("user", userMessage); // Add user's message immediately
            $("#user-input").val(""); // Clear the input field

            // Simulate a delay before bot's response
            setTimeout(() => {
                // Send message to Flask backend
                $.ajax({
                    url: "/get_response",
                    type: "POST",
                    contentType: "application/json",
                    data: JSON.stringify({ message: userMessage }),
                    success: function (response) {
                        // Add bot's message after receiving the response
                        addMessage("bot", response.response);
                    },
                    error: function () {
                        // Add an error message if server request fails
                        addMessage("bot", "Error: Could not connect to the server.");
                    },
                });
            }, 1000); // 1-second delay
        }
    }

    // Function to add messages to the chat body with fade-in animation
    function addMessage(sender, text) {
        const messageDiv = `<div class="message ${sender}">${text}</div>`;
        $("#chat-body").append($(messageDiv).hide().fadeIn(500));
        $("#chat-body").scrollTop($("#chat-body")[0].scrollHeight);
    }
});
