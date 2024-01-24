
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
						<input id="name" class="input" type="text" bind:value={name} placeholder="Category Name">
					</div>
				</div>

				<div class="field">
					<label class="label" for="category">Parent Category:</label>
					<div class="control">
						<CategorySelect bind:category={parent_id} />
					</div>
				</div>

				<div class="field">
					<label class="label" for="color">Color</label>
					<div class="control">
						<input id="color" class="input" type="color" bind:value={colorString} placeholder=0>
					</div>
				</div>

			{:else if menuSelection == 3}
				<div class="field">
					<label class="label" for="name">Name</label>
					<div class="control">
						<input id="name" class="input" type="text" bind:value={name} placeholder="Method Name">
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
	import type Transaction from '$lib/transaction';
	import type Category from '$lib/category';
	import type Method from '$lib/method';
	import CategorySelect from './category-select.svelte';
	import MethodSelect from './method-select.svelte';
	import { addTransaction, addCategory, addMethod } from './store';

	let rawDate = formatToday();
	let method = 0;
	let who = "";
	let desc = "";
	let cat = 0;
	let amount = 0.0;
	let name = ""
	let colorString = "#FFFFFF";
	let parent_id = 0;
	export let menuSelection = 0;

	function formatToday(): string {
		let date = new Date();
		let year = date.getFullYear();
		let month = (date.getMonth() + 1).toString().padStart(2, '0');
		let day = date.getDate().toString().padStart(2, '0');
		return `${year}-${month}-${day}`;
	}

	async function handleSubmit() {
		if(menuSelection == 1){
			let date = new Date(rawDate).getTime() / 1000;
			let toSubmit: Transaction = {
				id: 0, 
				who, 
				desc,
				cat,
				amount, 
				method, 
				date
			}
			addTransaction(toSubmit);
		}else if(menuSelection == 2){
			let color = parseInt(colorString.slice(1), 16);
			let toSubmit: Category = {
				id: 0,
				name,
				color,
				parent_id
			}
			addCategory(toSubmit);
		}else if(menuSelection == 3){
			let toSubmit: Method = {
				id: 0,
				name,
			}
			addMethod(toSubmit);
		}
		resetFields();
	}


	function resetFields() {
		rawDate = formatToday();
		method = 0;
		who = "";
		desc = "";
		cat = 0;
		amount = 0.0;
		name = ""
		colorString = "#FFFFFF";
		parent_id = 0;
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