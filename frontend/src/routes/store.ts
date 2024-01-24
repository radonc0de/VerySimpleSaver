import { writable } from 'svelte/store';
import type Method from '../lib/method';
import type Category from '../lib/category';
import type Transaction from '../lib/transaction';

export let methods = writable<Method[]>([]);
export let categories = writable<Category[]>([]);
export let transactions = writable<Transaction[]>([]);
