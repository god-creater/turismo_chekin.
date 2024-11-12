// script.js
document.getElementById("checkinForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let formData = {
        first_name: document.getElementById("first_name").value,
        last_name: document.getElementById("last_name").value,
        city: document.getElementById("city").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value
    };

    fetch("/checkin", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("statusMessage").textContent = data.message;
    })
    .catch(error => console.error("Erro:", error));
});
