export default interface Transaction {
	id: number,
	date: number,
	who: string,
	desc: string,
	cat: number,
	amount: number,
	method: number
}