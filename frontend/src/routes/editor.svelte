
<div class="modal-background">

</div>
<div class="modal-card">
	<header class="modal-card-head">
		<p class="modal-card-title">
			{#if menuSelection == 1}
				Transaction
			{:else if menuSelection == 2}
				Category
			{:else if menuSelection == 3}
				Method
			{/if}
			Editor 
		</p>
		<button class="delete" aria-label="close" on:click={() => menuSelection = 0}></button>
	</header>
	<section class="modal-card-body">
		<form >
			{#if menuSelection == 1}
				<label for="date">Date:</label>
				<input type="date" id="date" bind:value={rawDate} />

				<label for="method">Method:</label>
				<MethodSelect bind:method={method} />

				<label for="who">Who:</label>
				<input type="text" id="who" bind:value={who} />

				<label for="desc">Desc:</label>
				<input type="text" id="desc" bind:value={desc} />

				<label for="category">Category:</label>
				<CategorySelect bind:category={cat} />

				<label for="amount">Amount:</label>
				<input type="number" id="amount" step=".01" bind:value={amount} />
			{:else if menuSelection == 2}
				<div class="field">
					<label class="label" for="name" >Name</label>
					<div class="control">
						<input id="name" class="input" type="text" bind:value={who} placeholder="Category Name">
					</div>
				</div>

				<div class="field">
					<label class="label" for="category">Parent Category:</label>
					<div class="control">
						<CategorySelect bind:category={cat} />
					</div>
				</div>

			{:else if menuSelection == 3}
				<div class="field">
					<label class="label" for="name">Name</label>
					<div class="control">
						<input id="name" class="input" type="text" bind:value={who} placeholder="Method Name">
					</div>
				</div>
			{/if}
		</form>
	</section>
	<footer class="modal-card-foot">
		<button class="button is-success" on:click|preventDefault={handleSubmit}>Save</button>
		<button class="button" on:click={() => menuSelection = 0}>Cancel</button>
	</footer>
</div>


<script lang="ts">
	import { constants } from '../env';
	import CategorySelect from './category-select.svelte';
	import Menu from './menu.svelte';
	import MethodSelect from './method-select.svelte';

	let rawDate = formatToday();
	let method = 0;
	let who = "";
	let desc = "";
	let cat = 0;
	let amount = 0.0;
	export let menuSelection = 0;

	function formatToday(): string {
		let date = new Date();
		let year = date.getFullYear();
		let month = (date.getMonth() + 1).toString().padStart(2, '0');
		let day = date.getDate().toString().padStart(2, '0');
		return `${year}-${month}-${day}`;
	}


	async function handleSubmit() {
		let toSubmit;
		let path = '/' + (menuSelection == 1? 'transactions' : menuSelection == 2? 'categories' : 'methods');
		if(menuSelection == 1){
			let date = new Date(rawDate).getTime() / 1000;
			toSubmit = {
				who, 
				desc,
				cat,
				amount, 
				method, 
				date	
			}
		}else if(menuSelection == 2){
			toSubmit = {
				who,
				cat	
			}
		}else if(menuSelection == 3){
			toSubmit = {
				who
			}
		}
		await fetch(constants.API_URL + path, {
			method: 'POST',
			headers: {
				'Content-Type' : 'application/json',
			},
			body: JSON.stringify(toSubmit),
		})
		.then(resp => resp.json())
		.then(data => {
			menuSelection = 0;
		})
		.catch((err) => {
			console.error('Error:', err);
		})
	}
</script>


<style>
	form {
	display: flex;
	flex-direction: column;
	width: 200px;
	}

	label, input {
	margin-bottom: 10px;
	}

</style>