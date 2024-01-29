
<div class="modal-background">

</div>
<div class="modal-card">
	<header class="modal-card-head">
		<p class="modal-card-title">
			{#if $menuSelection >= 5}
				Account
			{:else if $menuSelection == 4}
				Options	
			{:else}
				{#if $menuSelection == 1}
					Transaction
				{:else if $menuSelection == 2}
					Category
				{:else if $menuSelection == 3}
					Method
				{/if}
				Editor 
			{/if}
		</p>
		<button class="delete" aria-label="close" on:click={exitModal}></button>
	</header>
	{#if $menuSelection < 4}
		<section class="modal-card-body">
			<div class="container">
				<form >
					{#if $menuSelection >= 1 && $menuSelection < 2}
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
					{:else if $menuSelection == 2}
						<div class="field">
							<label class="label" for="category">Edit a Category:</label>
							<div class="control">
								<CategorySelect bind:category={categoryEdittingId} />
							</div>
						</div>

						<div class="field">
							<label class="label" for="name" >Name</label>
							<div class="control">
								<input id="name" class="input" type="text" bind:value={name} placeholder="Category Name">
							</div>
						</div>

						<div class="field">
							<label class="label" for="category">Parent Category:</label>
							<div class="control">
								<CategorySelect  bind:category={parent_id} />
							</div>
						</div>

						<div class="field">
							<label class="label" for="color">Color</label>
							<div class="control">
								<input id="color" class="input" type="color" bind:value={colorString} placeholder=0>
							</div>
						</div>

					{:else if $menuSelection == 3}
						<div class="field">
							<label class="label" for="name">Name</label>
							<div class="control">
								<input id="name" class="input" type="text" bind:value={name} placeholder="Method Name">
							</div>
						</div>
					{/if}
				</form>
			</div>
		</section>
		<footer class="modal-card-foot">
			<button class="button is-success" on:click|preventDefault={handleSubmit}>Save</button>
			<button class="button" on:click={exitModal}>Cancel</button>
		</footer>
	{:else if $menuSelection >= 5}
		<section class="modal-card-body">
			{#if $email  && $email != ""}
				<div class="container has-text-centered">
					<button class="button is-danger" on:click={() => logOut(true)}>Log Out</button>
				</div>
			{:else if !login && !createAccount}
				<div class="tile is-ancestor">
					<div class="tile is-parent">
						<div class="tile">
							<div class="container has-text-centered">
								<button class="button is-success" on:click={() => login = true}>Log In</button>
							</div>
						</div>
						<div class="tile">
							<div class="container has-text-centered">
								<button class="button is-info" on:click={() => createAccount = true}>Sign up</button>
							</div>
						</div>
					</div>
				</div>
			{:else if login}
				<Login />
			{:else}
				<CreateAccount />
			{/if}
		</section>
		<footer class="modal-card-foot">
		</footer>
	{:else}
		<section class="modal-card-body">
			<div class="container has-text-centered">
			</div>
		</section>
		<footer class="modal-card-foot">
		</footer>
		
	{/if}
</div>

<script lang="ts">
import type Transaction from './transaction';
import type Category from './category';
import type Method from './method';
import CategorySelect from './category-select.svelte';
import MethodSelect from './method-select.svelte';
import { editTransaction, editCategory, addMethod, menuSelection, email, transactionSelected, categories, methods} from './store';
import Login from './login.svelte';
import CreateAccount from './createAccount.svelte';
import { onMount } from 'svelte';

let login = false
let createAccount = false
let rawDate = formatToday();
let method = 0;
let who = "";
let desc = "";
let cat = 0;
let amount = 0.0;
let name = ""
let colorString = "#FFFFFF";
let parent_id = 0;
let copiedTransaction = false;
let lastCopiedCategory = 0;
let categoryEdittingId = 0;
let methodEditting = 0

$: if(categoryEdittingId && categoryEdittingId != lastCopiedCategory) {
	let ctgry = $categories.filter(a => a.id == categoryEdittingId)[0];
	name = ctgry.name;
	parent_id = ctgry.parent_id;
	colorString = '#' + ctgry.color.toString(16).padStart(6, '0');
	lastCopiedCategory = categoryEdittingId;
}

// handle unauthorized request redirect to login
$: if (menuSelection){
	if($menuSelection == 5.1){
		logOut(false);
	}else if($menuSelection == 1.1){
		if ($transactionSelected && !copiedTransaction) {
			console.log('yah')
			method = $transactionSelected.method;
			who = $transactionSelected.who;
			desc = $transactionSelected.desc;
			cat = $transactionSelected.cat;
			amount = $transactionSelected.amount;
			rawDate = formatToday($transactionSelected.date)
			copiedTransaction = true;
		}
	}
}

function exitModal() {
	login = false;
	createAccount = false;
	resetFields();
	menuSelection.set(0);
}

function formatToday(optDate?: number): string {
	let year, month, day;
	if(optDate){
		let date = new Date(optDate * 1000)
		year = date.getUTCFullYear();
		month = (date.getUTCMonth() + 1).toString().padStart(2, '0');
		day = date.getUTCDate().toString().padStart(2, '0');
	}else{
		let date = new Date();
		year = date.getFullYear();
		month = (date.getMonth() + 1).toString().padStart(2, '0');
		day = date.getDate().toString().padStart(2, '0');
	}
	return `${year}-${month}-${day}`;
}

async function handleSubmit() {
	if($menuSelection < 2){
		let date = new Date(rawDate).getTime() / 1000;
		let toSubmit: Transaction = {
			id: $menuSelection == 1.1 && $transactionSelected && $transactionSelected.id? $transactionSelected.id : 0, 
			who, 
			desc,
			cat,
			amount, 
			method, 
			date
		}
		editTransaction(toSubmit);
	}else if($menuSelection == 2){
		let color = parseInt(colorString.slice(1), 16);
		let toSubmit: Category = {
			id: categoryEdittingId != 0? categoryEdittingId : 0,
			name,
			color,
			parent_id
		}
		editCategory(toSubmit);
	}else if($menuSelection == 3){
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
	copiedTransaction = false;
}

function logOut(refresh: boolean){
	console.log("calling logout. refresh = ", refresh); 
	localStorage.removeItem('token');
	if(refresh) window.location.href = ".";
}
</script>


<style>
	form {
		display: flex;
		flex-direction: column;
	}

	label, input {
		margin-bottom: 10px;
	}

</style>