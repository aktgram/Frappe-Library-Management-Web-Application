<script>
	import { AppBar, LightSwitch, initializeStores } from '@skeletonlabs/skeleton';
	import '../app.postcss';

	initializeStores();
</script>

<!-- Fontawesome icons -->
<link
	rel="stylesheet"
	href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
/>

<main>
	<AppBar slotDefault="place-self-center" slotTrail="place-content-end">
		<svelte:fragment slot="lead">
			<h2 class="h2">Frappe Library Management System</h2>
		</svelte:fragment>
		<svelte:fragment slot="trail">
			<a href="/" class="btn rounded-full variant-filled-secondary"> Books </a>
			<a href="/members" class="btn rounded-full variant-filled-secondary"> Members </a>
			<LightSwitch />
		</svelte:fragment>
	</AppBar>
</main>

<slot />
