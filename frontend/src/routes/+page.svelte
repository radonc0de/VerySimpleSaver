<script>
	let date = new Date();
	let method = "";
	let who = "";
	let desc = "";
	let category = 0;
	let amount = 0;
  
	const handleSubmit = () => {
		console.log(method)
	  // Here, you can also add code to handle form submission, like sending data to a server.
	};
</script>

<form on:submit|preventDefault={handleSubmit}>
	<label for="date">Date:</label>
	<input type="datetime-local" id="date" bind:value={date} />

	<label for="method">Method:</label>
	<input type="method" id="method" bind:value={method} />

	<label for="who">Who:</label>
	<input type="text" id="who" bind:value={who} />

	<label for="desc">Desc:</label>
	<input type="text" id="desc" bind:value={desc} />

	<label for="category">Category:</label>
	<input type="text" id="category" bind:value={category} />

	

	<button type="submit">Submit</button>
</form>

<style>
	form {
	display: flex;
	flex-direction: column;
	width: 200px;
	}

	label, input {
	margin-bottom: 10px;
	}

	button {
	background-color: blue;
	color: white;
	padding: 5px 10px;
	border: none;
	border-radius: 5px;
	}

	button:hover {
	background-color: darkblue;
	}
</style>



