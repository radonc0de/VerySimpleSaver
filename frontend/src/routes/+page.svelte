<script lang="ts">
	import Table from './table.svelte';
	import Editor from './editor.svelte'
	import Menu from './menu.svelte';
	import Charts from './charts.svelte';
	import type Transaction from '../lib/transaction';
	import type Method from '../lib/method';
	import type Category from '../lib/category';
	import { constants } from '../env';
	import { onMount } from 'svelte';
	import { transactions, methods, categories } from './store';

	let modalOpen = false;
	let currMenu = 0;

	async function fetchData(path: string, ref: (resp: any[]) => void){
		try {
			const response = await fetch(constants.API_URL + path);
			let data = await response.json();
			ref(data);
		} catch (e) {
			console.log(e);
		}
	}

	onMount(async() => {
		fetchData('/methods', (resp: Method[]) => methods.set(resp));
		fetchData('/categories', (resp: Category[]) => categories.set(resp));
		fetchData('/transactions', (resp: Transaction[]) => transactions.set(resp));
	})


	function toggleModal(openMenu: number){
		modalOpen = !modalOpen;
		currMenu = openMenu;
	}

</script>
<div class="container">
	<div class={`modal ${currMenu != 0 ? 'is-active' : ''}`}>
		<Editor bind:menuSelection={currMenu} />
	</div>

	<Menu bind:menuSelection={currMenu}/>
	<section class="hero is-primary is-fullheight-with-navbar">
		<div class="hero-body">
			{#if $transactions.length != 0}
				<div class="tile is-ancestor">
					<div class="tile is-vertical">
						<div class="tile">
							<Charts />
						</div>
						<br>
						<div class="tile">
							<Table />
						</div>
					</div>
				</div>
			{/if}
		</div>
	  </section>

</div>


<style>

</style>