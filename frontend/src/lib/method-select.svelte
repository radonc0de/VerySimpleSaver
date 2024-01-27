<div class="select">
	<select bind:value={method}>
	<option value=0>None</option>
	  {#each $methods as mt}
		<option value={mt.id}>{mt.name}</option>
	  {/each}
	</select>
</div>

<script lang="ts">
	import { methods } from './store';
	export let method = 0;
</script>