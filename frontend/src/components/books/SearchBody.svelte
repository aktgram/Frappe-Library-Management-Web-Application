<script>
	import BookCard from './BookCard.svelte';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { modalAlert } from '../../functions/showAlert';
	import { getModalStore } from '@skeletonlabs/skeleton';

	const modalStore = getModalStore();

	export let openIssueDrawer;
	export let searchTitle;
	export let searchAuthor;

	// to optimise instant search to have lesser api calls
	let debounceTimeout;
	let controller = new AbortController();

	let books = [];
	let pageNumber = 1;
	let searching = true;

	async function searchBooks() {
		searching = true;
		// remove unnecessary invocation when search field emptied
		if (searchAuthor != '' || searchTitle != '') {
			// Cancel any previous requests and create new controller
			controller.abort();
			controller = new AbortController();

			clearTimeout(debounceTimeout);

			debounceTimeout = setTimeout(async () => {
				const response = await fetch(
					PUBLIC_API_URL +
						`/books/search?title=${searchTitle}&authors=${searchAuthor}&page=${pageNumber}`
				);
				if (response.ok) {
					const json = await response.json();
					books = json.books;
					if (books.length <= 0) {
						searching = false;
					}
				} else {
					console.error('HTTP-Error: ' + response.status);
					modalAlert(modalStore, 'Server Down!!');
					if (books.length <= 0) {
						searching = false;
					}
				}
			}, 300);
		}
	}

	function nextPage() {
		// only if page end not reached
		if (books.length == 10) {
			books = [];
			pageNumber++;
			searchBooks();
		}
	}

	function previousPage() {
		// only if page beginning not reached
		if (pageNumber > 1) {
			books = [];
			pageNumber--;
			searchBooks();
		}
	}

	// update search on value change, and update page number on new search
	$: searchTitle, searchAuthor, ((pageNumber = 1), (books = [])), searchBooks();
</script>

<main>
	<div class="flex justify-between items-center my-8">
		<h3 class="h3 my-8">
			Search Results for {searchTitle}
			{searchAuthor ? 'by ' + searchAuthor : ''}
		</h3>
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
		{#if books.length === 0 && searching === true}
			{#each { length: 10 } as _, __}
				<BookCard placeholder={true} />
			{/each}
		{:else if books.length === 0 && searching === false}
			<div class="container flex w-100">
				<h3 class="h3">No Search Results</h3>
			</div>
		{:else}
			{#each books as book (book.id)}
				<BookCard {book} openDrawer={openIssueDrawer} placeholder={false} />
			{/each}
		{/if}
	</div>
</main>
