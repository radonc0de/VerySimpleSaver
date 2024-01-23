<nav class="navbar is-fixed-top">
	<div class="navbar-brand">
		<a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" on:click={toggleNavbar} href=".">
			<span aria-hidden="true"></span>
			<span aria-hidden="true"></span>
			<span aria-hidden="true"></span>
		  </a>
	</div>
	<div class="navbar-menu" class:is-active={navbarOpen}>
		<div class="navbar-start">
			<a class="navbar-item" href="." on:click={() => {menuSelection = 1}}>
				Transaction
			</a>
			<a class="navbar-item" href="." on:click={() => {menuSelection = 2}}>
				Categories	
			</a>
			<a class="navbar-item" href="." on:click={() => {menuSelection = 3}}>
				Methods	
			</a>
		</div>
		<div class="navbar-end">
			<a class="navbar-item" href="." on:click={() => {menuSelection = 4}}>
				Options	
			</a>
		</div>
	</div>
</nav>

<script>
	let navbarOpen = false;
	export let menuSelection = 0;

	function toggleNavbar(){
		navbarOpen = !navbarOpen;
	}

	function selectionMade(){

	}

</script>