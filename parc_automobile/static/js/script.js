function dropNotification() {
    const notifBox = document.getElementById("notifications");
    notifBox.style.display = (notifBox.style.display === "flex") ? "none" : "flex";
}

document.addEventListener("DOMContentLoaded", () => {
    const closeBtn = document.querySelector("#notifications .bx-x");
    if (closeBtn) {
        closeBtn.addEventListener("click", () => {
            document.getElementById("notifications").style.display = "none";
        });
    }
});
