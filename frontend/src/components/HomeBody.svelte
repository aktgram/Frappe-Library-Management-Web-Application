<script>
	import BookCard from './BookCard.svelte';
	import { Drawer, initializeStores, getDrawerStore } from '@skeletonlabs/skeleton';

	import { books } from './books';
	import IssueDrawerBody from './IssueDrawerBody.svelte';
	import ReturnDrawerBody from './ReturnDrawerBody.svelte';

	initializeStores();
	const drawerStore = getDrawerStore();

	/** @type {"right" | "left" | "top" | "bottom" | undefined} */
	const issueDrawerPosition = 'right';

	/**
	 * @param {{ id: number, title: any; authors: any; isbn: any; isbn13: any; language_code: any; num_pages: any; ratings_count: any; text_reviews_count: any; publication_date: any; publisher: any; stock: any; }} book
	 */
	function openIssueDrawer(book) {
		const drawerSettings = {
			id: 'issue',
			position: issueDrawerPosition,
			meta: book
		};
		drawerStore.open(drawerSettings);
	}

	function openReturnDrawer() {
		const drawerSettings = {
			id: 'return',
			meta: { foo: 'bar', fizz: 'buzz', age: 40 }
		};
		drawerStore.open(drawerSettings);
	}
</script>

<main>
	<div class="grid grid-cols-2 mb-5">
		<h3 class="h3">Some Available Books</h3>
		<button type="button" class="btn variant-filled" on:click={openReturnDrawer}>Return Book</button
		>
	</div>
	<div
		class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 xxl:grid-cols-6 gap-20 auto-cols-min"
	>
		{#each books as book (book.id)}
			<BookCard {book} openDrawer={openIssueDrawer} />
		{/each}
	</div>

	<Drawer width="200">
		{#if $drawerStore.id === 'issue'}
			<IssueDrawerBody />
		{:else if $drawerStore.id === 'return'}
			<ReturnDrawerBody />
		{/if}
	</Drawer>
</main>
