const diceImages = [
    "/static/ludo/images/dice/1.png",
    "/static/ludo/images/dice/2.png",
    "/static/ludo/images/dice/3.png",
    "/static/ludo/images/dice/4.png",
    "/static/ludo/images/dice/5.png",
    "/static/ludo/images/dice/6.png"
];

function rollDice() {
    const dice = document.getElementById("dice");

    dice.classList.add("dice-roll");

    setTimeout(() => {
        dice.classList.remove("dice-roll");
    }, 600);

    const value = Math.floor(Math.random() * 6) + 1;

    dice.src = diceImages[value - 1];

    console.log("Dice Rolled:", value);

    moveCurrentPlayer(value);

    return value;
}
