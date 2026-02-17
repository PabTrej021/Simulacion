document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');
    const talkCards = document.querySelectorAll('.talk-card');
    const noResultsMsg = document.getElementById('no-results');

    function filterTalks() {
        const searchTerm = searchInput.value.toLowerCase().trim();
        let hasVisibleCards = false;

        talkCards.forEach(card => {
            const title = card.getAttribute('data-title').toLowerCase();
            const category = card.getAttribute('data-category').toLowerCase();
            const speakers = card.getAttribute('data-speakers').toLowerCase();

            // Check if any field contains the search term
            const matches = title.includes(searchTerm) ||
                category.includes(searchTerm) ||
                speakers.includes(searchTerm);

            if (matches) {
                card.style.display = 'flex'; // Restore flex display
                hasVisibleCards = true;
            } else {
                card.style.display = 'none';
            }
        });

        if (hasVisibleCards) {
            noResultsMsg.style.display = 'none';
        } else {
            noResultsMsg.style.display = 'block';
        }
    }

    // Real-time filtering
    searchInput.addEventListener('input', filterTalks);

    // Button click (optional, as input handles it, but good for UX)
    searchBtn.addEventListener('click', filterTalks);
});
