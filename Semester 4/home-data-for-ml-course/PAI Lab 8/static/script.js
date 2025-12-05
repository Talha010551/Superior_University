const setupEl = document.getElementById("setup");
const punchlineEl = document.getElementById("punchline");
const button = document.getElementById("new-joke");

async function fetchJoke() {
    try {
        const response = await fetch("/get_joke");
        const joke = await response.json();

        setupEl.textContent = joke.setup;
        punchlineEl.textContent = joke.punchline;
    } catch (error) {
        setupEl.textContent = "Oops! Something went wrong.";
        punchlineEl.textContent = "Try again later.";
    }
}

button.addEventListener("click", fetchJoke);

// Load first joke on page load
fetchJoke();
