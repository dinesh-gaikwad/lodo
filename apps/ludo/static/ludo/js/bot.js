function botPlay() {
    console.log("Bot Playing");

    const randomDelay = Math.floor(Math.random() * 2000) + 1000;

    setTimeout(() => {
        const diceValue = rollDice();

        console.log("Bot Rolled:", diceValue);
    }, randomDelay);
}

function enableBotMode() {
    console.log("Bot Mode Enabled");
}
