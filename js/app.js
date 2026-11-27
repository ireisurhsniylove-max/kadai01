document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    form.addEventListener("submit", (event) => {

        const title = document.querySelector("[name='title']").value.trim();
        const message = document.querySelector("[name='message']").value.trim();

        if (title === "") {
            alert("タイトルを入力してください");
            event.preventDefault();
            return;
        }

        if (message === "") {
            alert("内容を入力してください");
            event.preventDefault();
            return;
        }

        alert("投稿しました！");
    });

});