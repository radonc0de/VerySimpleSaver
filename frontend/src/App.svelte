
<script lang="ts">
	import Table from './lib/table.svelte';
	import Modal from './lib/modal.svelte'
	import Menu from './lib/menu.svelte';
	import Charts from './lib/charts.svelte';
	import { onMount } from 'svelte';
	import { transactions, methods, categories, getTransactions, getMethods, getCategories} from './lib/store';
	let currMenu = 0;

	onMount(async() => {
		getTransactions();
		getMethods();
		getCategories();
	})

</script>
	<div class={`modal ${currMenu != 0 ? 'is-active' : ''}`}>
		<Modal bind:menuSelection={currMenu} />
	</div>

	<Menu bind:menuSelection={currMenu}/>
	<section class="hero is-primary is-fullheight">
		<div class="hero-body">
				<div class="tile is-ancestor">
					<div class="tile is-vertical">
						{#if $transactions.length != 0 && $categories.length != 0}
							<div class="tile">
								<Charts />
							</div>
							<div class="tile">
								<Table />
							</div>
						{/if}
					</div>
				</div>
		</div>
	  </section>



<style>

</style>