<script>
	import { Modal } from '@skeletonlabs/skeleton';
	import { getModalStore } from '@skeletonlabs/skeleton';
	import { PUBLIC_API_URL } from '$env/static/public';
	import { onMount } from 'svelte';
	import AddMemberModal from '../../components/members/MemberModal.svelte';

	const modalStore = getModalStore();

	let members = [];
	let pageNumber = 1;

	async function loadMembers() {
		const response = await fetch(PUBLIC_API_URL + `/members?page=${pageNumber}`);
		if (response.ok) {
			const json = await response.json();
			members = json.members;
		} else {
			alert('Server down');
		}
	}

	function addMember(name, debt) {
		return Promise.race([
			fetch(PUBLIC_API_URL + `/members`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					name: name,
					outstanding_debt: debt
				})
			}),
			new Promise((_, reject) => setTimeout(() => reject(new Error('Request timed out')), 8000))
		]);
	}

	function deleteMember(id) {
		Promise.race([
			fetch(PUBLIC_API_URL + `/members/${id}`, {
				method: 'DELETE'
			}),
			new Promise((_, reject) => setTimeout(() => reject(new Error('Request timed out')), 8000))
		])
			.then((res) => {
				if (res.status === 204) {
					alert(`Member ${id} Deleted`);
					members = members.filter((member) => member.id !== id);
				} else {
					alert(`Member Deletion failed`);
				}
			})
			.catch(() => {
				alert(error.message);
			});
	}

	function updateMember(id, name, debt) {
		// Update member logic here
		return Promise.race([
			fetch(PUBLIC_API_URL + `/members/${id}`, {
				method: 'PUT',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					name: name,
					outstanding_debt: debt
				})
			}),
			new Promise((_, reject) => setTimeout(() => reject(new Error('Request timed out')), 8000))
		]);
	}

	function nextPage() {
		// only if page end not reached
		if (members.length == 10) {
			pageNumber++;
			loadMembers();
		}
	}

	function previousPage() {
		// only if page beginning not reached
		if (pageNumber > 1) {
			pageNumber--;
			loadMembers();
		}
	}

	// Modal configs
	function addMemberModal() {
		const modal = {
			type: 'component',
			component: 'addModalComponent'
		};
		modalStore.trigger(modal);
	}

	function editMemberModal(member_id, member_name, member_debt) {
		if (!member_id || !member_debt || !member_name || member_id == 0) {
			alert('edit error');
		} else {
			const modal = {
				type: 'component',
				component: 'editModalComponent',
				title: `Edit Member ${member_id} Details`,
				member_name: member_name,
				member_id: member_id,
				member_debt: member_debt
			};
			modalStore.trigger(modal);
		}
	}

	const modalComponentRegistry = {
		addModalComponent: {
			ref: AddMemberModal,
			props: { submitForm: addMember },
			slot: '<p>Error loading Modal</p>'
		},
		editModalComponent: {
			ref: AddMemberModal,
			props: { submitForm: updateMember },
			slot: '<p>Error loading Modal</p>'
		}
	};

	onMount(() => {
		loadMembers();
	});
</script>

<main>
	<Modal components={modalComponentRegistry} />
	<div class="container mx-auto p-6">
		<div class="flex justify-between items-center mb-6">
			<h1 class="text-3xl font-semibold">Members</h1>
			<button on:click={addMemberModal} class="btn rounded-full variant-filled-secondary">
				<i class="fas fa-plus mr-1" /> Add Member
			</button>
		</div>
		<table class="table w-full">
			<thead>
				<tr>
					<th>Member ID</th>
					<th>Member Name</th>
					<th>Outstanding Debt</th>
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
				{#each members as member (member.id)}
					<tr>
						<td>{member.id}</td>
						<td>
							{member.name}
						</td>
						<td>
							₹{member.outstanding_debt}
						</td>
						<td>
							<button
								class="btn btn-square btn-primary text-lg"
								on:click={() => editMemberModal(member.id, member.name, member.outstanding_debt)}
							>
								<i class="fas fa-edit" />
							</button>
							<button
								class="btn btn-square btn-error text-lg"
								on:click={() => deleteMember(member.id)}
							>
								<i class="fas fa-trash" />
							</button>
						</td>
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
