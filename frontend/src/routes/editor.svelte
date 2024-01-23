
<div class="modal-background">

</div>
<div class="modal-card">
	<header class="modal-card-head">
		<p class="modal-card-title">Modal title</p>
		<button class="delete" aria-label="close" on:click={() => menuSelection = 0}></button>
	</header>
	<section class="modal-card-body">
		<form >
					<label for="date">Date:</label>
			<input type="date" id="date" bind:value={rawDate} />

			<label for="method">Method:</label>
			<input type="number" id="method" bind:value={method} />

			<label for="who">Who:</label>
			<input type="text" id="who" bind:value={who} />

			<label for="desc">Desc:</label>
			<input type="text" id="desc" bind:value={desc} />

			<label for="category">Category:</label>
			<input type="text" id="category" bind:value={cat} />

			<label for="amount">Amount:</label>
			<input type="number" id="amount" step=".01" bind:value={amount} />

		</form>
	</section>
	<footer class="modal-card-foot">
		<button class="button is-success" on:click|preventDefault={handleSubmit}>Save</button>
		<button class="button" on:click={() => menuSelection = 0}>Cancel</button>
	</footer>
</div>


<script lang="ts">
	import { constants } from '../env';

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
		let date = new Date(rawDate).getTime() / 1000;
		let toSubmit = {
			who, 
			desc,
			cat,
			amount, 
			method, 
			date	
		}

		await fetch(constants.API_URL + '/transactions', {
			method: 'POST',
			headers: {
				'Content-Type' : 'application/json',
			},
			body: JSON.stringify(toSubmit),
		})
		.then(resp => resp.json())
		.then(data => {
			console.log(data);
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