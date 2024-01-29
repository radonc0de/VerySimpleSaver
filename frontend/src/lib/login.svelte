<div class="container">
    <div class="columns is-centered">
        <div class="column is-10">
            <div class="box">
                <h3 class="title is-3">Login</h3>
					{#if info != ""}
						<div class="box has-text-danger">
							{info}
						</div>
					{/if}
					<div class="field">
						<label class="label" for="email">Email</label>
						<div class="control">
							<input class="input" type="email" id="email" placeholder="Enter email" bind:value={email}>
						</div>
					</div>
					<div class="field">
						<label class="label" for="password">Password</label>
						<div class="control">
							<input class="input" type="password" id="password" placeholder="Enter password" bind:value={password}>
						</div>
					</div>
					<div class="field">
						<div class="control">
							<button class="button is-primary" on:click={login} type="submit">Login</button>
						</div>
					</div>
            </div>
        </div>
    </div>
</div>

<script lang="ts">
	import { constants } from './env';

	let email = "";
	let password = "";
	let info = "";

	async function login(){
		console.log(email, password)
		const resp = await fetch(constants.API_URL + '/login', {
			method: 'POST',
			headers: {
				'Content-Type' : 'application/json',
			},
			body: JSON.stringify({email, password})
		});
		if(resp.ok){
			let data = await resp.json();
			console.log(data.token);
			localStorage.setItem('token', data.token);
			window.location.href = ".";
		}else if(resp.status == 401){
			info = "Incorrect email and/or password."
		}else{
			info = "An unknown error has occured."
		}
	}
</script>