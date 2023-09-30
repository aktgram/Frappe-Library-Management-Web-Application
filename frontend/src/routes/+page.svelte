<script>
	import { Drawer, initializeStores, getDrawerStore } from '@skeletonlabs/skeleton';

	import IssueDrawerBody from '../components/IssueDrawerBody.svelte';
	import ReturnDrawerBody from '../components/ReturnDrawerBody.svelte';
	import SuggestedBooksBody from '../components/SuggestedBooksBody.svelte';
	import SearchBody from '../components/SearchBody.svelte';

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

	let searchTitle = '';
	let searchAuthor = '';
	let searchToggle = false;
	function onClearSearch() {
		if (searchTitle == '' && searchAuthor === '') {
			// refresh books from search result to home feed
			searchToggle = false;
		} else {
			searchToggle = true;
		}
	}
</script>

<main>
	<div class="container h-full mx-auto flex justify-center items-center">
		<div class="space-y-5 m-5">
			<div class="flex my-5 items-center justify-between">
				<!-- Search by Title -->
				<div
					class="input-group input-group-divider rounded-full grid-cols-[auto_1fr_auto] w-1/4 h-full"
				>
					<div class="input-group-shim"><i class="fas fa-search" /></div>
					<!-- Font Awesome search icon -->
					<input
						id="searchInput"
						type="search"
						class="px-3 py-2"
						placeholder="Search by Book Title..."
						bind:value={searchTitle}
						on:input={onClearSearch}
					/>
				</div>

				<!-- Spacer -->
				<div class="flex-grow" />

				<!-- Search by Authors -->
				<div
					class="input-group input-group-divider rounded-full grid-cols-[auto_1fr_auto] w-1/4 h-full"
				>
					<div class="input-group-shim"><i class="fas fa-search" /></div>
					<!-- Font Awesome search icon -->
					<input
						id="searchInput"
						type="search"
						class="px-3 py-2"
						placeholder="Search by Book Authors..."
						bind:value={searchAuthor}
						on:input={onClearSearch}
					/>
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
				<SearchBody {searchTitle} {searchAuthor} {openIssueDrawer} />
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
		</div>
	</div>
</main>
