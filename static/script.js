document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const talkCards = document.querySelectorAll('.talk-card');
    const noResultsMsg = document.getElementById('no-results');

    searchInput.addEventListener('input', function (e) {
        const searchTerm = e.target.value.toLowerCase();
        let hasVisibleCards = false;

        talkCards.forEach(card => {
            const title = card.getAttribute('data-title').toLowerCase();
            const category = card.getAttribute('data-category').toLowerCase();
            const speakers = card.getAttribute('data-speakers').toLowerCase();

            if (title.includes(searchTerm) || category.includes(searchTerm) || speakers.includes(searchTerm)) {
                card.style.display = 'block';
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
    });
});
