<script>
	import BookCard from './BookCard.svelte';

	export let openIssueDrawer;
	import { books } from './books';

	let pageNumber = 1;

	function nextPage() {
		pageNumber++;
		// Add logic to fetch the next page of books
	}

	function previousPage() {
		if (pageNumber > 1) {
			pageNumber--;
			// Add logic to fetch the previous page of books
		}
	}
</script>

<main>
	<div class="flex justify-between items-center my-8">
		<h3 class="h3">Some Available Books</h3>
		<div class="flex items-center">
			<button on:click={previousPage} class="btn w-1 rounded-full variant-filled-secondary">
				<i class="fas fa-chevron-left" />
			</button>
			<span class="mx-4 flex justify-center items-center w-6">{pageNumber}</span>
			<button on:click={nextPage} class="btn w-1 rounded-full variant-filled-secondary">
				<i class="fas fa-chevron-right" />
			</button>
		</div>
	</div>
	<div
		class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 xxl:grid-cols-6 gap-20 auto-cols-min"
	>
		{#each books as book (book.id)}
			<BookCard {book} openDrawer={openIssueDrawer} />
		{/each}
	</div>
</main>
