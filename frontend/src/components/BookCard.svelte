<script>
	/**
	 * @type {{ id: number, title: any; authors: any; isbn: any; isbn13: any; language_code: any; num_pages: any; ratings_count: any; text_reviews_count: any; publication_date: any; publisher: any; stock: any; }}
	 */
	export let book;

	/**
	 * @type {any}
	 */
	export let openDrawer;
</script>

<div class="card p-4 bookcard">
	<h2>{book.title}</h2>
	<p>by {book.authors}</p>
	<p>ISBN: {book.isbn}</p>
	<p>ISBN13: {book.isbn13}</p>
	<p>Language: {book.language_code}</p>
	<p>Pages: {book.num_pages}</p>
	<p>Ratings: {book.ratings_count}</p>
	<p>Reviews: {book.text_reviews_count}</p>
	<p>Publication Date: {book.publication_date}</p>
	<p>Publisher: {book.publisher}</p>
	<p>Stock: {book.stock}</p>
	<div>
		<button type="button" class="btn variant-filled" on:click={openDrawer(book)}>Issue</button>
	</div>
</div>

<style>
	.bookcard {
		width: 220px;
		height: 380px;
	}
</style>
