
<div class="container">
    <div class="columns is-centered">
        <div class="column is-10">
            <div class="box">
                <h3 class="title is-3">Create Account</h3>
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
                        <button class="button is-primary" on:click={createAccount}>Create Account</button>
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

	async function createAccount(){
		let body = JSON.stringify({email, password});
		console.log(body);

		await fetch(constants.API_URL + '/createaccount', {
			method: 'POST',
			headers: {
				'Content-Type' : 'application/json',
			},
			body: body, 
		}).then(resp =>  {
			window.location.href = ".";
		})
		.catch((err) => {
			console.error('Error:', err);
			return  null;
		})
	}
</script>