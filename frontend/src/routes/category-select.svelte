<div class="select">
	<select bind:value={category}>
	  {#each $categories as cat}
		<option value={cat.id}>{cat.name}</option>
	  {/each}
	</select>
</div>

<script lang="ts">
	import { categories } from './store';
	export let category = 0;

</script>