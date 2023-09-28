<script>
	export let book;

	export let openDrawer;
</script>

<!-- For Ratings star icon -->
<link
	rel="stylesheet"
	href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
/>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-interactive-supports-focus -->
<div
	class="card p-4 bookcard"
	style="background: linear-gradient(135deg, #f5deb3 0%, #deb887 100%); color: black; display: flex; flex-direction: column; justify-content: center; align-items: center; position: relative; box-shadow: 0px 10px 15px rgba(0,0,0,0.1); transition: all 0.3s ease-in-out; overflow: hidden;"
	role="button"
	on:click={openDrawer(book)}
>
	<h1
		style="font-size: 2em; margin-bottom: 20px; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; text-overflow: ellipsis; text-align: center; line-height: 1.2;"
		title={book.title}
	>
		{book.title}
	</h1>
	<h3
		style="font-size: 1em; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; text-overflow: ellipsis; text-align: center; line-height: 1.2;"
		title={book.authors}
	>
		{book.authors}
	</h3>
	<p style="position: absolute; top: 10px; right: 10px; font-size: small;">
		{book.num_pages} <i class="fas fa-book-open" />
	</p>
	<p style="position: absolute; top: 10px; text-align: center; width: 100%; font-size: small;">
		{book.language_code}
	</p>
	<p style="position: absolute; top: 10px; left: 10px; font-size: small;">
		<i class="fas fa-star" />
		{book.average_rating}
	</p>
	<p
		style="position: absolute; bottom: 10px; text-align: center; width: 100%; font-size: x-small; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; cursor: pointer;"
		title={book.publisher}
	>
		{book.publisher}
	</p>
</div>

<style>
	.bookcard {
		width: 220px;
		height: 380px;
	}
</style>
