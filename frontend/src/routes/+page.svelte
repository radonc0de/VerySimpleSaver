<script lang="ts">
	import Table from './table.svelte';
	import Editor from './editor.svelte'
	import Menu from './menu.svelte';
	import Charts from './charts.svelte';
	import { onMount } from 'svelte';
	import { transactions, methods, categories, getTransactions, getMethods, getCategories} from './store';
	let currMenu = 0;

	onMount(async() => {
		getTransactions();
		getMethods();
		getCategories();
	})

</script>
<div class="container">
	<div class={`modal ${currMenu != 0 ? 'is-active' : ''}`}>
		<Editor bind:menuSelection={currMenu} />
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

</div>


<style>

</style>