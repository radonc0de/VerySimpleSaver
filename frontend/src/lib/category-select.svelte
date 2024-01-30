<div class="select">
	<select id="category" bind:value={category}>
		<option value=0>No Parent</option>
	  {#each $categories as cat}
		<option value={cat.id}>{cat.name}</option>
	  {/each}
	</select>
</div>

<script lang="ts">
	import { categories } from './store';
	export let category = 0;
</script>

<style>
	* {
		width: 100%
	}
</style>