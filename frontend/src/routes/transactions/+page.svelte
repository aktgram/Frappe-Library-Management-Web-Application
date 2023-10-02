<script>
	import { PUBLIC_API_URL } from '$env/static/public';
	import { onMount } from 'svelte';

	let transactions = [];
	let pageNumber = 1;

	async function loadTransactions() {
		const response = await fetch(PUBLIC_API_URL + `/transactions?page=${pageNumber}`);
		if (response.ok) {
			const json = await response.json();
			transactions = json.transactions;
		} else {
			alert('Server down');
		}
	}

	function nextPage() {
		// only if page end not reached
		if (transactions.length == 15) {
			pageNumber++;
			loadTransactions();
		}
	}

	function previousPage() {
		// only if page beginning not reached
		if (pageNumber > 1) {
			pageNumber--;
			loadTransactions();
		}
	}
	onMount(() => {
		loadTransactions();
	});
</script>

<main>
	<div class="container mx-auto p-6">
		<div class="flex justify-between items-center mb-6">
			<h1 class="text-3xl font-semibold">Book Rental Transactions</h1>
		</div>
		<table class="table w-full">
			<thead>
				<tr>
					<th>Transaction ID</th>
					<th>Book Title</th>
					<th>Member Name</th>
					<th>Issue Date</th>
					<th>Return Date</th>
					<th>Rent Fee</th>
					<th>
						<div class="flex items-center">
							<button on:click={previousPage} class="btn w-1 rounded-full variant-ghost-tertiary">
								<i class="fas fa-chevron-left" />
							</button>
							<span class="mx-4 flex justify-center items-center w-6">{pageNumber}</span>
							<button on:click={nextPage} class="btn w-1 rounded-full variant-ghost-tertiary">
								<i class="fas fa-chevron-right" />
							</button>
						</div>
					</th>
				</tr>
			</thead>
			<tbody>
				{#each transactions as transaction (transaction.id)}
					<tr>
						<td>{transaction.id}</td>
						<td>{transaction.book_title}</td>
						<td>{transaction.member_name}</td>
						<td>{new Date(transaction.issue_date).toLocaleDateString('en-GB')}</td>
						<td
							>{transaction.return_date
								? new Date(transaction.return_date).toLocaleDateString('en-GB')
								: 'Book Not Returned'}</td
						>

						<td>₹{transaction.rent_fee}</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</main>

<style>
	tbody td {
		font-size: 100%;
	}
</style>
