function setupUI() {
    const dice = document.getElementById("dice");

    if (dice) {
        dice.addEventListener("click", () => {
            rollDice();
        });
    }
}

function updateTurnUI(player) {
    const turn = document.getElementById("turn-player");

    if (turn) {
        turn.innerText = player.name + "'s Turn";
    }
}

function showWinner(player) {
    alert(player.name + " Wins The Game!");
}
