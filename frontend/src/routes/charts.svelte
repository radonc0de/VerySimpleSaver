<script lang="ts">
	// @ts-ignore
	import { Pie } from 'svelte-chartjs';
	import {
		Chart as ChartJS,
		Title,
		Tooltip,
		Legend,
		ArcElement,
		CategoryScale,
	// @ts-ignore
	} from 'chart.js';
	import  type Transaction from '../lib/transaction';
	import { onMount } from 'svelte';
	import { transactions, methods, categories } from './store';

	ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);



	function genRecords(): Record<number, number>{
		return $transactions.reduce((acc, transaction) => {
			if (!acc[transaction.cat]) {
				acc[transaction.cat] = 0;
			}
			acc[transaction.cat] += transaction.amount;
			return acc;
		}, {} as Record<number, number>);
	}	

	let loading = true;
	let pieLabels: string[] = [];
	let pieDataSet: number[] = [];
	let pieColors: string[] = [];

	$categories : {
		console.log(genRecords())
		let records = genRecords();
		let toRemove: number[] = [];
		let childRemaining = true;
		while(childRemaining){
			childRemaining = false;
			Object.keys(records).forEach(keyStr => {
				const cat_id = parseInt(keyStr, 10);
				const amount = records[cat_id];
				if (amount < 0) {
					let ctgry = $categories.filter(a => a.id == cat_id)[0];
					if(ctgry.parent_id != 0){
						childRemaining = true;
						if(records[ctgry.parent_id]){
							records[ctgry.parent_id] += amount;
						}else{
							records[ctgry.parent_id] = amount;
						}
						toRemove.push(cat_id)
					}
				}else{
					toRemove.push(cat_id);
				}
			});
			toRemove.forEach(d => delete records[d]);
			toRemove = [];
		}
		Object.keys(records).forEach(keyStr => {
			const cat_id = parseInt(keyStr, 10);
			const amount = records[cat_id];
			let ctgry = $categories.filter(a => a.id == cat_id)[0];
			pieLabels.push(ctgry.name);
			pieColors.push('#' + ctgry.color.toString(16).padStart(6, '0'));
			pieDataSet.push(amount * -1);
		});

		loading = false;
	}

	const data = {
		labels: pieLabels,
		datasets: [
			{
				data: pieDataSet,
				backgroundColor: pieColors
			},
		],
	};

	let options = {
		responsive: true,
		maintainAspectRatio: false,
		legend: {
			display: false
		}
	}

</script>
<div class="container">
	<div class="columns is-flex is-justify-content-center" >
		<div class="column is-half">
			<div class="box">
				<div class="columns is-flex is-justify-content-center is-size-4-mobile" >
					Expenses
				</div>
				<div class="columns is-flex is-justify-content-center is-size-4-mobile" >
					{#if loading == false}
						<Pie 
							data={data} 
							options={options} 
							width={300}
							height={300}
						/>
					{/if}
				</div>
			</div>
		</div>
	</div>
</div>

<style>
.container {
	margin-top: 25px
}
</style>
