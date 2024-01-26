<div class="select">
	<select bind:value={method}>
	<option value=0>None</option>
	  {#each methods as mt}
		<option value={mt.id}>{mt.name}</option>
	  {/each}
	</select>
</div>

<script lang="ts">
	import { constants } from './env';
	import { onMount } from 'svelte';
	import  type Method from '../lib/method';


	export let method = 0;
	let methods : Method[] = [];

	onMount(async() => {
		fetchData();
	})

	async function fetchData() {
		try {
			const response = await fetch(constants.API_URL + '/methods');
			methods = await response.json();
			methods.push({
				name: "",
				id: 0,
			})
			console.log(methods)
		} catch (e) {
			console.log(e);
		}
	}
</script>