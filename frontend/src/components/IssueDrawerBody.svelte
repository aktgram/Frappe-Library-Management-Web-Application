<script>
	import { getDrawerStore } from '@skeletonlabs/skeleton';

	const drawerStore = getDrawerStore();
	const book = $drawerStore.meta;
</script>

<main>
	<div id={book.id} class="card p-4">
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

		<form>
			<label for="memberId">Member ID:</label>
			<input id="memberId" type="text" required />

			<label for="issueDate">Issue Date:</label>
			<input id="issueDate" type="date" required />

			<button type="submit">Issue Book</button>
		</form>
	</div>
</main>
