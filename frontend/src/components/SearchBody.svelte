<script>
	import BookCard from './BookCard.svelte';

	export let openIssueDrawer;
	import { books } from './books';
</script>

<main>
	<h3 class="h3 my-8">Search Results</h3>
	<div
		class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 xxl:grid-cols-6 gap-20 auto-cols-min"
	>
		{#each books as book (book.id)}
			<BookCard {book} openDrawer={openIssueDrawer} />
		{/each}
	</div>
</main>
