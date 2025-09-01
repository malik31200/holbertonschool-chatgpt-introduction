document.getElementById("colorButton").addEventListener("click", function() {
    changeBackgroundColor();
});

function changeBackgroundColor() {
    // Génère une couleur aléatoire
    var randomColor = "#" + Math.floor(Math.random() * 16777215).toString(16);
    // Change la couleur de fond
    document.body.style.backgroundColor = randomColor;
}

