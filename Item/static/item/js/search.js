
document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("item-search");
    const suggestionsBox = document.getElementById("search-suggestions");
    const itemsGrid = document.getElementById("items-grid");

    if (!searchInput || !suggestionsBox || !itemsGrid) {
        console.error("Search elements were not found.");
        return;
    }

    const itemCards = itemsGrid.querySelectorAll(".item-card");

    // Search when the user types
    searchInput.addEventListener("input", function () {
        const query = searchInput.value.trim().toLowerCase();

        let visibleItems = 0;
        suggestionsBox.innerHTML = "";
        suggestionsBox.style.display = "none";

        itemCards.forEach(function (card) {
            const titleElement = card.querySelector("h2");
            const cardText = card.textContent.toLowerCase();
            const title = titleElement
                ? titleElement.textContent.trim()
                : "";

            // Match item name, category, description, or location
            if (cardText.includes(query)) {
                card.style.display = "";
                visibleItems++;
            } else {
                card.style.display = "none";
            }

            // Suggest matching item titles
            if (query !== "" && title.toLowerCase().includes(query)) {
                const suggestion = document.createElement("div");
                suggestion.className = "suggestion-item";
                suggestion.textContent = title;

                suggestion.addEventListener("click", function () {
                    searchInput.value = title;
                    suggestionsBox.style.display = "none";

                    itemCards.forEach(function (item) {
                        const itemTitle = item.querySelector("h2");

                        item.style.display =
                            itemTitle &&
                            itemTitle.textContent.trim() === title
                                ? ""
                                : "none";
                    });
                });

                suggestionsBox.appendChild(suggestion);
            }
        });

        // Show suggestions only when matching titles exist
        if (query !== "" && suggestionsBox.children.length > 0) {
            suggestionsBox.style.display = "block";
        }
    });

    // Hide suggestions when clicking outside the search area
    document.addEventListener("click", function (event) {
        if (
            !searchInput.contains(event.target) &&
            !suggestionsBox.contains(event.target)
        ) {
            suggestionsBox.style.display = "none";
        }
    });

    // Press Escape to close suggestions
    searchInput.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            suggestionsBox.style.display = "none";
        }
    });
});
