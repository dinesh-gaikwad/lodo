const players = [];
let currentPlayerIndex = 0;
let gameStarted = false;

function initGame() {
    createPlayers();
    renderBoard();
    gameStarted = true;

    console.log("Game Started");
}

function renderBoard() {
    const board = document.querySelector(".ludo-board");

    if (!board) return;

    for (let i = 0; i < 225; i++) {
        const cell = document.createElement("div");
        cell.classList.add("cell");
        board.appendChild(cell);
    }
}

function nextTurn() {
    currentPlayerIndex++;

    if (currentPlayerIndex >= players.length) {
        currentPlayerIndex = 0;
    }

    updateTurnUI(players[currentPlayerIndex]);
}
