<script lang="ts">
	import  type Transaction from '../lib/transaction';
	import { onMount } from 'svelte';
	import Table from './table.svelte';
	import Editor from './editor.svelte'
	import Menu from './menu.svelte';
	import { constants } from '../env';

	let transactions: Transaction[] = [];
	let modalOpen = false;
	let currMenu = 0;

	async function fetchData() {
		try {
			const response = await fetch(constants.API_URL + '/transactions');
			transactions = await response.json();
			console.log(transactions)
		} catch (e) {
			console.log(e);
		}
	}

	onMount(async() => {
		fetchData();
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
		  <p class="title">
			<Table transactions={transactions} />
		  </p>
		</div>
	  </section>

</div>


<style>

</style>