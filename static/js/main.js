let alertButton = document.querySelector('[close]');
let alert = document.getElementById(['alert']);


if (alertButton) {
    alertButton.addEventListener('click', () => {
    alert.classList.toggle('hidden')
})
}