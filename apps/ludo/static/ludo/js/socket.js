let socket = null;

function initSocket() {
    const protocol = window.location.protocol === "https:" ? "wss://" : "ws://";

    socket = new WebSocket(
        protocol + window.location.host + "/ws/ludo/"
    );

    socket.onopen = () => {
        console.log("WebSocket Connected");
    };

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);

        console.log("Socket Message:", data);
    };

    socket.onclose = () => {
        console.log("WebSocket Closed");
    };
}

function sendGameData(data) {
    if (socket && socket.readyState === WebSocket.OPEN) {
        socket.send(JSON.stringify(data));
    }
}
