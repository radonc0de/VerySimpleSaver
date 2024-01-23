<div class="select">
	<select bind:value={category}>
	  {#each categories as cat}
		<option value={cat.id}>{cat.name}</option>
	  {/each}
	</select>
</div>

<script lang="ts">
	import { constants } from '../env';
	import { onMount } from 'svelte';
	import  type Category from '../lib/category';


	export let category = 0;
	let categories: Category[] = [];

	onMount(async() => {
		fetchData();
	})

	async function fetchData() {
		try {
			const response = await fetch(constants.API_URL + '/categories');
			categories = await response.json();
			categories.push({
				name: "",
				id: 0,
				parent_id: 0
			})
			console.log(categories)
		} catch (e) {
			console.log(e);
		}
	}
</script>