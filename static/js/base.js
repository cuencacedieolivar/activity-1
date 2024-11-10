// base.js

// Log a simple message to test that JS is loaded
console.log('Plant Monitoring System Loaded');

// Function to alert when a user adds a care log
function alertCareLogSubmission() {
    alert("Care log submitted successfully!");
}

// Example: Handling AJAX request for plant updates or care logs (optional)
function updatePlantStatus(plantId, status) {
    fetch(`/plants/${plantId}/update/`, {
        method: 'POST',
        body: JSON.stringify({ status: status }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}

// Example of handling form submission for care log creation (optional)
document.getElementById("care-log-form").addEventListener("submit", function(event) {
    event.preventDefault();
    alertCareLogSubmission();
});
