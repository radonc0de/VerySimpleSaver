<script lang="ts">
	import  type Transaction from '../lib/transaction';

	let netMonth = 0;
	let netYear = 0;
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
		const date = new Date(timestamp);
		return date.toLocaleDateString();
	};


</script>

<div>
	Net Year: {netYear} 
	<br>
	Net Month: {netMonth}

</div>

<h2>Transactions</h2>

<table>
	<thead>
		<tr>
			<th>
				Date
			</th>
			<th>
				To/From
			</th>
			<th>
				Desc
			</th>
			<th>
				Category
			</th>
			<th>
				Amount
			</th>
			<th>
				Method
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
				<td>
					{transaction.desc}
				</td>
				<td>
					{transaction.cat}
				</td>
				<td>
					{transaction.amount}
				</td>
			</tr>
		{/each}
	</tbody>
</table>


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