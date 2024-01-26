<div class="container">
    <div class="columns is-centered">
        <div class="column is-4">
            <div class="box">
                <h3 class="title is-3">Login</h3>
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
                        <button class="button is-primary" on:click={() => {}}>Login</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

