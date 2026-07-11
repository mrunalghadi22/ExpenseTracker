const toggles = document.querySelectorAll(".password-toggle");

toggles.forEach(button => {

    button.addEventListener("click", () => {

        const input = document.getElementById(
            button.dataset.target
        );

        const icon = button.querySelector("span");

        if (input.type === "password") {

            input.type = "text";

            icon.textContent = "visibility_off";

        } else {

            input.type = "password";

            icon.textContent = "visibility";

        }

    });

});

const password = document.getElementById("newPassword");

const bar = document.getElementById("strengthBar");

const text = document.getElementById("strengthText");

password.addEventListener("input", () => {

    const value = password.value;

    let score = 0;

    if(value.length >= 8) score++;

    if(/[A-Z]/.test(value)) score++;

    if(/[0-9]/.test(value)) score++;

    if(/[^A-Za-z0-9]/.test(value)) score++;

    const widths = [

        "0%",

        "25%",

        "50%",

        "75%",

        "100%"

    ];

    const colors = [

        "#E2E8F0",

        "#EF4444",

        "#F59E0B",

        "#3B82F6",

        "#10B981"

    ];

    const labels = [

        "",

        "Weak",

        "Fair",

        "Good",

        "Strong"

    ];

    bar.style.width = widths[score];

    bar.style.background = colors[score];

    text.textContent = labels[score];

});