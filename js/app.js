document.addEventListener("DOMContentLoaded", () => {
    const modal = document.querySelector("#postModal");
    const openModalBtn = document.querySelector("#openModalBtn");
    const closeModalBtn = document.querySelector("#closeModalBtn");
    const form = document.querySelector("#postForm");

    openModalBtn.addEventListener("click", () => {
        modal.classList.add("open");
    });

    closeModalBtn.addEventListener("click", () => {
        modal.classList.remove("open");
    });

    modal.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.classList.remove("open");
        }
    });

    document.querySelectorAll("[data-filter]").forEach((button) => {
        button.addEventListener("click", () => {
            const filter = button.dataset.filter;

            document.querySelectorAll("#postList article").forEach((article) => {
                article.hidden = filter !== "all" && article.dataset.category !== filter;
            });
        });
    });

    form.addEventListener("submit", (event) => {
        const title = form.querySelector("[name='title']").value.trim();
        const message = form.querySelector("[name='message']").value.trim();

        if (title === "") {
            alert("タイトルを入力してください");
            event.preventDefault();
            return;
        }

        if (message === "") {
            alert("内容を入力してください");
            event.preventDefault();
        }
    });
});