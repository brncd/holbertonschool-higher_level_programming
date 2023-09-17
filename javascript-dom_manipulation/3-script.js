const toggleHeader = document.querySelector("header");
toggleHeader.addEventListener("click", () => {
    toggleHeader.classList.toggle("red");
    toggleHeader.classList.toggle("green");
});
