const modal = document.getElementById("confirmModal");
const deleteForm = document.getElementById("deleteForm");
const categoryName = document.getElementById("categoryName");

document.querySelectorAll(".delete-btn").forEach(button => {

    button.addEventListener("click", () => {

        categoryName.textContent = button.dataset.name;

        deleteForm.action = button.dataset.url;

        modal.classList.add("show");

    });

});

document.getElementById("cancelDelete").addEventListener("click", () => {

    modal.classList.remove("show");

});

modal.addEventListener("click", (e) => {

    if (e.target === modal) {

        modal.classList.remove("show");

    }

});




