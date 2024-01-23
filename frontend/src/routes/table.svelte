<script lang="ts">
	import  type Transaction from '../lib/transaction';
	import { constants } from '../env';
	import { onMount } from 'svelte';
	import  type Category from '../lib/category';

	let netMonth = 0;
	let netYear = 0;
	let isMobile = true;
	export let transactions: Transaction[];
	$: if (transactions) {
		updateBalance();
	}

	const now = new Date();
	const startOfYear = new Date(now.getFullYear(), 0, 1);
	const startOfYearUnix = Math.floor(startOfYear.getTime() / 1000);
	const startOfMonth = new Date(now.getFullYear(), now.getMonth(), 1);
	const startOfMonthUnix = Math.floor(startOfMonth.getTime() / 1000);

	function updateBalance(){
		netMonth = 0;
		netYear = 0;
		transactions.forEach(t => {
			if(t.date> startOfYearUnix){
				netYear += t.amount;
				if(t.date > startOfMonthUnix){
					netMonth += t.amount;
				}
			}
		})
	}

	function formatDate(timestamp: number) {
		const date = new Date(timestamp * 1000);
		return date.toLocaleDateString();
	};

	let categories: Category[] = [];

	onMount(async() => {
		fetchData();
	})

	async function fetchData() {
		try {
			const response = await fetch(constants.API_URL + '/categories');
			categories = await response.json();
			categories.push({
				name: "",
				id: 0,
				parent_id: 0
			})
			console.log(categories)
		} catch (e) {
			console.log(e);
		}
	}

</script>

<div class="container">
	<div class="columns is-flex is-justify-content-center" >
		<div class="column is-half">
			<div class="box">
				<div class="columns is-flex is-justify-content-center is-size-4-mobile" >
					Net Year: ${netYear.toFixed(2)} 
					<br>
					Net Month: ${netMonth.toFixed(2)}
				</div>
			</div>
		</div>
	</div>
	<div class="columns is-flex is-justify-content-center" >
		<div class="box">
			<div class="columns is-flex is-justify-content-center is-size-4-mobile" >
				Last 10 Transactions
			</div>
			<table class="table is-size-6-mobile">
				<thead>
					<tr>
						<th>
							Date
						</th>
						<th>
							To/From
						</th>
						{#if !isMobile}
							<th>
								Method
							</th>
							<th>
								Desc
							</th>
						{/if}
						<th>
							Category
						</th>
						<th>
							Amount
						</th>
					</tr>
				</thead>
				<tbody>
					{#each transactions as transaction}
						<tr>
							<td>
								{formatDate(transaction.date)}
							</td>
							<td>
								{transaction.who}
							</td>
							{#if !isMobile}
								<td>
									{transaction.method}
								</td>
								<td>
									{transaction.desc}
								</td>
							{/if}
							<td>
								{categories.filter(c => c.id == transaction.cat)[0].name}
							</td>
							<td>
								{transaction.amount}
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>


</div>




<style>
  table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
  }

  th, td {
    padding: 8px 16px;
    border-bottom: 1px solid #ddd;
  }

  th {
    background-color: #f4f4f4;
    font-weight: bold;
  }

  tr:nth-child(even) {
    background-color: #f9f9f9;
  }

  tr:hover {
    background-color: #f1f1f1;
  }
</style>