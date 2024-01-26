<nav class="navbar is-fixed-top">
	<div class="navbar-brand">
		<a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" on:click={toggleNavbar} href=".">
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
				Login	
			</a>
		</div>
	</div>
</nav>

<script lang="ts">
	let navbarOpen = false;
	export let menuSelection = 0;

	function toggleNavbar(){
		navbarOpen = !navbarOpen;
	}

	function selectionMade(x: number){
		menuSelection = x;
		navbarOpen = false;
	}

</script>