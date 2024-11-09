// Confirm before deletion
document.addEventListener("DOMContentLoaded", function() {
    const deleteButtons = document.querySelectorAll(".delete-button");
    deleteButtons.forEach(button => {
        button.addEventListener("click", function(event) {
            if (!confirm("Are you sure you want to delete this item?")) {
                event.preventDefault();
            }
        });
    });
});

// Form validation to ensure required fields are filled
function validateForm(form) {
    let isValid = true;
    const requiredFields = form.querySelectorAll("[required]");
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            field.classList.add("is-invalid");
            isValid = false;
        } else {
            field.classList.remove("is-invalid");
        }
    });
    return isValid;
}

// Attach validation on form submission
document.addEventListener("DOMContentLoaded", function() {
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", function(event) {
            if (!validateForm(form)) {
                event.preventDefault();
                alert("Please fill in all required fields.");
            }
        });
    });
});

// Auto fade-out for messages
document.addEventListener("DOMContentLoaded", function() {
    const alertBox = document.querySelector(".alert");
    if (alertBox) {
        setTimeout(() => {
            alertBox.style.transition = "opacity 1s ease";
            alertBox.style.opacity = 0;
            setTimeout(() => alertBox.remove(), 1000);
        }, 3000);  // 3 seconds
    }
});
