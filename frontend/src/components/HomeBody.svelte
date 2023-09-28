<script>
	import BookCard from './BookCard.svelte';
	import { Drawer, initializeStores, getDrawerStore } from '@skeletonlabs/skeleton';

	import { books } from './books';
	import IssueDrawerBody from './IssueDrawerBody.svelte';
	import ReturnDrawerBody from './ReturnDrawerBody.svelte';

	initializeStores();
	const drawerStore = getDrawerStore();

	function openIssueDrawer(book) {
		const drawerSettings = {
			id: 'issue',
			position: 'right',
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
	<div class="flex mb-5 items-center justify-between">
		<h3 class="h3">Some Available Books</h3>
		<button
			type="button"
			class="btn rounded-full variant-filled-secondary"
			on:click={openReturnDrawer}>Return Book</button
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
