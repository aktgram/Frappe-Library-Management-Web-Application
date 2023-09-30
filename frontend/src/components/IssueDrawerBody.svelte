<script>
	import { getDrawerStore } from '@skeletonlabs/skeleton';
	import { onMount } from 'svelte';
	import { PUBLIC_API_URL } from '$env/static/public';

	const drawerStore = getDrawerStore();
	const book = $drawerStore.meta;

	let memberId;
	let issueDate;
	let rentFee;
	let transactionId;
	let bookIssued = false;

	async function issueBook(event) {
		event.preventDefault();

		const response = await fetch(PUBLIC_API_URL + `/transactions`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				book_id: book.id,
				member_id: memberId,
				issue_date: issueDate,
				rent_fee: rentFee
			})
		});
		if (response.status == 201) {
			const json = await response.json();
			transactionId = json.id;

			// create a new paragraph element
			const p = document.createElement('p');
			p.textContent = 'Transaction Reference Number: ' + transactionId;
			p.className = 'h4 p-14';

			// append the paragraph to the form
			event.target.appendChild(p);

			bookIssued = true;
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
		issueDate = year + '-' + month + '-' + day;
	});
</script>

<main>
	<div id={book.id} class="card p-20">
		<table>
			<tr>
				<td>Title:</td>
				<td>{book.title}</td>
			</tr>
			<tr>
				<td>Author:</td>
				<td>{book.authors}</td>
			</tr>
			<tr>
				<td>Average Rating:</td>
				<td>{book.average_rating}</td>
			</tr>
			<tr>
				<td>ISBN:</td>
				<td>{book.isbn}</td>
			</tr>
			<tr>
				<td>ISBN13:</td>
				<td>{book.isbn13}</td>
			</tr>
			<tr>
				<td>Language:</td>
				<td>{book.language_code}</td>
			</tr>
			<tr>
				<td>Pages:</td>
				<td>{book.num_pages}</td>
			</tr>
			<tr>
				<td>Ratings:</td>
				<td>{book.ratings_count}</td>
			</tr>
			<tr>
				<td>Reviews:</td>
				<td>{book.text_reviews_count}</td>
			</tr>
			<tr>
				<td>Publication Date:</td>
				<td>{book.publication_date}</td>
			</tr>
			<tr>
				<td>Publisher:</td>
				<td>{book.publisher}</td>
			</tr>
			<tr>
				<td>Stock:</td>
				<td>{book.stock}</td>
			</tr>
		</table>

		<form on:submit={issueBook}>
			<label for="memberId" class="label mt-5">
				<span>Member ID:</span>
				<input
					bind:value={memberId}
					id="memberId"
					class="input mb-10 rounded-full px-3"
					type="text"
					placeholder="Enter Member ID"
					required
				/>
			</label>

			<label for="rentFee" class="label mt-10">
				<span>Rent Amount</span>
				<div class="input-group rounded-full input-group-divider grid-cols-[auto_1fr_auto]">
					<div class="input-group-shim"><i class="fas fa-rupee-sign" /></div>
					<input bind:value={rentFee} class="px-3" type="text" placeholder="Amount" />
				</div>
			</label>

			<label for="issueDate" class="label mt-10">
				<span>Issue Date:</span>
				<input
					bind:value={issueDate}
					id="issueDate"
					class="input mb-10 rounded-full px-3"
					type="date"
					required
				/>
			</label>

			<button
				disabled={bookIssued}
				type="submit"
				class="btn rounded-full variant-filled-secondary mt-10">Issue Book</button
			>
		</form>
	</div>
</main>

<style>
	.card {
		width: 700px;
		height: 100vh;
	}

	table {
		width: 100%;
	}

	td {
		padding: 5px;
	}

	form {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-top: 20px;
	}
</style>
