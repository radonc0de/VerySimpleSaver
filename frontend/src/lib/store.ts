import { writable } from 'svelte/store';
import type Method from '../lib/method';
import type Category from '../lib/category';
import type Transaction from '../lib/transaction';
import { constants } from './env';

export let methods = writable<Method[]>([]);
export let categories = writable<Category[]>([]);
export let transactions = writable<Transaction[]>([]);


export async function getTransactions(){
	let token = localStorage.getItem('token')
	if(token){
		try {
			const response = await fetch(constants.API_URL + '/transactions', {
				method: 'GET',
				headers: {
					'Content-Type' : 'application/json',
					'token': token
				},
			})
			let data = await response.json();
			data = data.sort((a: Transaction, b: Transaction) => b.date - a.date);
			transactions.set(data);
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
			let data = await response.json();
			methods.set(data);
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
			let data = await response.json();
			categories.set(data);
		} catch (e) {
			console.log(e);
		}
	}
}

export async function addTransaction(t: Transaction){
	let token = localStorage.getItem('token')
	if(token){
		await fetch(constants.API_URL + '/transactions', {
			method: 'POST',
			headers: {
				'Content-Type' : 'application/json',
				'token': token
			},
			body: JSON.stringify(t), 
		}).then(resp => resp.json()).then(data => {
			transactions.update(curr => {
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
	await fetch(constants.API_URL + '/categories', {
		method: 'POST',
		headers: {
			'Content-Type' : 'application/json',
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

export async function addMethod(m: Method){
	await fetch(constants.API_URL + '/methods', {
		method: 'POST',
		headers: {
			'Content-Type' : 'application/json',
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
