import { writable } from 'svelte/store';
import type Method from '../lib/method';
import type Category from '../lib/category';
import type Transaction from '../lib/transaction';
import { constants } from './env';

export let methods = writable<Method[]>([]);
export let categories = writable<Category[]>([]);
export let transactions = writable<Transaction[]>([]);
export let menuSelection = writable<number>();
export let email = writable<string>("");
export let transactionSelected = writable<Transaction>();

menuSelection.set(0)
let token = localStorage.getItem('token')
if(token){
	try{
		let payloadJSON = atob(token.split('.')[1]);
		let payload = JSON.parse(payloadJSON);
		email.set(payload.email)
		menuSelection.set(0);
	}
	catch{
		menuSelection.set(5.1);
	}
}else{
	menuSelection.set(5);
}

export async function getTransactions(){
	let token = localStorage.getItem('token')
	if(token){
		try {
			const resp = await fetch(constants.API_URL + '/transactions', {
				method: 'GET',
				headers: {
					'Content-Type' : 'application/json',
					'token': token
				},
			});
			if(resp.ok){
				let data = await resp.json();
				data = data.sort((a: Transaction, b: Transaction) => b.date - a.date);
				transactions.set(data);
			} else if(resp.status == 401){
				console.log("UNAUTH")
				menuSelection.set(5.1)
				email.set("")
			}else{
				throw Error;
			}
		} catch (e) {
			console.log(e);
		}
	}
}

export async function getMethods(){
	let token = localStorage.getItem('token')
	if(token){
		try {
			const response = await fetch(constants.API_URL + '/methods', {
				method: 'GET',
				headers: {
					'Content-Type' : 'application/json',
					'token': token
				},
			})
			if (response.ok){
				let data = await response.json();
				methods.set(data);
			} else if (response.status == 401){
				console.log("UNAUTHORIZED");
				menuSelection.set(5.1)
				email.set("")
			}else{
				throw Error;
			}
		} catch (e) {
			console.log(e);
		}
	}
}

export async function getCategories(){
	let token = localStorage.getItem('token')
	if(token){
		try {
			const response = await fetch(constants.API_URL + '/categories', {
				method: 'GET',
				headers: {
					'Content-Type' : 'application/json',
					'token': token
				},
			})
			if(response.ok){
				let data = await response.json();
				categories.set(data);
			}else if (response.status == 401){
				console.log("UNAUTHORIZED");
				menuSelection.set(5.1)
				email.set("")
			}else{
				throw Error;
			}
		} catch (e) {
			console.log(e);
		}
	}
}

export async function editTransaction(t: Transaction){
	let token = localStorage.getItem('token')
	if(token){
		await fetch(constants.API_URL + '/transactions', {
			method:t.id != 0? 'PUT' : 'POST',
			headers: {
				'Content-Type' : 'application/json',
				'token': token
			},
			body: JSON.stringify(t), 
		}).then(resp => resp.json()).then(data => {
			transactions.update(curr => {
				curr = curr.filter(a => a.id != t.id);
				curr.push(data as Transaction);
				return curr.sort((a, b) => b.date - a.date);
			})
		})
		.catch((err) => {
			console.error('Error:', err);
			return  null;
		})
	}
}

export async function addCategory(c: Category){
	let token = localStorage.getItem('token')
	if(token){
		await fetch(constants.API_URL + '/categories', {
			method: 'POST',
			headers: {
				'Content-Type' : 'application/json',
				'token': token
			},
			body: JSON.stringify(c), 
		}).then(resp => resp.json()).then(data => {
			categories.update(curr => {
				curr.push(data as Category);
				return curr;
			})
		})
		.catch((err) => {
			console.error('Error:', err);
			return  null;
		})
	}
}

export async function addMethod(m: Method){
	let token = localStorage.getItem('token')
	if(token){
		await fetch(constants.API_URL + '/methods', {
			method: 'POST',
			headers: {
				'Content-Type' : 'application/json',
				'token': token
			},
			body: JSON.stringify(m), 
		}).then(resp => resp.json()).then(data => {
			methods.update(curr => {
				curr.push(data as Method);
				return curr;
			})
		})
		.catch((err) => {
			console.error('Error:', err);
			return  null;
		})
	}
}