<div class="container">
    <div class="columns is-centered">
        <div class="column is-10">
            <div class="box">
                <h3 class="title is-3">Login</h3>
				<div class="box">
					{notice}
				</div>
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
                        <button class="button is-primary" on:click={login}>Login</button>
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
	export let notice = "";

	async function login(){
		await fetch(constants.API_URL + '/login', {
			method: 'POST',
			headers: {
				'Content-Type' : 'application/json',
			},
			body: JSON.stringify({email, password})
		}).then(resp => resp.json()).then(data => {
			console.log(data.token)
			localStorage.setItem('token', data.token);
			window.location.href = ".";
		})
		.catch((err) => {
			console.error('Error:', err);
			return  null;
		})
	}
</script>