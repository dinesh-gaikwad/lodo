function animateToken(player) {
    const token = document.querySelector("." + player.color + "-token");

    if (!token) return;

    token.classList.add("token-move");

    setTimeout(() => {
        token.classList.remove("token-move");
    }, 500);
}

function flashBoard() {
    const board = document.querySelector(".ludo-board");

    if (!board) return;

    board.style.opacity = "0.5";

    setTimeout(() => {
        board.style.opacity = "1";
    }, 200);
}
