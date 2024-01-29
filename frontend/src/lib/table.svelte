<script lang="ts">
	import { constants } from './env';
	import { transactions, categories, transactionSelected, menuSelection } from './store';

	let netMonth = 0;
	let netYear = 0;
	let totalInc = 0;
	let totalExp = 0;
	let isMobile = true;
	let selectedId = 0;
	$: if (transactions) {
		updateBalance();
	}

	const now = new Date();
	const startOfYear = new Date(Date.UTC(now.getUTCFullYear(), 0, 1));
	const startOfYearUnix = Math.floor(startOfYear.getTime() / 1000);
	const startOfMonth = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), 1));
	const startOfMonthUnix = Math.floor(startOfMonth.getTime() / 1000);

	function updateBalance(){
		netMonth = 0;
		netYear = 0;
		totalInc = 0;
		totalExp = 0;
		$transactions.forEach(t => {
			if(t.date >= startOfYearUnix){
				netYear += t.amount;
				if(t.date >= startOfMonthUnix){
					netMonth += t.amount;
					if(t.amount > 0){
						totalInc += t.amount;
					}else{
						totalExp -= t.amount;
					}
				}
			}
		})
	}

	function formatDate(timestamp: number) {
		const date = new Date(timestamp * 1000);
		const month = date.getUTCMonth() + 1; // getMonth() is zero-based
		const day = date.getUTCDate();
		const formattedMonth = month < 10 ? `0${month}` : `${month}`;
		const formattedDay = day < 10 ? `0${day}` : `${day}`;
		return `${formattedMonth}/${formattedDay}`;
	};

	async function deleteTransaction(){
		await fetch(constants.API_URL + '/transactions', {
			method: 'DELETE',
			headers: {
				'Content-Type' : 'application/json',
			},
			body: JSON.stringify({id: selectedId}),
		})
		.then(resp => resp.json())
		.then(data => {
			transactions.set($transactions.filter(a => a.id != selectedId))
		})
		.catch((err) => {
			console.error('Error:', err);
		})
	}

	function editTransaction(){
		transactionSelected.set($transactions.filter(t => t.id == selectedId)[0]);
		menuSelection.set(1.1);
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
					<br>
					Income This Month: ${totalInc.toFixed(2)}
					<br>
					Expenses This Month: ${totalExp.toFixed(2)}
				</div>
			</div>
		</div>
	</div>
	<div class="columns is-flex is-justify-content-center" >
		<div class="box">
			<div class="columns is-flex is-justify-content-center is-size-4-mobile" >
				Transactions ({$transactions.length})
			</div>
			<div class="columns is-flex is-justify-content-center is-size-4-mobile" >
				{#if selectedId != 0}
				<div class="field is-grouped">
					<div class="control">
						<button class="button is-success" on:click={editTransaction}>Edit</button>
					</div>
					<div class="control">
						<button class="button is-danger" on:click={deleteTransaction}>Delete</button>
					</div>
				</div>
				{/if}
			</div>
			<table class="table is-size-7-mobile">
				<thead>
					<tr>
						<th>
							Date
						</th>
						<th>
							Who	
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
					{#each $transactions as $transaction}
						<tr class:is-selected={selectedId == $transaction.id} on:click={() => {selectedId == $transaction.id? selectedId = 0 : selectedId = $transaction.id}}>
							<td>
								{formatDate($transaction.date)}
							</td>
							<td>
								{$transaction.who}
							</td>
							{#if !isMobile}
								<td>
									{$transaction.method}
								</td>
								<td>
									{$transaction.desc}
								</td>
							{/if}
							<td>
								{categories && $categories.length > 0? $categories.filter(c => c.id == $transaction.cat)[0].name : ""}
							</td>
							<td>
								{$transaction.amount.toFixed(2)}
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>


</div>