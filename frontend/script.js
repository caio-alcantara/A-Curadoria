const genreMapping = {
    28: 'Action',
    12: 'Adventure',
    16: 'Animation',
    35: 'Comedy',
    80: 'Crime',
    99: 'Documentary',
    18: 'Drama',
    53: 'Suspense',
    878: 'Sci-Fi',
    27: 'Terror',
    14: 'Fantasy'
};


async function searchMovie() {
    const movieName = document.getElementById('movieName').value.trim();
    const movieDetailsDiv = document.getElementById('movieDetails');

    if (!movieName) {
        movieDetailsDiv.innerHTML = '<p class="text-red-500">Please, type the movie name:</p>';
        return;
    }

    movieDetailsDiv.innerHTML = '<p class="text-gray-500">Loading...</p>';

    try {
        const response = await fetch(`http://localhost:5000/api/search?query=${movieName}`);
        const data = await response.json();

        if (response.ok && data.results && data.results.length > 0) {
            const movie = data.results[0];
            const genres = movie.genre_ids.map(id => genreMapping[id] || 'Unknown').join(', ');
            const posterUrl = movie.poster_path ? `https://image.tmdb.org/t/p/w500${movie.poster_path}` : 'https://via.placeholder.com/500x750?text=No+Image';

            movieDetailsDiv.innerHTML = `
                <h2 class="text-xl font-semibold mb-4">Movie Information</h2>
                <div class="flex flex-col items-center">
                    <img src="${posterUrl}" alt="${movie.title} Poster" class="rounded-lg shadow-lg w-64 mb-4">
                    <p><strong>Name:</strong> ${movie.title}</p>
                    <p><strong>Genre:</strong> ${genres}</p>
                    <p><strong>Year:</strong> ${movie.release_date.split('-')[0]}</p>
                    <p><strong>Description:</strong> ${movie.overview}</p>
                </div>
            `;
        } else {
            movieDetailsDiv.innerHTML = '<p class="text-red-500">No movies found.</p>';
        }
    } catch (error) {
        movieDetailsDiv.innerHTML = '<p class="text-red-500">Error when connecting to server.</p>';
    }
}
