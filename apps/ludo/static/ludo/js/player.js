function createPlayers() {
    players.push({
        id: 1,
        name: "Player 1",
        color: "red",
        position: 0
    });

    players.push({
        id: 2,
        name: "Player 2",
        color: "blue",
        position: 0
    });
}

function moveCurrentPlayer(steps) {
    const player = players[currentPlayerIndex];

    player.position += steps;

    console.log(player.name + " moved to " + player.position);

    animateToken(player);

    if (player.position >= 100) {
        showWinner(player);
        return;
    }

    nextTurn();
}
