<script>
	import { PUBLIC_API_URL } from '$env/static/public';
	import { getModalStore } from '@skeletonlabs/skeleton';
	import { modalAlert } from '../../functions/showAlert';

	const modalStore = getModalStore();

	let title, authors, isbn, publisher, number_of_books;
	let importing = false;
	async function startImport() {
		importing = true;
		try {
			let response = await fetch(PUBLIC_API_URL + '/books/import', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					title: title,
					authors: authors,
					isbn: isbn,
					publisher: publisher,
					number_of_books: number_of_books
				})
			});
			if (response.status == 201) {
				const books = await response.json();
				if (books.no_imported_books <= 0) {
					modalAlert(modalStore, `No new books available for specified query`);
				} else {
					modalAlert(modalStore, `successfully imported ${books.no_imported_books} books`);
				}
			} else {
				modalAlert(modalStore, `server error: ${response.status}`);
			}
		} catch (error) {
			console.log(error.message);
			modalAlert(modalStore, 'import error');
		}
		importing = false;
	}
</script>

<main>
	<div class="container mx-auto p-6">
		<h2 class="text-3xl font-semibold">Import Books from Frappe API</h2>
		<div class="flex justify-center">
			<form on:submit={startImport} class="mt-10 max-w-lg w-full">
				<div class="card p-10 rounded-lg">
					<div class="flex justify-center">
						<h4 class="h4 mb-5">Please Fill one or more Fields</h4>
					</div>
					<label class="title">
						<span>Title</span>
						<input
							bind:value={title}
							class="input rounded-full py-1 px-3 mt-1 mb-5"
							type="text"
							placeholder="Enter book title..."
						/>
					</label>
					<label class="authors">
						<span>Authors</span>
						<input
							bind:value={authors}
							class="input rounded-full py-1 px-3 mt-1 mb-5"
							type="text"
							placeholder="Enter authors..."
						/>
					</label>
					<label class="isbn">
						<span>ISBN</span>
						<input
							bind:value={isbn}
							class="input rounded-full py-1 px-3 mt-1 mb-5"
							type="text"
							placeholder="Enter ISBN..."
						/>
					</label>
					<label class="publisher">
						<span>Publisher</span>
						<input
							bind:value={publisher}
							class="input rounded-full py-1 px-3 mt-1 mb-5"
							type="text"
							placeholder="Enter publisher..."
						/>
					</label>
					<label class="number_of_books">
						<span>Maximum Number of Books</span>
						<input
							bind:value={number_of_books}
							class="input rounded-full py-1 px-3 mt-1 mb-5"
							type="number"
							placeholder="Enter number of books..."
						/>
					</label>

					<div class="mt-5 mt flex justify-center">
						<button
							type="reset"
							disabled={importing}
							class="btn mx-5 variant-ghost-tertiary rounded-full"
						>
							Clear <i class="ml-2 fas fa-times" />
						</button>
						<button
							disabled={importing}
							type="submit"
							class="btn mx-5 variant-filled-secondary rounded-full"
						>
							{importing ? 'Importing...' : 'Start Import'} <i class="ml-2 fas fa-file-import" />
						</button>
					</div>
				</div>
			</form>
		</div>
	</div>
</main>

<style>
	span {
		font-size: large;
	}
</style>
