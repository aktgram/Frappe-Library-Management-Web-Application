<script>
	import { onMount } from 'svelte';
	import BookCard from './BookCard.svelte';
	import { PUBLIC_API_URL } from '$env/static/public';

	export let openIssueDrawer;

	let books = [];
	let pageNumber = 1;

	async function fetchBooks() {
		const response = await fetch(PUBLIC_API_URL + '/books?page=' + pageNumber);
		if (response.ok) {
			const json = await response.json();
			books = json.books;
		} else {
			console.error('HTTP-Error: ' + response.status);
			alert('Server Down!!');
		}
	}

	function nextPage() {
		books = [];
		pageNumber++;
		fetchBooks();
	}

	function previousPage() {
		if (pageNumber > 1) {
			books = [];
			pageNumber--;
			fetchBooks();
		}
	}

	onMount(() => {
		fetchBooks();
	});
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
		{#if books.length === 0}
			{#each { length: 10 } as _, __}
				<BookCard placeholder={true} />
			{/each}
		{:else}
			{#each books as book (book.id)}
				<BookCard {book} openDrawer={openIssueDrawer} placeholder={false} />
			{/each}
		{/if}
	</div>
</main>
