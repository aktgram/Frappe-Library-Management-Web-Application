<script>
	import { PUBLIC_API_URL } from '$env/static/public';
	import { onMount } from 'svelte';

	let returnDate;
	let transactionId;
	let issuedDetails;
	let showDetails = false;
	let bookReturned = false;

	async function fetchIssuedDetails() {
		// Fetch the issued details based on the transaction ID
		const response = await fetch(PUBLIC_API_URL + `/transactions/${transactionId}`);
		if (response.ok) {
			const json = await response.json();
			issuedDetails = json.transaction;
			showDetails = true;
		} else {
			console.error('HTTP-Error: ' + response.status);
			alert('Server Down!!');
		}
	}

	async function returnBook() {
		// Handle the book return
		const response = await fetch(PUBLIC_API_URL + `/transactions/${transactionId}/return`, {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				return_date: returnDate
			})
		});
		if (response.ok) {
			// const json = await response.json();
			// issuedDetails = json.transaction;
			bookReturned = true;
		} else {
			console.error('HTTP-Error: ' + response.status);
			alert('Server Down!!');
		}
	}

	onMount(() => {
		// set issue date to default to today
		let today = new Date();
		let day = String(today.getDate()).padStart(2, '0');
		let month = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
		let year = today.getFullYear();
		returnDate = year + '-' + month + '-' + day;
	});
</script>

<main>
	<div id="return-book-card" class="card p-20">
		<form on:submit={fetchIssuedDetails}>
			<label for="transactionId" class="label">
				<span>Transaction ID:</span>
				<input
					id="transactionId"
					class="input rounded-full px-3"
					type="text"
					placeholder="Transaction Reference Number"
					bind:value={transactionId}
					required
				/>
			</label>

			<button type="submit" class="btn rounded-full variant-filled-secondary"
				>Fetch Issued Details</button
			>
		</form>

		{#if showDetails}
			<table>
				<tr>
					<td>Book ID:</td>
					<td>{issuedDetails.book_id}</td>
				</tr>
				<tr>
					<td>Book Title:</td>
					<td>{issuedDetails.book_title}</td>
				</tr>
				<tr>
					<td>Member ID:</td>
					<td>{issuedDetails.member_id}</td>
				</tr>
				<tr>
					<td>Member Name:</td>
					<td>{issuedDetails.member_name}</td>
				</tr>
				<tr>
					<td>Issue Date:</td>
					<td>{new Date(issuedDetails.issue_date).toLocaleDateString()}</td>
				</tr>
				<tr>
					<td>Rent Fee:</td>
					<td>{issuedDetails.rent_fee}</td>
				</tr>
			</table>

			<form on:submit={returnBook}>
				<label for="returnDate" class="label mt-10">
					<span>Return Date:</span>
					<input
						bind:value={returnDate}
						id="returnDate"
						class="input mb-10 rounded-full px-3"
						type="date"
						required
					/>
				</label>

				<button
					type="submit"
					class="btn rounded-full variant-filled-secondary"
					disabled={bookReturned}
				>
					{bookReturned ? 'Returned Book Successfully' : 'Return Book'}
				</button>
			</form>
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
