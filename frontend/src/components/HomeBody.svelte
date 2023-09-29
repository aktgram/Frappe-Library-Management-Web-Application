<script>
	import { Drawer, initializeStores, getDrawerStore } from '@skeletonlabs/skeleton';

	import IssueDrawerBody from './IssueDrawerBody.svelte';
	import ReturnDrawerBody from './ReturnDrawerBody.svelte';
	import SuggestedBooksBody from './SuggestedBooksBody.svelte';
	import SearchBody from './SearchBody.svelte';

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

	let searchInput = '';
	let searchToggle = false;
	function onClearSearch() {
		if (searchInput === '') {
			// Add any additional logic here
			// refresh books from search result to home feed
			searchToggle = false;
		} else {
			searchToggle = true;
		}
	}
</script>

<main>
	<div class="flex my-5 items-center justify-between">
		<!-- Search Box -->
		<div
			class="input-group input-group-divider rounded-full grid-cols-[auto_1fr_auto] w-1/3 h-full"
		>
			<div class="input-group-shim"><i class="fas fa-search" /></div>
			<!-- Font Awesome search icon -->
			<input
				id="searchInput"
				type="search"
				class="px-3 py-2"
				placeholder="Search for Books"
				bind:value={searchInput}
				on:input={onClearSearch}
			/>
			<button class="variant-filled-secondary">Submit</button>
		</div>

		<!-- Spacer -->
		<div class="flex-grow" />

		<!-- Return Book Button -->
		<button
			type="button"
			class="btn rounded-full variant-filled-secondary ml-5 h-full"
			on:click={openReturnDrawer}>Return Book</button
		>
	</div>

	{#if searchToggle === true}
		<SearchBody {openIssueDrawer} />
	{:else}
		<SuggestedBooksBody {openIssueDrawer} />
	{/if}

	<Drawer width="200">
		{#if $drawerStore.id === 'issue'}
			<IssueDrawerBody />
		{:else if $drawerStore.id === 'return'}
			<ReturnDrawerBody />
		{/if}
	</Drawer>
</main>
