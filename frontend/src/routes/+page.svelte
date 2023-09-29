<script>
	import { LightSwitch } from '@skeletonlabs/skeleton';
	import { AppBar } from '@skeletonlabs/skeleton';
	import HomeBody from '../components/HomeBody.svelte';
</script>

<main>
	<AppBar slotDefault="place-self-center" slotTrail="place-content-end">
		<svelte:fragment slot="lead">
			<h2 class="h2">Frappe Library Management System</h2>
		</svelte:fragment>
		<svelte:fragment slot="trail">
			<button type="button" class="btn rounded-full variant-filled-secondary">Add Book</button>
			<button type="button" class="btn rounded-full variant-filled-secondary">Add Member</button>
			<LightSwitch />
		</svelte:fragment>
	</AppBar>
	<div class="container h-full mx-auto flex justify-center items-center">
		<div class="space-y-5 m-5">
			<HomeBody />
		</div>
	</div>
</main>
