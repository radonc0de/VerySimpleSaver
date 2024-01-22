<script lang="ts">
	import  type Transaction from '../lib/transaction';
	import { onMount } from 'svelte';
	import Table from './table.svelte';
	import Editor from './editor.svelte'
	import { constants } from '../env';

	let transactions: Transaction[] = [];

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

</script>

<Editor />
<Table transactions={transactions} />