function dropRapport() {
    const modal = document.getElementById("rapportModal");
    modal.style.display = "block";
}

function closeRapport() {
    const modal = document.getElementById("rapportModal");
    modal.style.display = "none";
}

// Fermer si clic en dehors du contenu
window.onclick = function(event) {
    const modal = document.getElementById("rapportModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
};
