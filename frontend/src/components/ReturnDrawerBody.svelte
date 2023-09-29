<script>
	let transactionId = '';
	let issuedDetails = {
		book_id: 8,
		member_id: 3,
		issue_date: '2023-09-12',
		rent_fee: 100.0
	};
	let showDetails = false;
	let bookReturned = false;

	function fetchIssuedDetails() {
		// Fetch the issued details based on the transaction ID
		showDetails = true;
	}

	function returnBook() {
		// Handle the book return
		bookReturned = true;
	}
</script>

<main>
	<div id="return-book-card" class="card p-20">
		<form>
			<label for="transactionId" class="label">
				<span>Transaction ID:</span>
				<input
					id="transactionId"
					class="input"
					type="text"
					placeholder="Transaction Reference Number"
					bind:value={transactionId}
					required
				/>
			</label>

			<button
				type="button"
				on:click={fetchIssuedDetails}
				class="btn rounded-full variant-filled-secondary">Fetch Issued Details</button
			>
		</form>

		{#if showDetails}
			<table>
				<tr>
					<td>Book ID:</td>
					<td>{issuedDetails.book_id}</td>
				</tr>
				<tr>
					<td>Member ID:</td>
					<td>{issuedDetails.member_id}</td>
				</tr>
				<tr>
					<td>Issue Date:</td>
					<td>{issuedDetails.issue_date}</td>
				</tr>
				<tr>
					<td>Rent Fee:</td>
					<td>{issuedDetails.rent_fee}</td>
				</tr>
			</table>

			<button
				type="button"
				on:click={returnBook}
				class="btn rounded-full variant-filled-secondary"
				disabled={bookReturned}
			>
				{bookReturned ? 'Returned Book Successfully' : 'Return Book'}
			</button>
		{/if}
	</div>
</main>

<style>
	#return-book-card {
		width: 700px;
		height: 100vh;
	}

	form {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		margin-bottom: 20px;
	}

	#transactionId {
		margin-bottom: 20px;
	}

	button {
		margin-top: 20px;
	}

	td {
		padding: 5px;
	}
</style>
