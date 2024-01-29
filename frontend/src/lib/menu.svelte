<nav class="navbar is-fixed-top">
	<div class="navbar-brand">
		<!-- svelte-ignore a11y-interactive-supports-focus -->
		<!-- svelte-ignore a11y-click-events-have-key-events -->
		<!-- svelte-ignore a11y-missing-attribute -->
		<a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" on:click={toggleNavbar}>
			<span aria-hidden="true"></span>
			<span aria-hidden="true"></span>
			<span aria-hidden="true"></span>
		  </a>
	</div>
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<!-- svelte-ignore a11y-missing-attribute -->
	<div class="navbar-menu" class:is-active={navbarOpen}>
		<div class="navbar-start">
			<a class="navbar-item" on:click={() => {selectionMade(1)}}>
				Transaction
			</a>
			<a class="navbar-item" on:click={() => {selectionMade(2)}}>
				Categories	
			</a>
			<a class="navbar-item" on:click={() => {selectionMade(3)}}>
				Methods	
			</a>
		</div>
		<div class="navbar-end">
			<a class="navbar-item" on:click={() => {selectionMade(4)}}>
				Options	
			</a>
			<a class="navbar-item" on:click={() => {selectionMade(5)}}>
				{$email != ""? 'Log Out' : 'Log In'}
			</a>
			{#if $email != ""}
			<a class="navbar-item">
				<strong>
					{$email}	
				</strong>
			</a>
			{/if}
		</div>
	</div>
</nav>

<script lang="ts">
import { menuSelection, email} from "./store";

let navbarOpen = false;

function toggleNavbar(){
	navbarOpen = !navbarOpen;
}

function selectionMade(x: number){
	menuSelection.set(x);
	navbarOpen = false;
	console.log($menuSelection)

}

</script>