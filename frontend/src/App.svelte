
<script lang="ts">
	import Table from './lib/table.svelte';
	import Modal from './lib/modal.svelte'
	import Menu from './lib/menu.svelte';
	import Charts from './lib/charts.svelte';
	import { onMount } from 'svelte';
	import { transactions, methods, categories, getTransactions, getMethods, getCategories, menuSelection} from './lib/store';

	onMount(async() => {
		getTransactions();
		getMethods();
		getCategories();
	})

</script>
	<div class={`modal ${$menuSelection != 0 ? 'is-active' : ''}`}>
		<Modal />
	</div>

	<Menu />
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